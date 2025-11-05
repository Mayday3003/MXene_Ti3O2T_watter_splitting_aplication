# ¿Cómo Ver el Jupyter Book?

Este documento te guía paso a paso sobre cómo visualizar tu Jupyter Book ya creado.

## 🌐 Opción 1: Ver el Libro en Línea (Más Fácil)

El libro está automáticamente desplegado en GitHub Pages. Simplemente abre tu navegador y visita:

**🔗 [https://mayday3003.github.io/MXene_Ti3O2T_watter_splitting_aplication/](https://mayday3003.github.io/MXene_Ti3O2T_watter_splitting_aplication/)**

Esta es la forma más rápida y fácil de ver tu libro sin necesidad de instalar nada.

### Actualización Automática

Cada vez que haces un `push` a la rama `main`, GitHub Actions automáticamente:
1. Construye el libro
2. Lo despliega en GitHub Pages
3. Actualiza la versión en línea

Puedes ver el estado del despliegue en la pestaña "Actions" de tu repositorio.

## 💻 Opción 2: Ver el Libro Localmente

Si necesitas ver el libro en tu computadora local (por ejemplo, para revisar cambios antes de publicarlos), sigue estos pasos:

### Paso 1: Instalar las Dependencias

Primero, asegúrate de tener Python 3.8 o superior instalado. Luego, instala las dependencias necesarias:

```bash
# Opción A: Usar pip (recomendado para instalación rápida)
pip install -r requirements.txt

# Opción B: Usar conda/mamba (recomendado para desarrollo completo)
mamba env create -f environment.yml
conda activate matbook
```

### Paso 2: Construir el Libro

Navega a la carpeta raíz del repositorio y ejecuta:

```bash
jupyter-book build book/
```

Este comando:
- Lee los archivos fuente en `book/`
- Genera HTML estático en `book/_build/html/`
- Muestra cualquier error o advertencia

### Paso 3: Abrir el Libro en tu Navegador

Una vez construido, puedes abrir el libro de dos formas:

#### Opción A: Abrir directamente el archivo HTML

```bash
# En Linux/Mac:
open book/_build/html/index.html

# En Windows:
start book/_build/html/index.html

# O simplemente navega manualmente a la carpeta y abre index.html con tu navegador
```

#### Opción B: Usar un servidor HTTP local (Recomendado)

Para mejor experiencia (enlaces, JavaScript, etc.):

```bash
# Opción 1: Con Python
cd book/_build/html
python -m http.server 8000

# Opción 2: Con Node.js (si tienes npx)
cd book/_build/html
npx http-server -p 8000

# Luego abre en tu navegador:
# http://localhost:8000
```

### Reconstruir el Libro Después de Cambios

Si modificas algún archivo del libro, simplemente vuelve a ejecutar:

```bash
jupyter-book build book/
```

Para forzar una reconstrucción completa (útil si hay problemas):

```bash
jupyter-book clean book/
jupyter-book build book/
```

## 🚀 Opción 3: Usar Binder (Interactivo)

Si quieres ejecutar los notebooks de forma interactiva sin instalar nada:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Mayday3003/MXene_Ti3O2T_watter_splitting_aplication/HEAD?urlpath=lab/tree/book/)

Haz clic en el badge de arriba o visita directamente el enlace de Binder. Esto abrirá un JupyterLab en la nube con todos los notebooks del libro.

## 📋 Estructura del Libro

El libro está organizado en:

- **Introducción**: MXenes Jupyter Notebook
- **Investigación Preliminar**: Punto 3
- **Minería de Datos**: Data Mining Notebook
- **Superficie y Nanopartícula**: Nanomateriales Completo
- **Superficie**: Ejemplo de Nanopartícula con Wulffpack

Toda la configuración se encuentra en:
- `book/_config.yml`: Configuración general del libro
- `book/_toc.yml`: Tabla de contenidos y estructura

## ❓ Solución de Problemas

### Error: "jupyter-book: command not found"

```bash
pip install 'jupyter-book>=0.15.0,<1.0.0'
```

**Nota importante**: Este libro fue creado con Jupyter Book 0.15.x. La versión 2.0+ tiene una interfaz completamente diferente y no es compatible. Asegúrate de instalar la versión correcta usando `pip install -r requirements.txt`.

### Error al construir: "No module named '...'"

Asegúrate de haber instalado todas las dependencias:

```bash
pip install -r requirements.txt
```

### El libro en línea no se actualiza

1. Verifica que tu push llegó a la rama `main`
2. Revisa la pestaña "Actions" en GitHub para ver si el workflow está ejecutándose
3. Espera unos minutos - GitHub Pages puede tardar en actualizar

### Los cambios locales no se reflejan

Reconstruye el libro forzando limpieza:

```bash
jupyter-book clean book/
jupyter-book build book/
```

## 📚 Recursos Adicionales

- [Documentación oficial de Jupyter Book](https://jupyterbook.org/)
- [Guía de MyST Markdown](https://myst-parser.readthedocs.io/)
- [Repositorio de este proyecto](https://github.com/Mayday3003/MXene_Ti3O2T_watter_splitting_aplication)
