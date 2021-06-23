"""Set up appapi"""
from setuptools import setup, find_packages

setup(
    name="appapi",
    packages=find_packages(),
    version="1.0",
    license="",
    description="Breqwatr sample API",
    author="Breqwatr",
    author_email="kyle.pericak@breqwatr.com",
    python_requires=">=3.0.0",
    zip_safe=False,
    install_requires=["gunicorn", "Flask"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
    ],
)
