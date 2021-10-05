## NLP Stopwords

This is  a comprehensive stopwords for natural language processing and text mining.


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

## Related Repository
* [persian-stop-word](https://github.com/amirshnll/persian-stop-word/)
* [stopwords-json](https://github.com/6/stopwords-json)