import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stopwords_guilannlp",
    version=__import__("stopwords_guilannlp").stopword_version() + "." + "3.5",
    author="Javad Pourmostafa",
    author_email="javad.pourmostafa@gmail.com",
    description="A python package to be used in removing stopwords in different languages.",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    url="https://github.com/joyebright/stopwords_guilannlp",
    packages=setuptools.find_packages(),
    zip_safe=False,
    package_data={
        'stopwords_guilannlp': [
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
