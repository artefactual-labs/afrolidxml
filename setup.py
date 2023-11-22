from setuptools import find_packages, setup

import afrolidxml.meta as meta

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="afrolidxml",
    version=meta.version,
    description=meta.description,
    long_description=readme,
    url="https://github.com/artefactual-labs/afrolidxml",
    author=meta.author,
    author_email=meta.email,
    license=meta.license_description,
    packages=find_packages(),
    install_requires=[
        "afrolid==0.1.0",
        "click==8.1.7",
        "xmltodict==0.13.0",
    ],
    entry_points={
        "console_scripts": [
            "afrolidxml = afrolidxml.cli:afrolidxml",
        ],
    },
)
