# oxford_dictionaries_api.DictionaryEntriesApi

All URIs are relative to *https://od-api.oxforddictionaries.com:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entries_source_lang_word_id_filters_get**](DictionaryEntriesApi.md#entries_source_lang_word_id_filters_get) | **GET** /entries/{source_lang}/{word_id}/{filters} | Apply filters to response
[**entries_source_lang_word_id_get**](DictionaryEntriesApi.md#entries_source_lang_word_id_get) | **GET** /entries/{source_lang}/{word_id} | Retrieve dictionary information for a given word
[**entries_source_lang_word_id_regionsregion_get**](DictionaryEntriesApi.md#entries_source_lang_word_id_regionsregion_get) | **GET** /entries/{source_lang}/{word_id}/regions&#x3D;{region} | Specify GB or US dictionary for English entry search


# **entries_source_lang_word_id_filters_get**
> RetrieveEntry entries_source_lang_word_id_filters_get(source_lang, word_id, filters, app_id, app_key)

Apply filters to response

 Use filters to limit the [entry](documentation/glossary?term=entry) information that is returned. For example, you may only require definitions and not everything else, or just [pronunciations](documentation/glossary?term=pronunciation). The full list of filters can be retrieved from the filters Utility endpoint. You can also specify values within the filter using '='. For example 'grammaticalFeatures=singular'. Filters can also be combined using a semicolon.    <div id=\"dictionary_entries_filters\"></div> 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.DictionaryEntriesApi()
source_lang = 'source_lang_example' # str | IANA language code
word_id = 'word_id_example' # str | An Entry identifier. Case-sensitive.
filters = ['filters_example'] # list[str] | Separate filtering conditions using a semicolon. Conditions take values grammaticalFeatures and/or lexicalCategory and are case-sensitive. To list multiple values in single condition divide them with comma.
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Apply filters to response
    api_response = api_instance.entries_source_lang_word_id_filters_get(source_lang, word_id, filters, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryEntriesApi->entries_source_lang_word_id_filters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **word_id** | **str**| An Entry identifier. Case-sensitive. | 
 **filters** | [**list[str]**](str.md)| Separate filtering conditions using a semicolon. Conditions take values grammaticalFeatures and/or lexicalCategory and are case-sensitive. To list multiple values in single condition divide them with comma. | 
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

# **entries_source_lang_word_id_get**
> RetrieveEntry entries_source_lang_word_id_get(source_lang, word_id, app_id, app_key)

Retrieve dictionary information for a given word

 Use this to retrieve definitions, [pronunciations](documentation/glossary?term=pronunciation), example sentences, [grammatical information](documentation/glossary?term=grammaticalfeatures) and [word origins](documentation/glossary?term=etymology). It only works for dictionary [headwords](documentation/glossary?term=headword), so you may need to use the [Lemmatron](documentation/glossary?term=lemma) first if your input is likely to be an [inflected](documentation/glossary?term=inflection) form (e.g., 'swimming'). This would return the linked [headword](documentation/glossary?term=headword) (e.g., 'swim') which you can then use in the Entries endpoint. Unless specified using a region filter, the default lookup will be the Oxford Dictionary of English (GB).    <div id=\"dictionary_entries\"></div> 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.DictionaryEntriesApi()
source_lang = 'source_lang_example' # str | IANA language code
word_id = 'word_id_example' # str | An Entry identifier. Case-sensitive.
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Retrieve dictionary information for a given word
    api_response = api_instance.entries_source_lang_word_id_get(source_lang, word_id, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryEntriesApi->entries_source_lang_word_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **word_id** | **str**| An Entry identifier. Case-sensitive. | 
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

# **entries_source_lang_word_id_regionsregion_get**
> RetrieveEntry entries_source_lang_word_id_regionsregion_get(source_lang, word_id, region, app_id, app_key)

Specify GB or US dictionary for English entry search

 USe this filter to restrict the lookup to either our Oxford Dictionary of English (GB) or New Oxford American Dictionary (US). 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.DictionaryEntriesApi()
source_lang = 'source_lang_example' # str | IANA language code
word_id = 'word_id_example' # str | An Entry identifier. Case-sensitive.
region = 'region_example' # str | Region filter parameter. gb = Oxford Dictionary of English. us = New Oxford American Dictionary.
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Specify GB or US dictionary for English entry search
    api_response = api_instance.entries_source_lang_word_id_regionsregion_get(source_lang, word_id, region, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryEntriesApi->entries_source_lang_word_id_regionsregion_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **word_id** | **str**| An Entry identifier. Case-sensitive. | 
 **region** | **str**| Region filter parameter. gb &#x3D; Oxford Dictionary of English. us &#x3D; New Oxford American Dictionary. | 
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

