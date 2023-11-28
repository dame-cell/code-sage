from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="code-sage",
    version="0.0.10",
    description = "CodeSage is a Python library for reading and analyzing code using advanced language models.",
    package_dir={"": "code_sage"},
    packages=find_packages(where="code_sage"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dame-cell/code-sage",
    author="Dame Rajee",
    author_email="doss72180@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["click >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0"],
    },
    python_requires=">=3.10",
)