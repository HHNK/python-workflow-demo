# Python workflow demo
Standaard setup voor python-projects bij HHNK.

# IDE
`Visual Studio Code` `

# Env management
Meerdere opties;
- `conda`: 
    - Standaard, let op;. gebruik `conda-forge` en NIET `default` channel ivm licentie, zie [is-conda-free](https://www.anaconda.com/blog/is-conda-free)
- `mamba`: 
    - Snellere conda. Ofwel [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) installer of [miniforge](https://github.com/conda-forge/miniforge)

- `poetry`: 
    - Bouwt op `pyproject.toml`. Pip env management met lock-files
    - Werkende FIXME files:
        - 
    - env install: ?
- `pixi`: 
    - Bouwt op `pyproject.toml`. Conda+pip env management met lock-files (https://prefix.dev/blog/pixi_for_scientists, [pixi vs poetry](https://pixi.sh/dev/switching_from/poetry/))
    - Werkende `pixi.toml` files;
        - https://github.com/HHNK/python-workflow-demo/pixi.toml
        - https://github.com/threedi/hhnk-threedi-tools/pixi.toml
        - https://github.com/prefix-dev/pixi/blob/main/pixi.toml
    - installer: 
    - env install: `pixi install` in het project.



# Formatting en linting
Gebruik van [Ruff](TODO link) via de VS-Code extentie. 