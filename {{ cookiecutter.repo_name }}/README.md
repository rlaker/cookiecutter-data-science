{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Installation
------------

Just run `make environment` to create the conda environment, or `conda env create -f environment.yaml` if you don't have make.

Adding dependencies
------------

It is best practice to write the new dependency in the `environment.yaml` or `requirements.txt` file and then run
    
    conda env update -f environment.yaml

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   ├── exploratory    <- Quick exploration of data
    |   └── reports        <- More mature documents that create a repeated output
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   ├── understand     <- Finalised analysis pieces on a certain area
    │   ├── presentations  <- Presentation files with the date at the start, e.g. 24_02_06_title
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── environment.yaml   <- Conda environment file for reproducing the analysis environment.
    ├── requirements.txt   <- Installs the local package in -e mode and any non-conda packages
    │
    ├── pyproject.toml     <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   └── mypkg/
    │       __init__.py    <- Makes src a Python module
    │       │
    │       ├── data       <- Scripts to download or generate data
    │       │   └── make_dataset.py
    │       │
    │       ├── features   <- Scripts to turn raw data into features for modeling
    │       │   └── build_features.py
    │       │
    │       ├── models     <- Scripts to train models and then use trained models to make
    │       │   │                 predictions
    │       │   ├── predict_model.py
    │       │   └── train_model.py
    │       │
    │       └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │           └── visualize.py
    │
    └── docs               <- Documentation from either make docs_md or docs_html


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
