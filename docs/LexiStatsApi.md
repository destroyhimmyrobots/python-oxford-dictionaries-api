# oxford_dictionaries_api.LexiStatsApi

All URIs are relative to *https://od-api.oxforddictionaries.com:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stats_frequency_ngrams_source_lang_corpus_ngram_size_get**](LexiStatsApi.md#stats_frequency_ngrams_source_lang_corpus_ngram_size_get) | **GET** /stats/frequency/ngrams/{source_lang}/{corpus}/{ngram-size}/ | Retrieve the frequency of ngrams (1-4) derived from a corpus
[**stats_frequency_word_source_lang_get**](LexiStatsApi.md#stats_frequency_word_source_lang_get) | **GET** /stats/frequency/word/{source_lang}/ | Retrieve the frequency of a word derived from a corpus.
[**stats_frequency_words_source_lang_get**](LexiStatsApi.md#stats_frequency_words_source_lang_get) | **GET** /stats/frequency/words/{source_lang}/ | Retrieve a list of frequencies of a word/words derived from a corpus.


# **stats_frequency_ngrams_source_lang_corpus_ngram_size_get**
> NgramsResult stats_frequency_ngrams_source_lang_corpus_ngram_size_get(source_lang, corpus, ngram_size, app_id, app_key, tokens=tokens, contains=contains, punctuation=punctuation, format=format, min_frequency=min_frequency, max_frequency=max_frequency, min_document_frequency=min_document_frequency, max_document_frequency=max_document_frequency, collate=collate, sort=sort, offset=offset, limit=limit)

Retrieve the frequency of ngrams (1-4) derived from a corpus

This endpoint returns frequencies of ngrams of size 1-4. That is the number of times a word (ngram size = 1) or words (ngram size > 1) appear in the corpus. Ngrams are case sensitive (\"I AM\" and \"I am\" will have different frequency) and frequencies are calculated per word (true case) so \"the book\" and \"the books\" are two different ngrams. The results can be filtered based on query parameters. <br> <br> Parameters can be provided in PATH, GET or POST (form or json). The parameters in PATH are overridden by parameters in GET, POST and json (in that order). In PATH, individual options are separated by semicolon and values are separated by commas (where multiple values can be used). <br> <br> Example for bigrams (ngram of size 2): * PATH: /tokens=a word,another word * GET: /?tokens=a word&tokens=another word * POST (json):    ```javascript     {         \"tokens\": [\"a word\", \"another word\"]     }   ```  Either \"tokens\" or \"contains\" has to be provided. <br> <br> Some queries with \"contains\" or \"sort\" can exceed the 30s timeout, in which case the API will return an error message with status code 503. You mitigate this by providing additional restrictions such as \"minFrequency\" and \"maxFrequency\". <br> <br> You can use the parameters \"offset\" and \"limit\" to paginate through large result sets. For convenience, the HTTP header \"Link\" is set on the response to provide links to \"first\", \"self\", \"next\", \"prev\" and \"last\" pages of results (depending on the context). For example, if the result set contains 50 results and the parameter \"limit\" is set to 25, the Links header will contain an URL for the first 25 results and the next 25 results. <br> <br> Some libraries such as python's `requests` can parse the header automatically and offer a convenient way of iterating through the results. For example: ```python def get_all_results(url):     while url:         r = requests.get(url)         r.raise_for_status()         for item in r.json()['results']:           yield item         url = r.links.get('next', {}).get('url') ``` 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.LexiStatsApi()
source_lang = 'source_lang_example' # str | IANA language code
corpus = 'corpus_example' # str | For corpora other than 'nmc' (New Monitor Corpus) please contact api@oxforddictionaries.com
ngram_size = 'ngram_size_example' # str | the size of ngrams requested (1-4)
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )
tokens = 'a word' # str | List of tokens to filter. The tokens are separated by spaces, the list items are separated by comma (e.g., for bigrams (n=2) tokens=this is,this was, this will) (optional) (default to a word)
contains = 'contains_example' # str | Find ngrams containing the given token(s). Use comma or space as token separators; the order of tokens is irrelevant. (optional)
punctuation = 'punctuation_example' # str | Flag specifying whether to lookup ngrams that include punctuation or not (possible values are \"true\" and \"false\"; default is \"false\") (optional)
format = 'oup' # str | Option specifying whether tokens should be returned as a single string (option \"google\") or as a list of strings (option \"oup\") (optional) (default to oup)
min_frequency = 789 # int | Restrict the query to entries with frequency of at least `minFrequency` (optional)
max_frequency = 789 # int | Restrict the query to entries with frequency of at most `maxFrequency` (optional)
min_document_frequency = 789 # int | Restrict the query to entries that appear in at least `minDocumentFrequency` documents (optional)
max_document_frequency = 789 # int | Restrict the query to entries that appera in at most `maxDocumentFrequency` documents (optional)
collate = 'collate_example' # str | collate the results by wordform, trueCase, lemma, lexicalCategory. Multiple values can be separated by commas (e.g., collate=trueCase,lemma,lexicalCategory). (optional)
sort = 'sort_example' # str | sort the resulting list by wordform, trueCase, lemma, lexicalCategory, frequency, normalizedFrequency. Descending order is achieved by prepending the value with the minus sign ('-'). Multiple values can be separated by commas (e.g., sort=lexicalCategory,-frequency) (optional)
offset = 0 # int | pagination - results offset (optional) (default to 0)
limit = 100 # int | pagination - results limit (optional) (default to 100)

try:
    # Retrieve the frequency of ngrams (1-4) derived from a corpus
    api_response = api_instance.stats_frequency_ngrams_source_lang_corpus_ngram_size_get(source_lang, corpus, ngram_size, app_id, app_key, tokens=tokens, contains=contains, punctuation=punctuation, format=format, min_frequency=min_frequency, max_frequency=max_frequency, min_document_frequency=min_document_frequency, max_document_frequency=max_document_frequency, collate=collate, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LexiStatsApi->stats_frequency_ngrams_source_lang_corpus_ngram_size_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **corpus** | **str**| For corpora other than &#39;nmc&#39; (New Monitor Corpus) please contact api@oxforddictionaries.com | 
 **ngram_size** | **str**| the size of ngrams requested (1-4) | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]
 **tokens** | **str**| List of tokens to filter. The tokens are separated by spaces, the list items are separated by comma (e.g., for bigrams (n&#x3D;2) tokens&#x3D;this is,this was, this will) | [optional] [default to a word]
 **contains** | **str**| Find ngrams containing the given token(s). Use comma or space as token separators; the order of tokens is irrelevant. | [optional] 
 **punctuation** | **str**| Flag specifying whether to lookup ngrams that include punctuation or not (possible values are \&quot;true\&quot; and \&quot;false\&quot;; default is \&quot;false\&quot;) | [optional] 
 **format** | **str**| Option specifying whether tokens should be returned as a single string (option \&quot;google\&quot;) or as a list of strings (option \&quot;oup\&quot;) | [optional] [default to oup]
 **min_frequency** | **int**| Restrict the query to entries with frequency of at least &#x60;minFrequency&#x60; | [optional] 
 **max_frequency** | **int**| Restrict the query to entries with frequency of at most &#x60;maxFrequency&#x60; | [optional] 
 **min_document_frequency** | **int**| Restrict the query to entries that appear in at least &#x60;minDocumentFrequency&#x60; documents | [optional] 
 **max_document_frequency** | **int**| Restrict the query to entries that appera in at most &#x60;maxDocumentFrequency&#x60; documents | [optional] 
 **collate** | **str**| collate the results by wordform, trueCase, lemma, lexicalCategory. Multiple values can be separated by commas (e.g., collate&#x3D;trueCase,lemma,lexicalCategory). | [optional] 
 **sort** | **str**| sort the resulting list by wordform, trueCase, lemma, lexicalCategory, frequency, normalizedFrequency. Descending order is achieved by prepending the value with the minus sign (&#39;-&#39;). Multiple values can be separated by commas (e.g., sort&#x3D;lexicalCategory,-frequency) | [optional] 
 **offset** | **int**| pagination - results offset | [optional] [default to 0]
 **limit** | **int**| pagination - results limit | [optional] [default to 100]

### Return type

[**NgramsResult**](NgramsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_frequency_word_source_lang_get**
> StatsWordResult stats_frequency_word_source_lang_get(source_lang, app_id, app_key, corpus=corpus, wordform=wordform, true_case=true_case, lemma=lemma, lexical_category=lexical_category)

Retrieve the frequency of a word derived from a corpus.

This endpoint provides the frequency of a given word. When multiple database records match the query parameters, the returned frequency is the sum of the individual frequencies. For example, if the query parameters are lemma=test, the returned frequency will include the verb \"test\", the noun \"test\" and the adjective \"test\" in all forms (Test, tested, testing, etc.) <br> <br> If you are interested in the frequency of the word \"test\" but want to exclude other forms (e.g., tested) use the option trueCase=test. Normally, the word \"test\" will be spelt with a capital letter at the beginning of a sentence. The option trueCase will ignore this and it will count \"Test\" and \"test\" as the same token. If you are interested in frequencies of \"Test\" and \"test\", use the option wordform=test or wordform=Test. Note that trueCase is not just a lower case of the word as some words are genuinely spelt with a capital letter such as the word \"press\" in Oxford University Press. <br> <br> Parameters can be provided in PATH, GET or POST (form or json). The parameters in PATH are overriden by parameters in GET, POST and json (in that order). In PATH, individual options are separated by semicolon and values are separated by commas (where multiple values can be used). Examples: * PATH: /lemma=test;lexicalCategory=noun * GET: /?lemma=test&lexicalCategory=noun * POST (json):    ```javascript     {       \"lemma\": \"test\",       \"lexicalCategory\": \"noun\"     }   ```  <br> One of the options wordform/trueCase/lemma/lexicalCategory has to be provided. 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.LexiStatsApi()
source_lang = 'source_lang_example' # str | IANA language code
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )
corpus = 'nmc' # str | For corpora other than 'nmc' (New Monitor Corpus) please contact api@oxforddictionaries.com (optional) (default to nmc)
wordform = 'wordform_example' # str | The written form of the word to look up (preserving case e.g., Books vs books) (optional)
true_case = 'true_case_example' # str | The written form of the word to look up with normalised case (Books --> books) (optional)
lemma = 'test' # str | The lemma of the word to look up (e.g., Book, booked, books all have the lemma \"book\") (optional) (default to test)
lexical_category = 'lexical_category_example' # str | The lexical category of the word(s) to look up (e.g., noun or verb) (optional)

try:
    # Retrieve the frequency of a word derived from a corpus.
    api_response = api_instance.stats_frequency_word_source_lang_get(source_lang, app_id, app_key, corpus=corpus, wordform=wordform, true_case=true_case, lemma=lemma, lexical_category=lexical_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LexiStatsApi->stats_frequency_word_source_lang_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]
 **corpus** | **str**| For corpora other than &#39;nmc&#39; (New Monitor Corpus) please contact api@oxforddictionaries.com | [optional] [default to nmc]
 **wordform** | **str**| The written form of the word to look up (preserving case e.g., Books vs books) | [optional] 
 **true_case** | **str**| The written form of the word to look up with normalised case (Books --&gt; books) | [optional] 
 **lemma** | **str**| The lemma of the word to look up (e.g., Book, booked, books all have the lemma \&quot;book\&quot;) | [optional] [default to test]
 **lexical_category** | **str**| The lexical category of the word(s) to look up (e.g., noun or verb) | [optional] 

### Return type

[**StatsWordResult**](StatsWordResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_frequency_words_source_lang_get**
> StatsWordResultList stats_frequency_words_source_lang_get(source_lang, app_id, app_key, corpus=corpus, wordform=wordform, true_case=true_case, lemma=lemma, lexical_category=lexical_category, grammatical_features=grammatical_features, sort=sort, collate=collate, min_frequency=min_frequency, max_frequency=max_frequency, min_normalized_frequency=min_normalized_frequency, max_normalized_frequency=max_normalized_frequency, offset=offset, limit=limit)

Retrieve a list of frequencies of a word/words derived from a corpus.

This endpoint provides a list of frequencies for a given word or words. Unlike the /word/ endpoint, the results are split into the smallest units. <br> <br> To exclude a specific value, prepend it with the minus sign ('-'). For example, to get frequencies of the lemma 'happy' but exclude superlative forms (i.e., happiest) you could use options 'lemma=happy;grammaticalFeatures=-degreeType:superlative'. <br> <br> Parameters can be provided in PATH, GET or POST (form or json). The parameters in PATH are overridden by parameters in GET, POST and json (in that order). In PATH, individual options are separated by semicolon and values are separated by commas (where multiple values can be used). <br> <br> The parameters wordform/trueCase/lemma/lexicalCategory also exist in a plural form, taking a lists of items. Examples: * PATH: /wordforms=happy,happier,happiest * GET: /?wordforms=happy&wordforms=happier&wordforms=happiest * POST (json): ```javascript   {     \"wordforms\": [\"happy\", \"happier\", \"happiest\"]   } ``` A mor complex example of retrieving frequencies of multiple lemmas: ```   {       \"lemmas\": [\"happy\", \"content\", \"cheerful\", \"cheery\", \"merry\", \"joyful\", \"ecstatic\"],       \"grammaticalFeatures\": {           \"adjectiveFunctionType\": \"predicative\"       },       \"lexicalCategory\": \"adjective\",       \"sort\": [\"lemma\", \"-frequency\"]   } ``` Some queries with \"collate\" or \"sort\" can exceed the 30s timeout, in which case the API will return an error message with status code 503. You mitigate this by providing additional restrictions such as \"minFrequency\" and \"maxFrequency\". <br> <br> You can use the parameters \"offset\" and \"limit\" to paginate through large result sets. For convenience, the HTTP header \"Link\" is set on the response to provide links to \"first\", \"self\", \"next\", \"prev\" and \"last\" pages of results (depending on the context). For example, if the result set contains 50 results and the parameter \"limit\" is set to 25, the Links header will contain an URL for the first 25 results and the next 25 results. <br> <br> Some libraries such as python's `requests` can parse the header automatically and offer a convenient way of iterating through the results. For example: ```python def get_all_results(url):     while url:         r = requests.get(url)         r.raise_for_status()         for item in r.json()['results']:           yield item         url = r.links.get('next', {}).get('url') ``` 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.LexiStatsApi()
source_lang = 'source_lang_example' # str | IANA language code
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )
corpus = 'nmc' # str | For corpora other than 'nmc' (New Monitor Corpus) please contact api@oxforddictionaries.com (optional) (default to nmc)
wordform = 'wordform_example' # str | The written form of the word to look up (preserving case e.g., Book vs book) (optional)
true_case = 'true_case_example' # str | The written form of the word to look up with normalised case (Books --> books) (optional)
lemma = 'test' # str | The lemma of the word to look up (e.g., Book, booked, books all have the lemma \"book\") (optional) (default to test)
lexical_category = 'lexical_category_example' # str | The lexical category of the word(s) to look up (e.g., adjective or noun) (optional)
grammatical_features = 'grammatical_features_example' # str | The grammatical features of the word(s) to look up entered as a list of k:v (e.g., degree_type:comparative) (optional)
sort = 'sort_example' # str | sort the resulting list by wordform, trueCase, lemma, lexicalCategory, frequency, normalizedFrequency. Descending order is achieved by prepending the value with the minus sign ('-'). Multiple values can be separated by commas (e.g., sort=lexicalCategory,-frequency) (optional)
collate = 'collate_example' # str | collate the results by wordform, trueCase, lemma, lexicalCategory. Multiple values can be separated by commas (e.g., collate=trueCase,lemma,lexicalCategory). (optional)
min_frequency = 789 # int | Restrict the query to entries with frequency of at least `minFrequency` (optional)
max_frequency = 789 # int | Restrict the query to entries with frequency of at most `maxFrequency` (optional)
min_normalized_frequency = 3.4 # float | Restrict the query to entries with frequency of at least `minNormalizedFrequency` (optional)
max_normalized_frequency = 3.4 # float | Restrict the query to entries with frequency of at most `maxNormalizedFrequency` (optional)
offset = 0 # int | pagination - results offset (optional) (default to 0)
limit = 100 # int | pagination - results limit (optional) (default to 100)

try:
    # Retrieve a list of frequencies of a word/words derived from a corpus.
    api_response = api_instance.stats_frequency_words_source_lang_get(source_lang, app_id, app_key, corpus=corpus, wordform=wordform, true_case=true_case, lemma=lemma, lexical_category=lexical_category, grammatical_features=grammatical_features, sort=sort, collate=collate, min_frequency=min_frequency, max_frequency=max_frequency, min_normalized_frequency=min_normalized_frequency, max_normalized_frequency=max_normalized_frequency, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LexiStatsApi->stats_frequency_words_source_lang_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]
 **corpus** | **str**| For corpora other than &#39;nmc&#39; (New Monitor Corpus) please contact api@oxforddictionaries.com | [optional] [default to nmc]
 **wordform** | **str**| The written form of the word to look up (preserving case e.g., Book vs book) | [optional] 
 **true_case** | **str**| The written form of the word to look up with normalised case (Books --&gt; books) | [optional] 
 **lemma** | **str**| The lemma of the word to look up (e.g., Book, booked, books all have the lemma \&quot;book\&quot;) | [optional] [default to test]
 **lexical_category** | **str**| The lexical category of the word(s) to look up (e.g., adjective or noun) | [optional] 
 **grammatical_features** | **str**| The grammatical features of the word(s) to look up entered as a list of k:v (e.g., degree_type:comparative) | [optional] 
 **sort** | **str**| sort the resulting list by wordform, trueCase, lemma, lexicalCategory, frequency, normalizedFrequency. Descending order is achieved by prepending the value with the minus sign (&#39;-&#39;). Multiple values can be separated by commas (e.g., sort&#x3D;lexicalCategory,-frequency) | [optional] 
 **collate** | **str**| collate the results by wordform, trueCase, lemma, lexicalCategory. Multiple values can be separated by commas (e.g., collate&#x3D;trueCase,lemma,lexicalCategory). | [optional] 
 **min_frequency** | **int**| Restrict the query to entries with frequency of at least &#x60;minFrequency&#x60; | [optional] 
 **max_frequency** | **int**| Restrict the query to entries with frequency of at most &#x60;maxFrequency&#x60; | [optional] 
 **min_normalized_frequency** | **float**| Restrict the query to entries with frequency of at least &#x60;minNormalizedFrequency&#x60; | [optional] 
 **max_normalized_frequency** | **float**| Restrict the query to entries with frequency of at most &#x60;maxNormalizedFrequency&#x60; | [optional] 
 **offset** | **int**| pagination - results offset | [optional] [default to 0]
 **limit** | **int**| pagination - results limit | [optional] [default to 100]

### Return type

[**StatsWordResultList**](StatsWordResultList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

