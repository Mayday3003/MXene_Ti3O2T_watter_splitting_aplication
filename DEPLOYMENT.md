# Guía de Despliegue en GitHub Pages

Este documento explica cómo funciona el despliegue automático del Jupyter Book en GitHub Pages.

## Configuración Actual

### 1. GitHub Actions Workflow

El archivo `.github/workflows/build-book.yml` define el proceso de construcción y despliegue:

- **Trigger**: Se ejecuta automáticamente en cada push a la rama `main`, en pull requests, o manualmente
- **Permisos**: Tiene permisos de escritura para desplegar en GitHub Pages
- **Proceso**:
  1. Checkout del código
  2. Configuración de Python 3.10
  3. Instalación de dependencias desde `requirements.txt`
  4. Construcción del libro con `jupyter-book build book/`
  5. Creación del archivo `.nojekyll` para evitar procesamiento de Jekyll
  6. Despliegue del HTML generado a la rama `gh-pages`

### 2. Requisitos del Sistema

El archivo `requirements.txt` especifica:
- `jupyter-book==0.15.1` - Versión específica compatible con la configuración existente
- Temas y extensiones de Sphinx necesarios para el libro

### 3. Configuración del Libro

- **Configuración principal**: `book/_config.yml`
  - Define título, autor, repositorio
  - Configura opciones de ejecución de notebooks
  - Establece el tema y idioma (español)
  
- **Tabla de contenidos**: `book/_toc.yml`
  - Estructura el libro en secciones y capítulos
  - Define el orden de los notebooks

## URL de Acceso

Una vez desplegado, el libro es accesible en:
**https://mayday3003.github.io/MXene_Ti3O2T_watter_splitting_aplication/**

## Verificación del Despliegue

Para verificar que el despliegue funcionó:

1. Ir a la pestaña "Actions" en GitHub
2. Buscar el workflow "Build and deploy Jupyter Book"
3. Verificar que la última ejecución fue exitosa (marca verde ✓)
4. Visitar la URL del libro para confirmar que está actualizado

## Configuración de GitHub Pages en el Repositorio

GitHub Pages debe estar configurado en el repositorio para servir desde la rama `gh-pages`:

1. Ir a Settings > Pages en el repositorio GitHub
2. Verificar que "Source" esté configurado como "Deploy from a branch"
3. Verificar que "Branch" esté configurado en `gh-pages` y carpeta `/ (root)`

## Resolución de Problemas

### El workflow falla en la construcción

- Verificar los logs en la pestaña Actions
- Asegurarse de que todos los notebooks en `_toc.yml` existen
- Verificar que no hay errores de sintaxis en `_config.yml` o `_toc.yml`

### El sitio no se actualiza

- Esperar unos minutos después del despliegue exitoso
- Verificar en Settings > Pages que GitHub Pages está habilitado
- Limpiar caché del navegador

### Errores 404 al acceder a páginas

- Verificar que el archivo `.nojekyll` se creó en la rama `gh-pages`
- Verificar que la estructura de URLs coincide con los nombres de archivo

## Mantenimiento

### Actualizar el contenido

1. Modificar los notebooks en la carpeta `book/`
2. Hacer commit y push a la rama que se fusionará con `main`
3. El despliegue ocurrirá automáticamente al fusionar con `main`

### Actualizar dependencias

1. Modificar `requirements.txt` con las nuevas versiones
2. Probar localmente que el libro se construye correctamente
3. Hacer commit y push para desplegar

### Cambiar la estructura del libro

1. Modificar `book/_toc.yml` con la nueva estructura
2. Asegurarse de que todos los archivos referenciados existen
3. Hacer commit y push para desplegar

## Notas Importantes

- **No se requiere acción manual** para el despliegue después del push a `main`
- El workflow usa `force_orphan: true` para mantener la rama `gh-pages` limpia
- La versión de Jupyter Book está fijada en 0.15.1 para compatibilidad
- El archivo `.nojekyll` es crítico para que GitHub Pages sirva correctamente los archivos estáticos
