# Jupyter Book - Ciencia de Materiales

Este repositorio contiene un libro interactivo para ciencia de materiales usando ASE, pymatgen, wulffpack y pyxtal.

## 📖 ¿Cómo Ver el Libro?

**👉 [Lee la guía completa aquí: COMO_VER_LIBRO.md](COMO_VER_LIBRO.md)**

**Acceso rápido:**
- **En línea**: [Ver Jupyter Book en GitHub Pages](https://mayday3003.github.io/MXene_Ti3O2T_watter_splitting_aplication/)
- **Interactivo**: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Mayday3003/MXene_Ti3O2T_watter_splitting_aplication/HEAD?urlpath=lab/tree/book/)
- **Local**: `jupyter-book build book/` (ver [COMO_VER_LIBRO.md](COMO_VER_LIBRO.md) para detalles)

## Estructura principal

- Carpeta `book/`: contiene el Jupyter Book y sus recursos.
- Carpeta `src/matbook/`: código fuente reutilizable.
- Archivos de entorno y despliegue: `environment.yml`, `requirements.txt`, `postBuild`, `Dockerfile`, `.github/workflows/`, etc.

## Desarrollo y Construcción

Para trabajar con el libro localmente:

```bash
# Instalar dependencias
mamba env create -f environment.yml
conda activate matbook

# Construir el libro
jupyter-book build book/
```

Para más detalles sobre cómo ver y trabajar con el libro, consulta [COMO_VER_LIBRO.md](COMO_VER_LIBRO.md).
