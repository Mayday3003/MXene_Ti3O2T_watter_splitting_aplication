#!/usr/bin/env python3
"""
make_tio2_wulff_mp390.py

1) Descarga la estructura mp-390 (TiO2 anatasa) desde Materials Project (usa tu API key).
2) Usa las γ(hkl) PBE-relajadas de la Tabla II (Lazzeri et al., PRB 2001) para construir
   la Wulff-shape mediante desigualdades n·r <= d_i (d_i ∝ γ_i).
3) Recorta una supercelda y guarda la nanopartícula atómica (Ti + O).

Uso:
    export MP_API_KEY="TU_API_KEY"
    python make_tio2_wulff_mp390.py --scale 30 --out particle.cif

Dependencias:
    pip install pymatgen ase numpy
"""

import os
import argparse
import numpy as np
from pymatgen.ext.matproj import MPRester
from pymatgen.core import Structure, Lattice
from pymatgen.io.ase import AseAtomsAdaptor

try:
    from ase.io import write as ase_write
    ASE_AVAILABLE = True
except Exception:
    ASE_AVAILABLE = False

# -------------------------
# Superficie gamma (PBE RELAX) - Tabla II (Lazzeri et al., PRB 2001)
# Usamos estas magnitudes como proporciones; 'scale' controla tamaño absoluto.
# -------------------------
surface_energies = {
    (1, 0, 1): 0.49,   # (101) PBE relajado
    (1, 0, 0): 0.58,   # (100)
    (0, 0, 1): 0.98,   # (001)
    (1, 0, 3): 0.90    # (103)_f - si prefieres (103)_s usar ~0.99
}

def miller_to_normal(hkl, lattice: Lattice):
    """
    Calcula la normal unitaria en coordenadas cartesianas para un plano (h,k,l)
    con respecto a la celda dada (usa la base recíproca cristalográfica).
    """
    h, k, l = hkl
    recip_mat = lattice.reciprocal_lattice_crystallographic.matrix
    g = np.dot(np.array([h, k, l], dtype=float), recip_mat)
    norm = np.linalg.norm(g)
    if norm == 0:
        raise ValueError(f"Miller {hkl} inválido para la celda dada")
    n = g / norm
    return n

def build_supercell(structure, max_extent_angstrom):
    """
    Construye una supercelda suficientemente grande para contener la partícula.
    max_extent_angstrom: radio aproximado que queremos cubrir en Å.
    """
    a_vecs = structure.lattice.matrix
    norms = np.linalg.norm(a_vecs, axis=1)
    reps = [max(3, int(np.ceil(2 * max_extent_angstrom / n)) + 2) for n in norms]
    supercell = structure * tuple(reps)
    return supercell

def cut_cluster(supercell, normals, gammas_scaled, tol=1e-8):
    """
    Filtra átomos dentro del poliedro |n·r| <= d_i para todas las facetas.
    Retorna un objeto pymatgen.Structure con la cluster atómica (sin periodicidad).
    """
    coords = supercell.cart_coords.copy()
    center = coords.mean(axis=0)
    coords_centered = coords - center
    species = [site.specie for site in supercell]
    inside_coords = []
    inside_species = []
    for i, r in enumerate(coords_centered):
        keep = True
        for n, d in zip(normals, gammas_scaled):
            if abs(np.dot(n, r)) > d + tol:
                keep = False
                break
        if keep:
            inside_coords.append(r)
            inside_species.append(species[i])
    if len(inside_coords) == 0:
        raise RuntimeError("No atoms inside la Wulff con esos parámetros. Aumenta 'scale'.")
    coords_arr = np.array(inside_coords)
    minc = coords_arr.min(axis=0) - 5.0
    maxc = coords_arr.max(axis=0) + 5.0
    box_lengths = maxc - minc
    L = max(box_lengths.max(), 20.0)
    lattice = Lattice.cubic(L)
    frac_sites = [lattice.get_fractional_coords(pos - minc) for pos in coords_arr]
    species_symbols = [sp.symbol for sp in inside_species]
    new_struct = Structure(lattice, species_symbols, frac_sites, coords_are_cartesian=False)
    return new_struct

def main():
    parser = argparse.ArgumentParser(description="Construir nanopartícula TiO2 (anatasa) a partir de mp-390 y Tabla II (PBE).")
    parser.add_argument("--mp_api", default=os.environ.get("MP_API_KEY", ""), help="Materials Project API key (o exportar MP_API_KEY).")
    parser.add_argument("--scale", "-s", type=float, default=30.0, help="Factor de escala (Å) multiplicado por γ para dar tamaño absoluto.")
    parser.add_argument("--out", "-o", default="particle.cif", help="Archivo de salida (particle.cif o particle.xyz).")
    parser.add_argument("--save_cell", action="store_true", help="Guardar anatase.cif descargado de MP (por defecto no).")
    args = parser.parse_args()

    api_key = args.mp_api or os.environ.get("MP_API_KEY", "")
    if not api_key:
        raise RuntimeError("Necesitas una Materials Project API key. Pásala con --mp_api o exportando MP_API_KEY.")

    # 1) descargar estructura mp-390
    print("Descargando mp-390 desde Materials Project...")
    try:
        with MPRester(api_key) as m:
            struct = m.get_structure_by_material_id("mp-390")
    except Exception as e:
        raise RuntimeError(f"Error al descargar estructura: {e}")
    print("Estructura descargada: fórmula =", struct.composition.reduced_formula)
    if args.save_cell:
        print("Guardando 'anatase_from_mp.cif'...")
        ase_atoms = AseAtomsAdaptor.get_atoms(struct)
        ase_write("anatase_from_mp.cif", ase_atoms)
        print("Guardado.")

    # 2) calcular normales y distancias escaladas d_i = scale * gamma_i
    normals = []
    gammas_scaled = []
    for hkl, gamma in surface_energies.items():
        n = miller_to_normal(hkl, struct.lattice)
        normals.append(n)
        gammas_scaled.append(args.scale * float(gamma))
    print("Facetas usadas:", list(surface_energies.keys()))
    # 3) construir supercelda
    max_d = max(gammas_scaled)
    supercell = build_supercell(struct, max_extent_angstrom=2 * max_d + 5.0)
    print("Supercelda creada. sitios en supercelda:", len(supercell.sites))
    # 4) recortar cluster
    cluster = cut_cluster(supercell, normals, gammas_scaled)
    print("Átomos en nanopartícula resultante:", len(cluster.sites))
    # 5) guardar resultado
    out = args.out
    if out.lower().endswith(".cif"):
        cluster.to(filename=out)
        print("Guardado en:", out)
    elif out.lower().endswith(".xyz"):
        if ASE_AVAILABLE:
            atoms = AseAtomsAdaptor.get_atoms(cluster)
            ase_write(out, atoms)
            print("Guardado en XYZ:", out)
        else:
            with open(out, "w") as f:
                f.write(str(len(cluster.sites)) + "\n")
                f.write("TiO2 cluster\n")
                for site in cluster.sites:
                    f.write(f"{site.specie} {site.x:.6f} {site.y:.6f} {site.z:.6f}\n")
            print("Guardado (fallback) en:", out)
    else:
        cluster.to(filename=out)
        print("Guardado en:", out)

    # Visualizar nanopartícula si ASE está disponible
    if ASE_AVAILABLE:
        try:
            from ase.visualize import view
            atoms = AseAtomsAdaptor.get_atoms(cluster)
            print("Mostrando nanopartícula en visor ASE...")
            view(atoms)
        except Exception as e:
            print(f"No se pudo visualizar la nanopartícula: {e}")
    else:
        print("ASE no está disponible para visualización interactiva.")

if __name__ == "__main__":
    main()
