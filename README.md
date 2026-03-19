## Description
Hello! This is a tutorial repo where I follow along to Corey Schafer's FastAPI series on YouTube, which can be found [here](https://www.youtube.com/playlist?list=PL-osiE80TeTsak-c-QsVeg0YYG_0TeyXI).

The plan is to understand FastAPI as an end user and then explore its open source codebase which I've forked. I hope to make a meaningful contribution to the FastAPI codebase and by doing so, improving my ability to:
- read other people's code
- navigate large codebases
- contribute to open source projects

### Replicate my setup!
I'm using Windows Subsystem for Linux (WSL) Ubuntu 24.04.
1. Install `uv`:
` ` `
[terminal]
pip install uv
` ` `
2. Use `uv` to initiate your project:
` ` `
[terminal]
uv init fastapi-blog
` ` `
3. I forked and cloned the FastAPI repo locally. The file structure is as follows:
- Projects root
    - pyproject.toml
    - (Your project)
        - Your files, etc.
        - pyproject.toml
    - FastAPI
        - FastAPI files, etc.
4. To be able to import your local FastAPI module, navigate to the outer `pyproject.toml` file (`Projects root/pyproject.toml`) and add the following:
` ` `
[tool.uv.workspace]
members = ["fastapi", "fastapi-blog"]
` ` `
Then navigate to the inner `pyproject.toml` (`(Your project)/pyproject.toml`) and add:
` ` `
dependencies = [
    "fastapi",
]
[tool.uv.sources]
fastapi = {workspace = true}
` ` `
5. Finally, navigate to the Project root (`~/projects/`) and run `uv sync`.
Voila! You should be able to use your local FastAPI repo for your project!

### Setup troubleshooting
Please refer to the official FastAPI documentation located [here](https://fastapi.tiangolo.com/) for any questions on how to install and use FastAPI if your setup differs from mine.