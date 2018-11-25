import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Stopwords-GuilanNLP",
    version=__import__("Stopwords-GuilanNLP").stopword_version() + " " + "2.0",
    author="Javad PourMostafa",
    author_email="javad.pourmostafa@gmail.com",
    description="A comprehensive package for stopwords in NLP and text mining",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    url="https://github.com/joyebright/Stopword-GuilanNLP",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: NLP",
        "Topic :: Pre-processing in text mining",
    ],
)
