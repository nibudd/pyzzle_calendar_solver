# pyzzle_calendar_solver

# environment
First, install `pip-tools` in the virtual environment
```sh
pip install pip-tools
```

To recompile requirements files with the newest versions of all packages:

```sh
pip-compile --upgrade -o requirements/src.txt pyproject.toml
pip-compile --upgrade --extra dev -o requirements/dev.txt pyproject.toml
```