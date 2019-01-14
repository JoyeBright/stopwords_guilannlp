import os
import pandas as pd

# I'd like to concat the date of releasing
__VERSION__ = [13, 2019]

current_directory = os.path.dirname(os.path.realpath(__file__))
languages_directory = os.path.join(current_directory, 'Languages')


def stopword_version():
    return ".".join(str(i) for i in __VERSION__)


class StopWordError(Exception):
    pass


def converter(stopword_file, output):
    if output == "df":
        # Data Frame
        return stopword_file
    if output == "nar":
        # Numpy Array
        return stopword_file.values
    if output == "set":
        # Set
        numpy_array = stopword_file.values
        return set(numpy_array.flatten())
    else:
        # List
        ls = stopword_file.values.T.tolist()
        # Remove the redundant bracket
        return ls[0]


def ingest(stopword_file, output):
    file = pd.read_csv(stopword_file, sep="\n", encoding="utf-8")
    output = output.lower()
    # Check the type of output
    try:
        if output != "df" and output != "nar" and output != "set" and output != "ls":
            raise ValueError
    except ValueError:
        print("There is no such an output! ...")
    # Convert the file into a desired type of output
    return converter(file, output)


def stopwords(language, output):
    filename = language.lower()
    stopword_directory = os.path.join(languages_directory, filename)
    stopword_file = stopword_directory + ".csv"
    # Check whether the language is supported or not
    try:
        open(stopword_file, 'r')
    except FileNotFoundError:
        print("The language does not support! ...")
    # Read the related CSV file
    # Second argument is in term of type of output
    # numpy array (nar), data frame (df), list (ls)
    return ingest(stopword_file, output)


def stopwords_output(language, output):
    try:
        return stopwords(language, output)
    except StopWordError:
        print("StopWordError, Contact with developer!")
