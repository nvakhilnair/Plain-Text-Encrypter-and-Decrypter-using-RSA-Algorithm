from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="PyPI_upload_package",
    version="1.0.1",
    description="This Gui application is used upload your package to PyPI and PyPI Test",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/nvakhilnair/",
    author="Akhil",
    author_email="nvakhilnair@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["pythonfiles"],
    include_package_data=True,
    install_requires=["PyQt4"],
    entry_points={
        "console_scripts": [
            "PyPI_upload_package=pythonfiles.PyPI_upload_package:main",
        ]
    },
)
