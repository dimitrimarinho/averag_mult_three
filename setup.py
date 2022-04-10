from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="averag_mult_three",
    version="0.0.1",
    author="Dimitri Marinho",
    author_email="my_email",
    description="Testando a criação de pacote em Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link",
    packages=find_packages(),
    python_requires='>=3.8',
)