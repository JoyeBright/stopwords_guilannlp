## Stopwords Guilan NLP

This is  a comprehensive stopwords for natural language processing and text mining.

## Installation

[Now stopwords_guilannlp is on PyPI!](https://pypi.org/project/stopwords-guilannlp)
<br>
   * Download via PyPI: 
   ```
   $ pip3 install stopwords_guilannlp
   ```
   * Or clone the repo: 
   ```
   $ git clone --recursive git://github.com/JoyeBright/Sstopwords_guilannlp.git
   ```
   * Then install it: 
   ```
   $ python3 setup.py install
   ```

## Usage
 ```
 tokens = word_tokenize(s)
          filtered_tokens = []
          stopwords = stopwords_output("Persian", "nar")
          for w in tokens:
              if w not in stopwords:
                  filtered_tokens.append(w)
          return filtered_tokens
 ```
 * Note: Package does not support tokenizing process.
## Supported Languages
   * English
   * Persian

## Type of Outputs
   * Dataframe
   * Numpy Array
   * Set
   * List
