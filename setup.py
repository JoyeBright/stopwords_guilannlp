import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nlpstopwords",
    version=__import__("nlpstopwords").stopword_version() + "." + "3.5",
    author="Amir Shokri",
    author_email="amirsh.nll@gmail.com",
    description="A comprehensive package for stopwords in NLP and text mining",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    url="https://github.com/amirshnll/nlpstopwords",
    packages=setuptools.find_packages(),
    zip_safe=False,
    package_data={
        'nlpstopwords': [
            'Languages/*.json'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing",
        "Topic :: Utilities"
    ],
)
