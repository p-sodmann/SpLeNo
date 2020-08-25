import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="spacy-spleno",
    version="0.0.1",
    description="Easy writing and loading of custom lemmas",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/theudas/SpLeNo",
    author="Philipp Sodmann",
    author_email="psodmann@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["spleno"],
    include_package_data=True,
    install_requires=["spacy"]
)