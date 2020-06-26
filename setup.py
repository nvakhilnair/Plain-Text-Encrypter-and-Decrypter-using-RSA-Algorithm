from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="encryption_decryption_RSA",
    version="1.0.0",
    description="GUI application is used for plain text decryption and encryption using RSA algorithm",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/nvakhilnair/Plain-Text-Encrypter-and-Decrypter-using-RSA-Algorithm",
    author="Akhil",
    author_email="MadeWithPY009@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["PyQt4>=4.11.4"],
    scripts=["encryption_decryption_RSA.py"],
    package_data={'data': ['logo.png','icon.ico']},
    include_package_data=True,
)
