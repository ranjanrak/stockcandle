from setuptools import setup


README = open("README.md").read()

setup(
    name="stockcandle",  
    version="0.2",
    author="Rakesh R",
    author_email="rrrakesh265@gmail.com",
    description="Python library to fetch intraday data for any given EQ symbol",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ranjanrak/stockcandle.git",
    packages=['stockcandle'],
    install_requires=["requests"],
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries"
    ],
)