# Technical Project Template

<!-- Uncomment to display test coverage badges -->
<!-- <div align="center">
<img src="cov/ub18cov.svg">
<img src="cov/ub20cov.svg">
</div> -->

Continuous documentation and reporting for technical projects.

## Setting up your project

Start by installing Cookiecutter by running `pip install cookiecutter`. Then:

1. Set up a new project. You will be asked for its name, and that of its Python source directory.
   
   `cookiecutter https://github.com/alopezrivera/template_technical`
2. Edit `docs/source/project.py` and `docs/source/project.sty` with the details of your project.
3. Push your project's initial commit to GitHub.
5. Set up the host for your documentation site. Your options:
   - A `docs` branch has been automatically created. It is the default host for your documentation site.
   - Create an external repository to host, and introduce its details in `config.env`. In this case, you will need to have write permission to the repo, and create a **secret** called **API_TOKEN_GITHUB** in your repository with a personal API token (check your profile -> developer settings -> keys). Push the updated `config.env` and enjoy. All is set.

If you go to the Actions tab of your repo you will see an action running, with two jobs: one for the documentation site and another generating a technical report.

## Important files

### `config.env`

Sets the terminal environment variables of the GitHub runners 
which generate and upload your site and report.

### `requirements.txt`

Requirements of your Python package.

### `docs/source/project.py`

Project name, author, `codename` (Python package name)
and report title.

### LaTeX: `docs/source/project.sty`

Project name, institution, logo and design settings.
