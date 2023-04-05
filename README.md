## Stopwords Guilan NLP

A python package to be used in removing stopwords in different languages.

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
  * Afrikaans
  * Arabic
  * Armenian
  * Basque
  * Bengali
  * Breton
  * Bulgarian
  * Catalan
  * Chinese
  * Croatian
  * Czech
  * Danish
  * Dutch
  * English
  * Esperanto
  * Estonian
  * Finnish
  * French
  * Galician
  * German
  * Greek
  * Hausa
  * Hebrew
  * Hindi
  * Hungarian
  * Indonesian
  * Irish
  * Italian
  * Japanese
  * Korean
  * Latin
  * Latvian
  * Marathi
  * Norwegian
  * Persian
  * Polish
  * Portuguese
  * Romanian
  * Russian
  * Slovak
  * Slovenian
  * Somalia
  * Southern Sotho
  * Spanish
  * Swahili
  * Swedish
  * Thai
  * Turkish
  * Yoruba
  * Zulu

## Type of Outputs
   * Dataframe
   * Numpy Array
   * Set
   * List
