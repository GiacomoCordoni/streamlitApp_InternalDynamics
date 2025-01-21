# app.py

import streamlit as st
import pandas as pd
import os
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Cluster Analysis Dashboard", layout="wide")

image_dir       = './Data/'
alternative_dir = './Data/Alternative/'
cluster_groups = [
    'dynyoung', 'dynold', 'p2conc', 'mixed', 'insitu', 'accreted', 
    'inner', 'outer', 'underfilling', 'filling', 'highvesc', 
    'lowvesc', 'rot', 'norot'
]

# Define the sidebar navigation

st.sidebar.image(os.path.join(image_dir, "logoanu.png"), use_container_width=True)
st.title("Internal Dynamics of Multiple Populations in 28 Galactic Globular Clusters: A Wide-Field study with Gaia and the Hubble Space Telescope")

# st.subheader("G. Cordoni et al. ")
container1 = st.container()
col1, col2, col3, col4 = st.columns(4) 

with container1: 
    with col1:
        st.link_button(":blue[Go to article] 📄 ", "https://ui.adsabs.harvard.edu/abs/2024arXiv240902330C/abstract", type="secondary", use_container_width=True)
    with col2:
        st.link_button(":blue[Go to website] 🌏", "https://giacomocordoni.github.io/", type="secondary", use_container_width=True)

st.markdown("""
**G. Cordoni**¹,²  *L. Casagrande*¹,²  *A. P. Milone*³,⁴  *E. Dondoglio*³  *A. Mastrobuono-Battisti*⁴,⁵  *S. Jang*⁶  *A. F. Marino*⁴,⁷  *E. P. Lagioia*⁸  *M. V. Legnardi*³  *T. Ziliotto*³  *M. Tailo*³  *E. Lacchin*³,⁹,¹⁰  *F. Muratore*³  *V. Mehta*¹  
            """)

# 1. Research School of Astronomy and Astrophysics, The Australian National University, Canberra, ACT 2611, Australia   2. ARC Centre of Excellence for All Sky Astrophysics in 3 Dimensions (ASTRO 3D), Australia   3. Dipartimento di Fisica e Astronomia "Galileo Galilei" - Univ. di Padova, Vicolo dell'Osservatorio 3, Padova, IT-35122   4. Istituto Nazionale di Astrofisica - Osservatorio Astronomico di Padova, Vicolo dell'Osservatorio 5, Padova, IT-35122   5. GEPI, Observatoire de Paris, PSL Research University, CNRS, Place Jules Janssen, 92195 Meudon, France   6. Center for Galaxy Evolution Research and Department of Astronomy, Yonsei University, Seoul 03722, Korea   7. Istituto Nazionale di Astrofisica - Osservatorio Astrofisico di Arcetri, Largo Enrico Fermi, 5, Firenze, IT-50125   8. South-Western Institute for Astronomy Research, Yunnan University, Kunming, 650500, P.R. China   9. Dipartimento di Fisica e Astronomia Augusto Righi, Univ. degli Studi di Bologna, Via Gobetti 93/2, 40129 Bologna, Italy   10. Osservatorio di Astrofisica e Scienza dello Spazio di Bologna, Via Gobetti 93/3, 40129 Bologna, Italy   11. Institut für Theoretische Astrophysik, ZAH, Universität Heidelberg, Albert-Ueberle-Straße 2, D-69120, Heidelberg, Germany   12. INFN - Padova, Via Marzolo 8, I–35131 Padova, Italy  

st.sidebar.title("Pages")
page = st.sidebar.radio("Go to", ["Home", "Global profiles", "Cluster groups profiles", 
                                  "Alternative global profiles", "Individual clusters profiles", "Statistical tests"])

# ===========================
# Page 1: Home
# ===========================
if page == "Home":
    # st.title("Cluster Analysis Dashboard")
    st.markdown("""                
    ## Abstract


**Important: the dashboard is still being updated** We present a detailed analysis of the internal dynamics of multiple stellar populations (MPs) in 28 Galactic Globular Clusters (GCs) using astro-photometric catalogs from ground-based observations, Gaia, and the Hubble Space Telescope (HST). Exploiting Chromosome Maps (ChMs) and the ( $C_\mathrm{UBI}$) photometric index, we identified first-population (1P) and second-population (2P) stars among RGB stars and studied their internal dynamics with Gaia DR3 and HST proper motions. Our results show that while 1P stars display isotropic motion across the entire cluster field, 2P stars become increasingly radially anisotropic in the outer regions. We analyzed the dynamical profiles of clusters with different dynamical and structural properties. In dynamically young and non-relaxed clusters, we observe significant dynamical differences, particularly beyond the tidal radius. In these regions, 1P stars shift from isotropic to slightly tangentially anisotropic motion, while 2P stars become increasingly radially anisotropic. We also find that clusters with orbits closer to the Galactic center display greater dynamical differences between 1P and 2P stars compared to those with larger peri-Galactic radii. These findings suggest that 2P stars likely formed in a more centrally concentrated environment, with the interactions between the Galaxy and MPs playing a crucial role in shaping these dynamics.

## Introduction

Research using Hubble Space Telescope (HST) images has revealed that photometric diagrams of nearly all globular clusters (GCs) show two primary groups: first-population (1P) and second-population (2P) stars. These groups exhibit specific chemical compositions, with 2P stars being enriched in Sodium, Nitrogen, and Helium, and depleted in Carbon and Oxygen. Despite several models proposed to explain the formation of MPs, none can simultaneously fit the numerous observational constraints. Some scenarios predict that 2P stars formed from the ejecta of short-lived massive 1P stars. Since the expelled gas accumulated toward the cluster center, 2P stars would dominate the composition of the central cluster regions. Alternatively, the chemical composition of 2P stars could result from the accretion of chemically enriched material emitted from 1P stars in binary configurations.

While some clusters exhibit a more centrally concentrated 2P population, numerous examples show that 1P and 2P stars are spatially mixed, and even clusters with a more centrally concentrated 1P are observed. Recent studies suggest that the extent of this mixing between 1P and 2P stars may correlate with the dynamical age of the cluster, indicating that older clusters tend to show more complete mixing of MPs. Nonetheless, despite accumulating observational constraints, a comprehensive picture of how these populations interact dynamically over time remains elusive.

In recent years, a promising new path has emerged: the study of the internal kinematics of cluster stars. This approach is crucial for uncovering the physical processes behind the formation of multiple populations. Specifically, \( N \)-body simulations indicate that the dynamical evolution of 2P stars formed in different environments should differ significantly from that of more spatially extended 1P stars. Such differences may still be detectable in present-day GC kinematics, provided the populations are not completely relaxed. In the case of more centrally concentrated 2P stars, the distinct initial configurations could lead to different anisotropy, especially in the outer regions where the relaxation time is longer. Additionally, studies have shown how the dynamical differences between 1P and 2P stars might be connected with the dynamical state of the clusters, their interaction with the Milky Way, and their overall properties (e.g., escape velocity).

Over the past decade, numerous studies have analyzed the spatial distribution and internal kinematics of MPs in various GCs, using HST photometry and proper motions, MUSE/APOGEE line-of-sight (LoS) velocities, ground-based photometry coupled with Gaia proper motions, or a combination of these methods. These works have presented the first evidence of significant dynamical differences between 1P and 2P stars in some GCs, aligning qualitatively with \( N \)-body simulations' results. However, the limited number of analyzed clusters and the small field of view of MUSE and HST have prevented a complete characterization of the phenomenon.

More recently, large-scale analyses have been conducted to investigate the internal kinematics of MPs across a broader sample of clusters. These studies have revealed diverse dynamical behaviors among different GCs, highlighting the influence of both internal cluster properties and external Galactic interactions on the dynamical evolution of MPs.

In this work, we aim to overcome the limitations of previous studies by investigating the internal dynamics of MPs in a sample of 28 GCs, combining photometric information from HST, ground-based telescopes, Gaia DR3 proper motions, and spectro-photometric data. By doing this, we improve the identification of 1P and 2P stars using Chromosome Maps and extend the analyzed field of view from the innermost cluster regions to their outskirts. This comprehensive approach allows for a more detailed understanding of the dynamical interactions and evolutionary processes shaping multiple stellar populations in globular clusters.

## Dataset

To investigate the internal dynamics of MPs in Galactic GCs over a wide field of view, we combined data from multiple sources:

- **Hubble Space Telescope (HST) Photometry**: High-resolution images and photometric data from HST \citep{milone2017, nardiello2018}.
- **Ground-Based UBVI Photometry**: Comprehensive photometric surveys from ground-based telescopes \citep{stetson2019, jang2022}.
- **Gaia DR3 Proper Motions**: Accurate astrometric measurements from Gaia Data Release 3 \citep{gaiadr3}, supplemented by synthetic photometry from Gaia XP spectra \citep{mehta2024} for select clusters.
- **Astro-Photometric Catalogs**: Integrated datasets providing multi-band photometry and proper motion information for RGB stars in 28 GCs.

The final sample consists of 28 GCs selected based on the availability and reliability of multi-wavelength photometric data and proper motion measurements. This extensive dataset allows for a robust identification of MPs across a wide spatial range, from the core to the outskirts of each cluster.

### Identification of Multiple Populations

- **Chromosome Maps (ChMs)**: Utilized to separate 1P and 2P stars based on their photometric properties. ChMs plot the verticalized color indices (\( \Delta_\mathrm{BI} \) vs. \( \Delta_\mathrm{C_{UBI}} \)) to distinguish between different populations.
- **\( C_\mathrm{UBI} \) Photometric Index**: A color index designed to maximize the separation between 1P and 2P stars, enhancing the identification accuracy.
- **Selection Process**: Employed Gaussian Mixture Models (GMM) to fit the distribution of stars in the ChMs and classify them into 1P and 2P populations based on their positions in these diagrams.

## Methodology

### Proper Motion Analysis

We utilized proper motion data from Gaia DR3 and HST to study the internal dynamics of 1P and 2P stars within each GC. The analysis involved the following steps:

1. **Coordinate Transformation**:
   - Converted celestial coordinates and proper motion components (\( \alpha, \delta, \mu_\alpha, \mu_\delta \)) into a Cartesian reference frame (\( x, y, \mu_x, \mu_y \)) using orthographic projection.
   - Transformed proper motions into radial (\( \mu_R \)) and tangential (\( \mu_T \)) components relative to the cluster center.

2. **Velocity Dispersion and Anisotropy**:
   - Calculated the mean and dispersion of radial and tangential velocities for both 1P and 2P stars.
   - Derived anisotropy profiles (\( \beta = \frac{\sigma_T^2}{\sigma_R^2} - 1 \)) to quantify the difference between radial and tangential dispersions.

3. **Global Profiles**:
   - Combined data from all 28 GCs to create global dynamical profiles.
   - Normalized radial distances to the half-light radius (\( R_h \)) and velocity dispersions to the central dispersion values to ensure consistency across clusters.
   - Applied the LOESS algorithm to derive smoothed global profiles and assess the overall trends in the dynamics of 1P and 2P stars.

### Statistical Significance

To ensure the reliability of the observed dynamical differences between 1P and 2P stars, we performed the following statistical analyses:

- **Bootstrapping**: Generated 1,000 bootstrapped samples to estimate uncertainties in the LOESS fits.
- **Significance Testing**: Compared the observed differences in anisotropy profiles against the bootstrapped distributions to determine the statistical significance of these differences.

## Results

### Individual Cluster Dynamics

Analysis of individual clusters revealed distinct dynamical behaviors between 1P and 2P stars:

- **1P Stars**: Generally exhibit isotropic motion within clusters, with some clusters showing slight tangential anisotropy in the outer regions.
- **2P Stars**: Display increasingly radially anisotropic motion in the outskirts of clusters, indicating a stronger influence of their formation environment on their kinematics.

These patterns are consistent across several clusters, aligning with predictions from \( N \)-body simulations that suggest 2P stars formed in more centrally concentrated environments.

### Global Dynamical Profiles

By combining data from all 28 GCs, we derived global dynamical profiles that encapsulate the average behavior of 1P and 2P stars across the sample:

- **Radial Dispersion**: No significant differences between 1P and 2P stars, indicating similar radial velocity dispersions.
- **Tangential Dispersion**: 2P stars exhibit lower tangential dispersion compared to 1P stars, especially beyond \( 1-2 R_h \).
- **Anisotropy**: The global anisotropy profiles show that 1P stars transition from isotropic to slightly tangentially anisotropic motion in the outer regions, while 2P stars become increasingly radially anisotropic.

### Influence of Cluster Properties

The dynamical differences between 1P and 2P stars are influenced by several cluster properties:

1. **Dynamical Age**:
   - **Young Clusters**: Exhibit significant dynamical differences between 1P and 2P stars, particularly beyond the tidal radius.
   - **Older Clusters**: Show reduced dynamical differences due to enhanced spatial and dynamical mixing over time.

2. **Galactic Proximity**:
   - **Inner Clusters (Closer to Galactic Center)**: Display greater dynamical differences between populations, suggesting stronger Galactic tidal interactions.
   - **Outer Clusters (Farther from Galactic Center)**: Show more balanced dynamical profiles with less pronounced differences between 1P and 2P stars.

3. **Escape Velocity (\( v_\mathrm{esc} \))**:
   - Clusters with higher escape velocities tend to retain 2P stars more effectively, maintaining their radially anisotropic motion in the outskirts.

4. **Tidal Filling Factor**:
   - **Tidally Underfilling Clusters**: 1P stars exhibit isotropic to tangentially anisotropic motion, while 2P stars remain radially anisotropic.
   - **Tidally Filling Clusters**: Show different dynamical patterns, potentially due to varying degrees of tidal stripping and interaction with the Galactic potential.

### Formation Implications

The observed dynamical differences support the hypothesis that 2P stars formed in more centrally concentrated environments. The increasing radial anisotropy of 2P stars in the outer regions suggests that Galactic interactions and the initial conditions of star formation within clusters play crucial roles in shaping the kinematics of multiple populations.

## Conclusion

This work provides a comprehensive picture of the dynamical differences between multiple populations in Galactic Globular Clusters. By analyzing a large sample of 28 GCs using combined datasets from HST, Gaia, and ground-based observations, we have identified and studied the internal dynamics of first-population (1P) and second-population (2P) stars across a wide field of view.

### Key Insights:

- **Isotropic vs. Anisotropic Motion**: 1P stars generally exhibit isotropic motion within clusters, while 2P stars become increasingly radially anisotropic in the outer regions.
- **Dynamical Age Influence**: Younger, non-relaxed clusters show more significant dynamical differences between populations, highlighting the role of cluster evolution in shaping MP dynamics.
- **Galactic Tidal Interactions**: Clusters closer to the Galactic center display greater dynamical differences, indicating that external tidal forces significantly influence the internal kinematics of MPs.
- **Formation Environments**: The distinct dynamical profiles of 2P stars support the notion that they formed in more centrally concentrated environments, aligning with predictions from \( N \)-body simulations.

Overall, the analysis advances the understanding of multiple populations in globular clusters by providing robust evidence of dynamical distinctions between 1P and 2P stars across a diverse sample of clusters. These insights contribute to refining formation and evolutionary models of globular clusters, offering valuable constraints for future \( N \)-body simulations and theoretical studies.
    """)

# ===========================
# Page 2: Global Profiles Results
# ===========================
elif page == "Global profiles":
    st.title("Global Profiles Results")

    st.markdown("""
    ## Overview of Global Profiles
    ### Derivation of Global Profiles Using the LOESS Algorithm

    To analyze the dynamical differences between multiple populations (1P and 2P stars) across all clusters, we employed the **LOESS (Locally-Weighted Regression)** algorithm as described by Cappellari et al. (2013).

    #### **How Global Profiles Are Derived**

    1. **Individual Cluster Profiles**:
        - Each cluster in our sample of **28 globular clusters** has its own set of dynamical profiles based on the motions of 1P and 2P stars.
        - These profiles include measurements of radial and tangential velocity dispersions, as well as anisotropy parameters.

    2. **Applying LOESS Smoothing**:
        - The LOESS algorithm smooths these individual profiles by fitting local regressions around each data point.
        - For each point in the global profile, LOESS assigns a **weight** between **0 and 1**, determining the influence of nearby data points on the fit.
        - This weighting ensures that data points closer to the target point have a more significant impact on the smoothing process.
    """)
    # Placeholder for the global profiles figure
    # st.write("#### Combined LOESS Weight Distributions")
    # st.pyplot()  # Empty plot for now
    # Construct filenames based on the selected group
    fig1_filename = f'HSTGaiaAll_figStackedDynamics_wSig.png'
    fig2_filename = f'Cluster_weigths_HSTGaiaAll.png'

    # Construct full paths
    fig1_path = os.path.join(image_dir, fig1_filename)
    fig2_path = os.path.join(image_dir, fig2_filename)

    # Check if files exist
    fig1_exists = os.path.isfile(fig1_path)
    fig2_exists = os.path.isfile(fig2_path)

    # Display images on separate rows spanning the whole page width
    if fig1_exists:
        st.write("##### Figure 1: Cluster Fractions Heatmap")
        st.markdown("""
### Description of Figures

Before presenting the results of the different tests, we first provide the **global profiles** obtained from the stacked dataset, which includes all 1P and 2P stars from all clusters. To combine the individual clusters’ datasets, we adopted the following normalization:

1. **Radial Coordinate Normalization**:  
   - The radial coordinate is normalized to the cluster’s half-light radius (\(R_h\)).

2. **Proper Motion Normalization**:  
   - Proper motions are normalized to the central dispersion, determined in *Libralato et al. (2023)* when available, or *Vasiliev & Baumgardt (2021)*.

3. **Tangential Profile subtraction**:  
   - The cluster’s tangential profile (a proxy for rotation) is subtracted from individual tangential proper motions.  
   - This subtraction prevents an artificially increased tangential dispersion caused by the combination of differently rotating and non-rotating clusters.  


### Results

- **Radial and Tangential Dispersion Profiles**: Shown in the first two columns for both 1P and 2P stars.  
- **Profile Comparisons**: Displayed in the third column, highlighting differences between the radial and tangential profiles of 1P and 2P stars.  
- **Statistical Significance of Differences**: Shown in the rightmost column, where differences are color-coded by their statistical significance.

---
                    """)
        image1 = Image.open(fig1_path)
        st.image(image1, use_container_width=True)
    else:
        st.warning(f"Image not found: {fig1_filename}")

    if fig2_exists:
        st.write("##### Figure 2: LOESS Weight Distribution")
        st.markdown("""
### Contribution of Individual Clusters to Global Profiles

To better understand the contribution of each cluster to the global profiles, we computed a **weight heatmap** for each test. These heatmaps illustrate the relative weight of each cluster in each bin. The weight for a cluster in a given bin is calculated as:  
\[
\text{Weight} = \frac{\text{Number of Stars from Cluster X in Bin Y}}{\text{Total Number of Stars in Bin Y}}
\]

Weights range from:
- **0**: No stars from cluster X in bin Y.
- **1**: All stars in bin Y belong to cluster X.

In the heatmaps:
- **Darker colors** indicate larger weights.  
- **White-greyish colors** represent lower weights.

These visuals provide insights into how individual clusters influence the global profiles, highlighting the contribution patterns across different datasets.                    
""")
        image2 = Image.open(fig2_path)
        st.image(image2, use_container_width=True)
    else:
        st.warning(f"Image not found: {fig2_filename}")

# ===========================
# Page 3: Group Profiles from stacked individual datasets
# ===========================
elif page == "Cluster groups profiles":
    st.title("Group Profiles Comparison")

    st.markdown("""
### Grouping Clusters Based on Evolutionary Properties

To explore how dynamical differences between multiple populations (1P and 2P stars) depend on the evolutionary state of clusters, we divided our sample of **28 clusters** into distinct groups based on various internal and external factors. Below is an overview of the criteria and classifications used:

| **Criterion**                     | **Dynamical Ages**                                                                                                                                                        | **Tidal Filling Factor**                                                                                                                                                                                                                                               | **Spatial Mixing of MPs**                                                                                                                                          | **Tidal Interaction with Milky Way**                                                                                                                                                        | **Clusters' Origin**                                                                                                                                                | **Escape Velocity (\(v_{\text{esc}}\))**                                                                                                                                              |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Definition**                    | Ratio between cluster age and half-mass relaxation time.[^1]                                                                                                            | $$\mathcal{R} = \frac{R_h}{R_J}$$ where \(R_h\) is the half-light radius and \(R_J\) is the Jacobi radius.[^2]                                                                                                                                                               | Degree to which 1P and 2P stars are spatially mixed.[^3]                                                                                                                 | Interaction strength based on peri-Galactic radius.[^4]                                                                                                                                              | Whether clusters formed **in situ** or were **accreted**.[^5]                                                                                                         | The escape velocity from the cluster.[^6]                                                                                                                                                         |
| **Reference**                     | [Libralato et al. 2022](https://ui.adsabs.harvard.edu/abs/2022...)                                                                                                      | [Baumgardt et al. 2010; Balbinot et al. 2018](https://ui.adsabs.harvard.edu/abs/2010...)                                                                                                                                                              | [Leitinger et al. 2023; Jang et al. (submitted)](#)                                                                                                                  | [Milone et al. 2020; Libralato et al. 2023](https://ui.adsabs.harvard.edu/abs/2020...)                                                                                                 | [Massari et al. 2019](https://ui.adsabs.harvard.edu/abs/2019...)                                                                                                 | [Baumgardt et al. 2018; Mastrobuono-Battisti et al. 2021](https://ui.adsabs.harvard.edu/abs/2018...)                                                                                             |
| **Classification**                | - **Young**  
- **Intermediate-Old**                                                                                                                                                 | - **Isolated Regime (Tidally Underfilling)**: \(\mathcal{R} < 0.05\)  
- **Tidal Regime (Tidally Filling)**: \(\mathcal{R} > 0.05\)                                                                                                                              | - **Mixed**  
- **P2 Concentrated**                                                                                                                                                | - **Inner Clusters**: \(R_{\text{peri}} < 3.5\,\text{kpc}\)  
- **Outer Clusters**: \(R_{\text{peri}} \geq 3.5\,\text{kpc}\)                                                               | - **In-situ**  
- **Accreted**                                                                                                                              | - **Low Escape Velocity**: \(v_{\text{esc}} < 20\,\text{km/s}\)  
- **High Escape Velocity**: \(v_{\text{esc}} \geq 20\,\text{km/s}\)                                                       |

---

### ⚠️ **Important Notes**
- **Overlapping Groups**:
  - Different group classifications can overlap since some cluster properties are interdependent.
  - *Example*: **Spatial Mixing of MPs** is connected with the **Cluster Dynamical Age** ([Dalessandro et al. 2019](https://ui.adsabs.harvard.edu/abs/2019...), [Leitinger et al. 2023](#)).
  
- **Internal Rotation**:
  - Clusters are also categorized based on their internal rotation, but for clarity, these results are not shown in the main comparison figure.
  - Differences between 1P and 2P anisotropy profiles for each group, along with their statistical significance, are included in **Figure X** of the report.

---

[^1]: Clusters with \(\mathcal{R} < 0.05\) are considered in the *isolated regime* or tidally underfilling, while clusters with \(\mathcal{R} > 0.05\) are in the *tidal regime* or tidally filling.
[^2]: Clusters with \(R_{\text{peri}} < 3.5\,\text{kpc}\) are categorized as *inner clusters*, and those with \(R_{\text{peri}} \geq 3.5\,\text{kpc}\) as *outer clusters*.
[^3]: Escape velocity (\(v_{\text{esc}}\)) categories are defined as follows:
- **Low Escape Velocity**: \(v_{\text{esc}} < 20\,\text{km/s}\)
- **High Escape Velocity**: \(v_{\text{esc}} \geq 20\,\text{km/s}\)

---
                """)


    # Sidebar for group selection
    options = ['Comparison'] + cluster_groups
    selected_group = st.sidebar.selectbox(
        "Select a Group",
        options, 
        index=0  # Sets the default selected option to the first item
    )


    if selected_group == 'Comparison':
        st.markdown(f"### Comparison between all groups")

        # Construct filenames based on the selected group
        fig1_filename = f'HSTGaiaAll_{selected_group}_figStackedDynamics_wSig.png'
        fig2_filename = f'Cluster_weigths_HSTGaiaAll_{selected_group}.png'

        # Construct full paths
        fig1_path = os.path.join(image_dir, 'figComparison_all_0.png')
        fig2_path = os.path.join(image_dir, 'figComparison_all_1.png')
        fig3_path = os.path.join(image_dir, 'figSignificanceBeta_vall.png')

        # Check if files exist
        fig1_exists = os.path.isfile(fig1_path)
        fig2_exists = os.path.isfile(fig2_path)
        fig3_exists = os.path.isfile(fig3_path)

        # Display images on separate rows spanning the whole page width
        if fig1_exists:
            st.write("##### Figure 1: Global profiles comparison")
            image1 = Image.open(fig1_path)
            st.image(image1, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig1_filename}")

        if fig2_exists:
            image2 = Image.open(fig2_path)
            st.image(image2, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig2_filename}")
        
        if fig3_exists:
            st.write("##### Figure 2: Global profiles difference significance")
            image3 = Image.open(fig3_path)
            st.image(image3, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig2_filename}")
    
    else:
        st.markdown(f"### Group: {selected_group}")

        # Option selector for static vs. Plotly plots
        # plot_option = st.radio("Select Plot Type", ["Static Plots", "Interactive Plotly Plots"])

        # if plot_option == "Static Plots":
            # st.write("#### Static Figures")

        # Define the directory where images are stored
        # Construct filenames based on the selected group
        fig1_filename = f'HSTGaiaAll_{selected_group}_figStackedDynamics_wSig.png'
        fig2_filename = f'Cluster_weigths_HSTGaiaAll_{selected_group}.png'
        # Construct full paths
        fig1_path = os.path.join(image_dir, fig1_filename)
        fig2_path = os.path.join(image_dir, fig2_filename)
        # Check if files exist
        fig1_exists = os.path.isfile(fig1_path)
        fig2_exists = os.path.isfile(fig2_path)
        # Display images on separate rows spanning the whole page width
        if fig1_exists:
            st.write("##### Figure 1: Cluster Fractions Heatmap")
            image1 = Image.open(fig1_path)
            st.image(image1, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig1_filename}")

        if fig2_exists:
            st.write("##### Figure 2: LOESS Weight Distribution")
            image2 = Image.open(fig2_path)
            st.image(image2, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig2_filename}")

# ===========================
# Page 4: Group Profiles from stacked profiles
# ===========================
elif page == "Alternative global profiles":
    st.title("Alternative Global Profiles Comparison")

    st.markdown("""
### Grouping Clusters Based on cluster properties
1. **Combining Data from All Clusters**:
    - By applying LOESS to the combined dynamical profiles of all clusters, we derive **global profiles** that represent the average dynamical behavior of 1P and 2P stars across the entire sample.
    - This approach mitigates biases that might arise from clusters with a disproportionately large number of stars or unique dynamical properties.

#### **Understanding Weight Distribution**

- **Weight Assignment**:
    - Each data point in the global profiles receives a weight \( w \) such that \( 0 \leq w \leq 1 \).
    - A higher weight indicates a stronger influence of that data point on the LOESS fit, while a lower weight suggests minimal contribution.

- **Weight Distribution Analysis**:
    - To assess how each cluster contributes to the global profiles, we analyzed the distribution of these weights.
    - **Box Plots**:
        - **Median Weight**: Represents the central tendency of the weights for each cluster.
        - **Dispersion Range**: Indicates the variability of weights within each cluster, showcasing how consistently a cluster contributes across different regions of the profile.
        - **Insights from Box Plots**:
            - **Significant Contributors**: Most clusters exhibit median weights close to **1**, indicating a substantial and consistent contribution to the global profiles.
            - **Minimal Contributors**: A few clusters display median weights near **0**, suggesting that their influence on the global profiles is negligible.
            - **Balanced Influence**: The overall distribution ensures that the global profiles are not unduly dominated by a few massive clusters, promoting a more representative average of the entire sample.

---

### 📊 **Visual Representation of Weight Distributions**
To visualize how each cluster influences the global dynamical profiles, we utilized **weight heatmaps** and **box plots**:

**Box Plots of Weight Distributions**:
    - **Components**:
        - **Median**: Central value of the weight distribution for each cluster.
        - **Interquartile Range (IQR)**: Highlights the middle 50% of the weight values, indicating consistency in contribution.
    - **Insights**:
        - Clusters with higher median weights and narrower IQRs
                """)

    # Sidebar for group selection
    options2 = ['All clusters', 'Groups comparison', 'young', 'intermedold', 'p2conc', 'mixed', 'insitu', 'accreted',  'inner', 'outer', 'underfilling', 'filling', 'high', 'low', 'rot', 'norot'] # cluster_groups.insert(0, 'Comparison').insert(0, 'All clusters')    
    selected_group = st.sidebar.selectbox(
        "Select a Group",
        options2, 
        index=0
    )

    if selected_group == 'All clusters':
        fig1_path =  os.path.join(alternative_dir, 'figStackedDynamics_wSig_wweights.png')
        fig2_path =  os.path.join(alternative_dir, 'LOESS_weights_boxplot.png')
                # Check if files exist
        fig1_exists = os.path.isfile(fig1_path)
        fig2_exists = os.path.isfile(fig2_path)
        # Display images on separate rows spanning the whole page width
        if fig1_exists:
            st.write("##### Figure 1: Global profiles comparison")
            image1 = Image.open(fig1_path)
            st.image(image1, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig1_path}")

        if fig2_exists:
            image2 = Image.open(fig2_path)
            st.image(image2, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig2_path}")

    elif selected_group == 'Groups comparison':
        st.markdown(f"### Comparison between all groups")

        # Construct full paths
        fig1_path = os.path.join(alternative_dir, 'figComparison_all_0.png')
        fig2_path = os.path.join(alternative_dir, 'figComparison_all_1.png')
        fig3_path = os.path.join(alternative_dir, 'figSignificanceBeta_vall.png')

        # Check if files exist
        fig1_exists = os.path.isfile(fig1_path)
        fig2_exists = os.path.isfile(fig2_path)
        fig3_exists = os.path.isfile(fig3_path)

        # Display images on separate rows spanning the whole page width
        if fig1_exists:
            st.write("##### Figure 1: Global profiles comparison")
            image1 = Image.open(fig1_path)
            st.image(image1, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig1_path}")

        if fig2_exists:
            image2 = Image.open(fig2_path)
            st.image(image2, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig2_path}")
        
        if fig3_exists:
            st.write("##### Figure 2: Global profiles difference significance")
            image3 = Image.open(fig3_path)
            st.image(image3, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig3_path}")
    
    else:
        st.markdown(f"### Group: {selected_group}")
        # Define the directory where images are stored
        fig1_path = os.path.join(alternative_dir, 'figSignificance_%s.png' %selected_group)
        fig1_exists = os.path.isfile(fig1_path)
        if fig1_exists:
            st.write("##### Figure 1: Group Global profiles significance")
            image1 = Image.open(fig1_path)
            st.image(image1, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig1_path}")

# ===========================
# Page : Individual ckusters' profiles 
# ===========================
elif page == 'Individual clusters profiles':
        # Sidebar for group selection
    options3 = ['Radial mean profile', 'Tangential mean profile', 'Radial dispersion profile', 
    'Tangential dispersion profile', 'Anisotropy profile']
    selected_group = st.sidebar.selectbox(
        "Select a Group",
        options3, 
        index=0
    )
    fignames = {
        'Radial mean profile': 'figRadMed_wHST.png',
        'Tangential mean profile': 'figTanMed_wHST.png',
        'Radial dispersion profile': 'figRadDis_wHST.png',
        'Tangential dispersion profile': 'figTanDis_wHST.png',
        'Anisotropy profile': 'figBeta_wHST.png'        
    }

    fig1_path =  os.path.join(image_dir, fignames[selected_group])
                # Check if files exist
    fig1_exists = os.path.isfile(fig1_path)
        # Display images on separate rows spanning the whole page width
    if fig1_exists:
        st.write("##### %s" %selected_group)
        image1 = Image.open(fig1_path)
        st.image(image1, use_container_width=True)
    else:
        st.warning(f"Image not found: {fig1_path}")

elif page == "Statistical tests":
    st.title("Statistical tests")

    st.markdown("""

## Quantification of Cluster Influence

To ensure that no specific clusters unduly dominate the global profiles, we conducted a series of tests by recomputing the global profiles using different subsets of the data:

- **Test 1**: Recomputed the global profiles by including only the six most populated clusters (NGC 0104, NGC 2808, NGC 5272, NGC 6205, NGC 5904, and NGC 7089).
  
- **Test 2**: Repeated the analysis excluding these six clusters to assess their impact on the global profiles.
  
- **Test 3**: Resampled the clusters to include approximately the same number of stars per cluster (50 stars, or the total available stars for clusters with fewer than 50). This resampling was repeated 1,000 times, resulting in 1,000 global profiles to account for random fluctuations.

These tests confirmed that the global profiles remain consistent regardless of the inclusion or exclusion of specific clusters, validating the robustness of our methodological approach.

---
                """)

    # Sidebar for group selection
    options4 = ['Only 6 most populated clusters', 'Excluding 6 most populated clusters', 'Equalized number of stars']
    selected_group = st.sidebar.selectbox(
        "Select a Group",
        options4, 
        index=0
    )
    groups_names = {
        'Only 6 most populated clusters':'massive', 
        'Excluding 6 most populated clusters':'intermediate', 
        'Equalized number of stars':'equalized'
    }

    if selected_group == 'Only 6 most populated clusters':         
        fig1_path =  os.path.join(image_dir, 'HSTGaiaAll_%s_figStackedDynamics_wSig.png' %groups_names[selected_group])
        fig2_path =  os.path.join(image_dir, 'Cluster_weigths_HSTGaiaAll_%s.png' %groups_names[selected_group])
                # Check if files exist
        fig1_exists = os.path.isfile(fig1_path)
        fig2_exists = os.path.isfile(fig2_path)
        # Display images on separate rows spanning the whole page width
        if fig1_exists:
            st.markdown("""
                        ##### Global profiles 
                        The global profiles have been computed in the same way described in the paper, but including only the 6 most populated clusters: NGC0104, NGC2808, NGC5272, NGC5904, NGC6205 and NGC7089
                    """)
            image1 = Image.open(fig1_path)
            st.image(image1, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig1_path}")

        if fig2_exists:
            st.write('Global profile weight heatmap')
            image2 = Image.open(fig2_path)
            st.image(image2, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig2_path}")

    elif selected_group == 'Excluding 6 most populated clusters':         
        fig1_path =  os.path.join(image_dir, 'HSTGaiaAll_%s_figStackedDynamics_wSig.png' %groups_names[selected_group])
        fig2_path =  os.path.join(image_dir, 'Cluster_weigths_HSTGaiaAll_%s.png' %groups_names[selected_group])
                # Check if files exist
        fig1_exists = os.path.isfile(fig1_path)
        fig2_exists = os.path.isfile(fig2_path)
        # Display images on separate rows spanning the whole page width
        if fig1_exists:
            st.markdown("""
                        ##### Global profiles 
                        The global profiles have been computed in the same way described in the paper, but excluding the 6 most populated clusters. 
                    """)
            image1 = Image.open(fig1_path)
            st.image(image1, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig1_path}")

        if fig2_exists:
            st.write('Global profile weight heatmap')
            image2 = Image.open(fig2_path)
            st.image(image2, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig2_path}")
    
    elif selected_group == 'Equalized number of stars':         
        fig1_path =  os.path.join(image_dir, 'HSTGaiaAll_1000equalized_figStackedDynamics_wSig_perc.png')
        fig2_path =  os.path.join(image_dir, 'Cluster_weigths_HSTGaiaAll_%s.png' %groups_names[selected_group])
                # Check if files exist
        fig1_exists = os.path.isfile(fig1_path)
        fig2_exists = os.path.isfile(fig2_path)
        # Display images on separate rows spanning the whole page width
        if fig1_exists:
            st.markdown("""
                        ##### Global profiles 
                        The global profiles have been computed in the same way described in the paper, but from datasets created including the same number of stars per clusters. Hence, by construction, no cluster biases the global profiles. We repeated the sampling 1000 times, and whos the distribution of the resulting LOESS globla profiles. Darker colors indicate the 50th percentiles (red, blue and green for 1P, 2P and 1P-2P differences), while lighter colors indicate percentiles close to 0 or 100. 
                        The weights heatmap refers to a single realization, with the purpose of whosin gthat indeed the weight distribution is homogeneous and not biased by few clusters.
                    """)
            image1 = Image.open(fig1_path)
            st.image(image1, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig1_path}")

        if fig2_exists:
            st.write('Global profile weight heatmap')
            image2 = Image.open(fig2_path)
            st.image(image2, use_container_width=True)
        else:
            st.warning(f"Image not found: {fig2_path}")

# ===========================
# Run the App
# ===========================
# To run the app, navigate to your_project directory in the terminal and execute:
# streamlit run app.py
