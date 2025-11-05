# Jupyter Book - Ciencia de Materiales

Este repositorio contiene un libro interactivo para ciencia de materiales usando ASE, pymatgen, wulffpack y pyxtal.

## Estructura principal

- Carpeta `book/`: contiene el Jupyter Book y sus recursos.
- Carpeta `src/matbook/`: código fuente reutilizable.
- Archivos de entorno y despliegue: `environment.yml`, `requirements.txt`, `postBuild`, `Dockerfile`, `.github/workflows/`, etc.

## Cómo construir el libro

```bash
mamba env create -f environment.yml
conda activate matbook
jupyter-book build book/
```

## Ver el Libro Online

El libro está desplegado automáticamente en GitHub Pages: [Ver Jupyter Book](https://mayday3003.github.io/MXene_Ti3O2T_watter_splitting_aplication/)

## Abrir en Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Mayday3003/MXene_Ti3O2T_watter_splitting_aplication/HEAD?urlpath=lab/tree/book/)
