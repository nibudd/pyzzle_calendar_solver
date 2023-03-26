# pyzzle_calendar_solver

# environment
To recompile requirements files with the newest versions of all packages:
- requirements/src.txt

```sh
pip-compile --upgrade -o requirements/src.txt pyproject.toml
pip-compile --upgrade --extra dev -o requirements/dev.txt pyproject.toml
```