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

## Abrir en Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/TU_USUARIO/TU_REPO/HEAD?urlpath=lab/tree/book/)

## Abrir en Colab

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TU_USUARIO/TU_REPO/blob/main/book/tutorials/tutorial_01_generate_crystals.ipynb)
