import setuptools

with open("README.md", 'r', encoding="utf-8") as file:
    long_descrip = file.read()

__version__ = "0.0.0"

REPO_NAME = "END-TO-END-KINDEY-DISEASE-CLASSIFICATION---DEEP-LEARNING"
AUTHOR_NAME = "adityagarwal2005"
SRC_REPO = "kidney"
AUTHOR_LINKEDIN = "www.linkedin.com/in/aditya-agarwal-03294128a"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    description=REPO_NAME,
    long_description=long_descrip,
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
