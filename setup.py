"""Setup file for PyPi"""
from setuptools import find_packages, setup

with open("README.md") as readme_file:
    README = readme_file.read()

setup_args = dict(
    name="mytoyota",
    version="0.0.2",
    description="Tool to communicate with Toyota Connected Services.",
    long_description_content_type="text/markdown",
    long_description=README,
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    author="Simon Hansen",
    author_email="simongrud@gmail.com",
    keywords=["Toyota", "MyT", "API"],
    url="https://github.com/DurgNomis-drol/mytoyota",
)

install_requires = [
    "langcodes",
    "requests",
]

if __name__ == "__main__":
    setup(**setup_args, install_requires=install_requires)
