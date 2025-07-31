from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-PROJECT-CircleCI",
    version="0.1",
    author="Aishwarya",
    packages=find_packages(),
    install_requires = requirements,
)