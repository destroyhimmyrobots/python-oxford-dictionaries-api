# oxford_dictionaries_api.TranslationApi

All URIs are relative to *https://od-api.oxforddictionaries.com:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entries_source_translation_language_word_id_translationstarget_translation_language_get**](TranslationApi.md#entries_source_translation_language_word_id_translationstarget_translation_language_get) | **GET** /entries/{source_translation_language}/{word_id}/translations&#x3D;{target_translation_language} | Retrieve translation for a given word


# **entries_source_translation_language_word_id_translationstarget_translation_language_get**
> RetrieveEntry entries_source_translation_language_word_id_translationstarget_translation_language_get(source_translation_language, word_id, target_translation_language, app_id, app_key)

Retrieve translation for a given word

 Use this to return translations for a given word. In the event that a word in the dataset does not have a direct translation, the response will be a [definition](documentation/glossary?term=entry) in the target language.    <div id=\"translation\"></div> 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.TranslationApi()
source_translation_language = 'source_translation_language_example' # str | IANA language code
word_id = 'word_id_example' # str | The source word
target_translation_language = 'target_translation_language_example' # str | IANA language code
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Retrieve translation for a given word
    api_response = api_instance.entries_source_translation_language_word_id_translationstarget_translation_language_get(source_translation_language, word_id, target_translation_language, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationApi->entries_source_translation_language_word_id_translationstarget_translation_language_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_translation_language** | **str**| IANA language code | 
 **word_id** | **str**| The source word | 
 **target_translation_language** | **str**| IANA language code | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**RetrieveEntry**](RetrieveEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

