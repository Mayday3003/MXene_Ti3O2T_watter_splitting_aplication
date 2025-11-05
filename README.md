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

### Despliegue Automático

El libro se construye y despliega automáticamente en GitHub Pages cada vez que se hace push a la rama `main`. El proceso incluye:

1. **GitHub Actions** ejecuta el workflow definido en `.github/workflows/build-book.yml`
2. Se instalan las dependencias necesarias desde `requirements.txt`
3. Se construye el Jupyter Book con `jupyter-book build book/`
4. El HTML generado se despliega en la rama `gh-pages`
5. GitHub Pages publica el contenido en: https://mayday3003.github.io/MXene_Ti3O2T_watter_splitting_aplication/

No se requiere ninguna acción manual para el despliegue.

## Abrir en Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Mayday3003/MXene_Ti3O2T_watter_splitting_aplication/HEAD?urlpath=lab/tree/book/)
