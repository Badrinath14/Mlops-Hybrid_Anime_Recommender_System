from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Mlops_Hybrid_Anime_Recommender",
    version="0.1",
    author="Badrinath",
    packages=find_packages(),
    install_requires = requirements,
)