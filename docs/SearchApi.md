# oxford_dictionaries_api.SearchApi

All URIs are relative to *https://od-api.oxforddictionaries.com:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_source_lang_get**](SearchApi.md#search_source_lang_get) | **GET** /search/{source_lang} | Retrieve possible matches to input
[**search_source_search_language_translationstarget_search_language_get**](SearchApi.md#search_source_search_language_translationstarget_search_language_get) | **GET** /search/{source_search_language}/translations&#x3D;{target_search_language} | Retrieve possible translation matches to input


# **search_source_lang_get**
> Wordlist search_source_lang_get(source_lang, app_id, app_key, q=q, prefix=prefix, regions=regions, limit=limit, offset=offset)

Retrieve possible matches to input

 Use this to retrieve possible [headword](documentation/glossary?term=headword) matches for a given string of text. The results are culculated using headword matching, fuzzy matching, and [lemmatization](documentation/glossary?term=lemma)     <div id=\"search\"></div> 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.SearchApi()
source_lang = 'source_lang_example' # str | IANA language code
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )
q = 'eye' # str | Search string (optional) (default to eye)
prefix = false # bool | Set prefix to true if you'd like to get results only starting with search string. (optional) (default to false)
regions = 'regions_example' # str | If searching in English, filter words with specific region(s) either 'us' or 'gb'. (optional)
limit = 'limit_example' # str | Limit the number of results per response. Default and maximum limit is 5000. (optional)
offset = 'offset_example' # str | Offset the start number of the result. (optional)

try:
    # Retrieve possible matches to input
    api_response = api_instance.search_source_lang_get(source_lang, app_id, app_key, q=q, prefix=prefix, regions=regions, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_source_lang_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]
 **q** | **str**| Search string | [optional] [default to eye]
 **prefix** | **bool**| Set prefix to true if you&#39;d like to get results only starting with search string. | [optional] [default to false]
 **regions** | **str**| If searching in English, filter words with specific region(s) either &#39;us&#39; or &#39;gb&#39;. | [optional] 
 **limit** | **str**| Limit the number of results per response. Default and maximum limit is 5000. | [optional] 
 **offset** | **str**| Offset the start number of the result. | [optional] 

### Return type

[**Wordlist**](Wordlist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_source_search_language_translationstarget_search_language_get**
> Wordlist search_source_search_language_translationstarget_search_language_get(source_search_language, target_search_language, app_id, app_key, q=q, prefix=prefix, regions=regions, limit=limit, offset=offset)

Retrieve possible translation matches to input

 Use this to find matches in our translation dictionaries.    <div id=\"search_translation\"></div> 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.SearchApi()
source_search_language = 'source_search_language_example' # str | IANA language code
target_search_language = 'target_search_language_example' # str | IANA language code
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )
q = 'eye' # str | Search string. (optional) (default to eye)
prefix = false # bool | Set prefix to true if you'd like to get results only starting with search string. (optional) (default to false)
regions = 'regions_example' # str | Filter words with specific region(s) E.g., regions=us. For now gb, us are available for en language. (optional)
limit = 'limit_example' # str | Limit the number of results per response. Default and maximum limit is 5000. (optional)
offset = 'offset_example' # str | Offset the start number of the result. (optional)

try:
    # Retrieve possible translation matches to input
    api_response = api_instance.search_source_search_language_translationstarget_search_language_get(source_search_language, target_search_language, app_id, app_key, q=q, prefix=prefix, regions=regions, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_source_search_language_translationstarget_search_language_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_search_language** | **str**| IANA language code | 
 **target_search_language** | **str**| IANA language code | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]
 **q** | **str**| Search string. | [optional] [default to eye]
 **prefix** | **bool**| Set prefix to true if you&#39;d like to get results only starting with search string. | [optional] [default to false]
 **regions** | **str**| Filter words with specific region(s) E.g., regions&#x3D;us. For now gb, us are available for en language. | [optional] 
 **limit** | **str**| Limit the number of results per response. Default and maximum limit is 5000. | [optional] 
 **offset** | **str**| Offset the start number of the result. | [optional] 

### Return type

[**Wordlist**](Wordlist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

