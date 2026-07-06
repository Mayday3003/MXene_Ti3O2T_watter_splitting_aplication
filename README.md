# MXene Ti3O2T Water Splitting Research

This repository collects exploratory notebooks, data mining workflows, and materials-analysis examples focused on MXene Ti3O2T systems for water splitting research.

## Project Overview

The workspace is organized as a set of themed folders so each stage of the research process is easy to find:

- `introduction/`: foundational MXene notes and overview material.
- `preliminary-research/`: literature-oriented search and early screening notebooks, plus extracted search results.
- `data-mining/`: data extraction, filtering, and analysis workflows.
- `surface-and-nanoparticles/`: surface and nanoparticle modeling notebooks.
- `surface/`: Wulff construction and nanoparticle examples.

Key notebooks:

- `introduction/mxene-overview.ipynb`
- `preliminary-research/literature-screening.ipynb`
- `data-mining/data-mining.ipynb`
- `surface-and-nanoparticles/nanomaterials-modeling.ipynb`
- `surface/wulffpack_nanoparticle_example.ipynb`

## Repository Structure

```text
.
├── introduction/
├── preliminary-research/
├── data-mining/
├── surface-and-nanoparticles/
├── surface/
├── README.md
└── index.md
```

## How to Use This Repository

1. Open the project in VS Code or JupyterLab.
2. Start with the notebook that matches your research stage.
3. Follow the notebook cells to inspect data sources, run analyses, and reproduce figures or calculations.

## Recommended Environment

The notebooks are intended for a Python scientific stack. A typical setup includes:

- `jupyter`
- `numpy`
- `pandas`
- `matplotlib`
- `scipy`
- `pymatgen`
- `ase`
- `wulffpack`
- `matminer`

If your environment is already configured in the repository, use that configuration first. Otherwise, create a new environment with the packages above before running the notebooks.

## Notes

- Folder names have been normalized to English and lowercase to keep the repository consistent and GitHub-friendly.
- The notebook and data folder names now follow the same naming convention.

## Contributing

When adding new material, keep notebooks grouped by research stage and use clear, descriptive filenames. Prefer short, consistent titles and keep generated files out of version control unless they are part of the reproducible workflow.
