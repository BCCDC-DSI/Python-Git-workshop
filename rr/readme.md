# Research Reproducibility (RR)

**[Page under construction]**

Goodman et al. (2016):
- Methods
- Results
- Inferential

[Five creative ways to promote reproducible science](theory.md)

## Version control
- [Git](../git)

## Reproducible environments

- ***New!!*** [Best practices to RR from the perspectives of a Kaggler](https://www.kaggle.com/code/rtatman/reproducible-research-best-practices-jupytercon)
- R and Python with pven, renv, venv: see [blog from Nov 2023](https://occasionaldivergences.com/posts/rep-env/)
- Python:
    ```
    pip freeze > requirements.txt
    ```
- [Dockerfile](examples/Dockerfile)
- YAML is a human readable language
  - Often used to write configuration files
    ```
    ---
    title: "Reports on alerts"
    author: "Winnie Mo"
    date: "2024-APR-05"
    format: html
    jupyter: python3
    ---  
    ```

## Publishing platforms

- [Dryad](https://datadryad.org/)
  - A community-owned resource
  - Python package ```dryad2dataverse```
- [Open Science framework.io](https://osf.io)

## Coding platforms


<details>

### Free with limits
- [Kaggle](https://www.kaggle.com)
- Digital Ocean
- Google Colab
- [Jupyter.org](https://jupyter.org)
- ...

### Sponsored accounts

#### Option 1: Servers

Replace ```yourusername``` with your's
- https://sfu.syzygy.ca/jupyter/user/yourusername/lab
- https://ubc.syzygy.ca/jupyter/user/yourusername/lab
- [https://jupyterhub.dataspace.copernicus.eu/](https://jupyterhub.dataspace.copernicus.eu/user/r4g.neiss2@gmail.com/lab/workspaces/auto-b)

#### Option 2: Digital Research Alliance 

[Digital Research Alliance; new users require sponsorship](info/DRA.md)

#### Option 3: UBC Advanced Research Computing
[Digital Research Alliance; new users require sponsorship](https://github.com/lisatwyw/nlp-gala/blob/main/info/DRA.md)

</details>




## Recommended practices
- [markdown](https://www.markdownguide.org/basic-syntax/)

## Example workflows
<details>
<summary>R</summary>

  ```
  # Makefile (target: required_files)
  
  manuscript.pdf: manuscript.Rmd simulated_data.csv 
  
  Rscript -e 'rmarkdown::render("manuscript.Rmd")' 
  
  simulated_data.csv: simulate.R
  
  Rscript -e 'source("simulate.R")' 
  ```
Source: [MDPI 2020](https://mdpi-res.com/psych/psych-03-00053/article_deploy/psych-03-00053.pdf)

</details>


## References
- Davos: A Python package ‘‘smuggler’’ for constructing lightweight reproducible notebooks, Paxton C. Fitzpatrick, Jeremy R. Manning [2024 article](https://doi.org/10.1016/j.softx.2023.101614)
- [Reproducible data science - Python](https://valdanchev.github.io/reproducible-data-science-python/notebooks/01_end_to_end_data_science_project.html)

[Return to Home](https://bccdc-dsi.github.io/Python-Git-workshop/)


