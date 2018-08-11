# oxford_dictionaries_api.TheSentenceDictionaryApi

All URIs are relative to *https://od-api.oxforddictionaries.com:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entries_source_language_word_id_sentences_get**](TheSentenceDictionaryApi.md#entries_source_language_word_id_sentences_get) | **GET** /entries/{source_language}/{word_id}/sentences | Retrieve corpus sentences for a given word


# **entries_source_language_word_id_sentences_get**
> SentencesResults entries_source_language_word_id_sentences_get(source_language, word_id, app_id, app_key)

Retrieve corpus sentences for a given word

 Use this to retrieve sentences extracted from  corpora which show how a word is used in the language. This is available for English and Spanish. For English, the sentences are linked to the correct [sense](documentation/glossary?term=sense) of the word in the dictionary. In Spanish, they are linked at the [headword](documentation/glossary?term=headword) level.   <div id=\"sentences\"></div> 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.TheSentenceDictionaryApi()
source_language = 'source_language_example' # str | IANA language code
word_id = 'word_id_example' # str | An Entry identifier. Case-sensitive.
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Retrieve corpus sentences for a given word
    api_response = api_instance.entries_source_language_word_id_sentences_get(source_language, word_id, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TheSentenceDictionaryApi->entries_source_language_word_id_sentences_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_language** | **str**| IANA language code | 
 **word_id** | **str**| An Entry identifier. Case-sensitive. | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**SentencesResults**](SentencesResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

