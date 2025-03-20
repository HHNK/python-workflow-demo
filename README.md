# Python workflow demo
Standaard setup voor python-projects bij HHNK.

# IDE
Veel opties, we gebruiken [Visual Studio Code](https://code.visualstudio.com/download). Biedt goede integratie van notebooks en tal van andere entensies.

Overige IDE's\
Visual Studio Code Insiders [installer](https://code.visualstudio.com/insiders) - pre-releases, tegenwoordig niet zo meer nodig\
Cursor AI (https://www.cursor.com/) - Upcoming, vs-code based, maar vereist licentie, met juiste extensions kan deel ook in vs-code. 


Zie [settings.json](https://github.com/HHNK/python-workflow-demo/.vscode/settings.json) voor standaard instellingen.

Komt neer op de formatter on save draaien:
```
"[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.fixAll": "explicit"
    }
},
```

De `ruff` instelligen staan in de [pyproject.toml](https://github.com/HHNK/python-workflow-demo/pyproject.toml)

Defaults die we gebruiken over alle projecten zijn;
```
[tool.ruff]
# see https://docs.astral.sh/ruff/rules/ for meaning of rules
line-length = 119

#Exclude external packages in formatter
extend-exclude = [".pixi/*"]
include = ["*.py"]

[tool.ruff.lint]
select = ["D", "E", "F", "NPY", "PD", "C4", "I"]
ignore = ["D1", "D202", "D205", "D400", "D404", "E501", "PD002", "PD901"]
fixable = ["I"]

[tool.ruff.lint.pydocstyle]
convention = "numpy"

[tool.ruff.lint.per-file-ignores]
# Ignore unused imports in init
"__init__.py" = ["F401",  "I001"]

[tool.pylint]
disable = ["W1203"]
```

# Env management
Meerdere opties;\
- `conda`
    - Standaard, let op;. gebruik `conda-forge` en NIET `default` channel ivm licentie, zie [is-conda-free](https://www.anaconda.com/blog/is-conda-free)
- `mamba`
    - Snellere conda. Ofwel [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) installer of [miniforge](https://github.com/conda-forge/miniforge)

- `poetry`
    - Bouwt op `pyproject.toml`. Pip env management met lock-files
    - Werkende FIXME files:
        - 
    - env install: ?
- `pixi`
    - Bouwt op `pyproject.toml`. Conda+pip env management met lock-files        
        - https://prefix.dev/blog/pixi_for_scientists 
        - https://pixi.sh/dev/switching_from/poetry/
        - https://stackoverflow.com/questions/70851048/does-it-make-sense-to-use-conda-poetry
    - Werkende `pixi.toml` files;
        - https://github.com/HHNK/python-workflow-demo/pixi.toml
        - https://github.com/threedi/hhnk-threedi-tools/pixi.toml
        - https://github.com/prefix-dev/pixi/blob/main/pixi.toml
    - installer: 
    - env install: `pixi install` in het project.



# Formatting en linting
Gebruik van [Ruff](https://docs.astral.sh/ruff/) als vs-code extentie.
Zie  



# AI helpers
Lokaal thuis een [ollama](https://ollama.com/) installatie draaien waarmee je lokaal AI kan draaien. Met de [Continue](https://docs.continue.dev/getting-started/install) extension zijn code-hints mogelijk zonder de limieten van de free-tier van [copilot](https://code.visualstudio.com/docs/copilot/overview).