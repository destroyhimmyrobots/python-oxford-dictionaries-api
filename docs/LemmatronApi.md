# oxford_dictionaries_api.LemmatronApi

All URIs are relative to *https://od-api.oxforddictionaries.com:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inflections_source_lang_word_id_filters_get**](LemmatronApi.md#inflections_source_lang_word_id_filters_get) | **GET** /inflections/{source_lang}/{word_id}/{filters} | Apply optional filters to Lemmatron response
[**inflections_source_lang_word_id_get**](LemmatronApi.md#inflections_source_lang_word_id_get) | **GET** /inflections/{source_lang}/{word_id} | Check a word exists in the dictionary and retrieve its root form


# **inflections_source_lang_word_id_filters_get**
> Lemmatron inflections_source_lang_word_id_filters_get(source_lang, word_id, filters, app_id, app_key)

Apply optional filters to Lemmatron response

 Retrieve available [lemmas](documentation/glossary?term=lemma) for a given [inflected](documentation/glossary?term=inflection) wordform. Filter results by categories.      <div id=\"lemmatron_filters\"></div> 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.LemmatronApi()
source_lang = 'source_lang_example' # str | IANA language code
word_id = 'word_id_example' # str | The input word
filters = ['filters_example'] # list[str] | Separate filtering conditions using a semicolon. Conditions take values grammaticalFeatures and/or lexicalCategory and are case-sensitive. To list multiple values in single condition divide them with comma.
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Apply optional filters to Lemmatron response
    api_response = api_instance.inflections_source_lang_word_id_filters_get(source_lang, word_id, filters, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LemmatronApi->inflections_source_lang_word_id_filters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **word_id** | **str**| The input word | 
 **filters** | [**list[str]**](str.md)| Separate filtering conditions using a semicolon. Conditions take values grammaticalFeatures and/or lexicalCategory and are case-sensitive. To list multiple values in single condition divide them with comma. | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**Lemmatron**](Lemmatron.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inflections_source_lang_word_id_get**
> Lemmatron inflections_source_lang_word_id_get(source_lang, word_id, app_id, app_key)

Check a word exists in the dictionary and retrieve its root form

 Use this to check if a word exists in the dictionary, or what 'root' form it links to (e.g., swimming > swim). The response tells you the possible [lemmas](documentation/glossary?term=lemma) for a given [inflected](documentation/glossary?term=inflection) word. This can then be combined with other endpoints to retrieve more information.    <div id=\"lemmatron\"></div> 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.LemmatronApi()
source_lang = 'source_lang_example' # str | IANA language code
word_id = 'word_id_example' # str | The input word
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Check a word exists in the dictionary and retrieve its root form
    api_response = api_instance.inflections_source_lang_word_id_get(source_lang, word_id, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LemmatronApi->inflections_source_lang_word_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **word_id** | **str**| The input word | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**Lemmatron**](Lemmatron.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

