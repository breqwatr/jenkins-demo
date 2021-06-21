"""Set up applib"""
from setuptools import setup, find_packages

setup(
    name="applib",
    packages=find_packages(),
    version="1.0",
    license="",
    description="Application lib",
    author="Breqwatr",
    author_email="info@breqwatr.com",
    python_requires=">=3.0.0",
    install_requires=["pytest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
    ],
)
