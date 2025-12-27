import setuptools

with open ("README.md", "r", encoding ="UTF-8") as f:
    long_description = f.read()

    __version__ = "0.0.0"

    REPO_NAME = "end-to-end-ml-project-with DVC-MLflow"
    AUTHOR_USER_NAME = "SaurabhVilasAhire"
    SRC_REPO = "mlproject"
    AUTHOR_EMAIL = "saurabhahire222@gmail.com"

    setuptools.setup(
        name = SRC_REPO,
        version = __version__,
        author = AUTHOR_USER_NAME,
        author_email = AUTHOR_EMAIL,
        description = "A end to end ML project",
        long_description = long_description,
        long_description_content_type = "text/markdown",
        url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/",
        project_urls = {
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
        },
        package_dir = {"": "src"},
        packages = setuptools.find_packages(where="src"),
    )