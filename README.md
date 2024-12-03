# Streamlit Internal Dynamics

## Overview

**Streamlit Internal Dynamics** is an interactive application designed to analyze and visualize the internal dynamics of multiple stellar populations within 28 Galactic Globular Clusters (GCs). Leveraging high-quality astro-photometric data from ground-based observations, Gaia DR3, and the Hubble Space Telescope (HST), this app provides insights into the kinematic behaviors of first-population (1P) and second-population (2P) stars across various regions of each cluster.

## Features

- **Interactive Visualizations**: Explore velocity dispersion and anisotropy profiles of 1P and 2P stars.
- **Comprehensive Data Coverage**: Analyze data from the core to the outskirts of 28 Galactic GCs.
- **Dynamic Filtering**: Select clusters based on properties like dynamical age, Galactic proximity, and more.
- **Statistical Insights**: Understand the significance of observed dynamical differences between populations.

## Dataset

The application utilizes a combination of datasets to provide a robust analysis of multiple stellar populations:

- **Hubble Space Telescope (HST) Photometry**: High-resolution images and photometric data.
- **Ground-Based UBVI Photometry**: Comprehensive surveys providing multi-band photometric information.
- **Gaia DR3 Proper Motions**: Accurate astrometric measurements for proper motion analysis.
- **Gaia XP Synthetic Photometry**: Enhanced photometric data derived from Gaia's low-resolution spectra for select clusters.

All necessary figures and data files required for plotting are organized within the `Data/` directory.

## How to cite
```bibtex
@ARTICLE{2024arXiv240902330C,
       author = {{Cordoni}, Giacomo and {Casagrande}, Luca and {Milone}, Antonino and {Dondoglio}, Emanuele and {Mastrobuono-Battisti}, Alessandra and {Jang}, Sohee and {Marino}, Anna and {Lagioia}, Edoardo and {Vittoria Legnardi}, Maria and {Ziliotto}, Tuila and {Muratore}, Fabrizio and {Mehta}, Vernica and {Lacchin}, Elena and {Tailo}, Marco},
        title = "{Internal Dynamics of Multiple Populations in 28 Galactic Globular Clusters: A Wide-Field study with Gaia and the Hubble Space Telescope}",
      journal = {arXiv e-prints},
     keywords = {Astrophysics - Astrophysics of Galaxies, Astrophysics - Solar and Stellar Astrophysics},
         year = 2024,
        month = sep,
          eid = {arXiv:2409.02330},
        pages = {arXiv:2409.02330},
          doi = {10.48550/arXiv.2409.02330},
archivePrefix = {arXiv},
       eprint = {2409.02330},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2024arXiv240902330C},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```