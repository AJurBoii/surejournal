## Description
What initially started as a purely tutorial repo, has now morphed into a tutorial/personal project. I follow along with [Corey Schafer's FastAPI tutorial series on YouTube.](https://www.youtube.com/playlist?list=PL-osiE80TeTsak-c-QsVeg0YYG_0TeyXI) while making my own edits to match what I want this application to be. My goal is to make a mental health journaling app with the following features:
- [] a database for users to keep their journal entries and stuff
- [] user authentication/authorization
- [] mood tracking
- [] interactive guided breathing exercises
- [] mental health research hub

The secondary intention with this project is to understand FastAPI as an end user and then explore its open source codebase which I've forked. I hope to make a meaningful contribution to the FastAPI codebase and by doing so, improving my ability to:
- read other people's code
- navigate large codebases
- contribute to open source projects

### Replicate my setup!
I'm using Windows Subsystem for Linux (WSL) Ubuntu 24.04.
1. Install `uv`:
```
pip install uv
```
2. Use `uv` to initiate your project:
```
uv init fastapi-blog
```
3. I forked and cloned the FastAPI repo locally. The file structure is as follows:
- Projects root
    - pyproject.toml
    - (Your project)
        - Your files, etc.
        - pyproject.toml
    - FastAPI
        - FastAPI files, etc.
4. To be able to import your local FastAPI module, navigate to the outer `pyproject.toml` file (`Projects root/pyproject.toml`) and add the following:
```
[tool.uv.workspace]
members = ["fastapi", "fastapi-blog"]
```
Then navigate to the inner `pyproject.toml` (`(Your project)/pyproject.toml`) and add:
```
dependencies = [
    "fastapi",
]
[tool.uv.sources]
fastapi = {workspace = true}
```
5. Navigate to the Project root (`~/projects/`) and run `uv sync`.
6. Run `uv add "fastapi[standard]"`
Voila! You should be able to use your local FastAPI repo for your project!

### Setup troubleshooting
Please refer to the official FastAPI documentation located [here](https://fastapi.tiangolo.com/) for any questions on how to install and use FastAPI if your setup differs from mine.
