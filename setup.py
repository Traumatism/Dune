from setuptools import setup, find_packages

setup(
    name="dune",
    author="traumatism",
    author_email="toast@mailfence.com",
    url="https://github.com/Traumatism/Dune",
    description="Dune is a minimal value storing database built in Python 3.10+",  # noqa
    version="0.0.1",
    packages=find_packages(where=".", exclude=["tests"]),
    install_requires=[
        "setuptools>=45.0",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.0",
        "Topic :: Utilities",
    ],
)
