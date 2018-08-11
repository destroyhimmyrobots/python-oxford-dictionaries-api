# oxford_dictionaries_api.WordlistApi

All URIs are relative to *https://od-api.oxforddictionaries.com:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wordlist_source_lang_filters_advanced_get**](WordlistApi.md#wordlist_source_lang_filters_advanced_get) | **GET** /wordlist/{source_lang}/{filters_advanced} | Retrieve list of words for category with advanced options
[**wordlist_source_lang_filters_basic_get**](WordlistApi.md#wordlist_source_lang_filters_basic_get) | **GET** /wordlist/{source_lang}/{filters_basic} | Retrieve a list of words in a category


# **wordlist_source_lang_filters_advanced_get**
> Wordlist wordlist_source_lang_filters_advanced_get(source_lang, filters_advanced, app_id, app_key, exclude=exclude, exclude_senses=exclude_senses, exclude_prime_senses=exclude_prime_senses, word_length=word_length, prefix=prefix, exact=exact, limit=limit, offset=offset)

Retrieve list of words for category with advanced options

Use this to apply more complex filters to the [list of words](documentation/glossary?term=wordlist). For example, you may only want to filter out words for which all [senses](documentation/glossary?term=sense) match the filter, or only its 'prime sense'. You can also filter by word length or match by substring (prefix).     <div id=\"wordlist_advanced\"></div> 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.WordlistApi()
source_lang = 'source_lang_example' # str | IANA language code
filters_advanced = 'filters_advanced_example' # str | Semicolon separated list of wordlist parameters, presented as value pairs: LexicalCategory, domains, regions, registers. Parameters can take comma separated list of values. E.g., lexicalCategory=noun,adjective;domains=sport. Number of values limited to 5.
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )
exclude = 'exclude_example' # str | Semicolon separated list of parameters-value pairs (same as filters). Excludes headwords that have any senses in specified exclusion attributes (lexical categories, domains, etc.) from results. (optional)
exclude_senses = 'exclude_senses_example' # str | Semicolon separated list of parameters-value pairs (same as filters). Excludes only those senses of a particular headword that match specified exclusion attributes (lexical categories, domains, etc.) from results but includes the headword if it has other permitted senses. (optional)
exclude_prime_senses = 'exclude_prime_senses_example' # str | Semicolon separated list of parameters-value pairs (same as filters). Excludes a headword only if the primary sense matches the specified exclusion attributes (registers, domains only). (optional)
word_length = '>5,<10' # str | Parameter to speficy the minimum (>), exact or maximum (<) length of the words required. E.g., >5 - more than 5 chars; <4 - less than 4 chars; >5<10 - from 5 to 10 chars; 3 - exactly 3 chars. (optional) (default to >5,<10)
prefix = 'goal' # str | Filter words that start with prefix parameter (optional) (default to goal)
exact = false # bool | If exact=true wordlist returns a list of entries that exactly matches the search string. Otherwise wordlist lists entries that start with prefix string. (optional) (default to false)
limit = 'limit_example' # str | Limit the number of results per response. Default and maximum limit is 5000. (optional)
offset = 'offset_example' # str | Offset the start number of the result. (optional)

try:
    # Retrieve list of words for category with advanced options
    api_response = api_instance.wordlist_source_lang_filters_advanced_get(source_lang, filters_advanced, app_id, app_key, exclude=exclude, exclude_senses=exclude_senses, exclude_prime_senses=exclude_prime_senses, word_length=word_length, prefix=prefix, exact=exact, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordlistApi->wordlist_source_lang_filters_advanced_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **filters_advanced** | **str**| Semicolon separated list of wordlist parameters, presented as value pairs: LexicalCategory, domains, regions, registers. Parameters can take comma separated list of values. E.g., lexicalCategory&#x3D;noun,adjective;domains&#x3D;sport. Number of values limited to 5. | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]
 **exclude** | **str**| Semicolon separated list of parameters-value pairs (same as filters). Excludes headwords that have any senses in specified exclusion attributes (lexical categories, domains, etc.) from results. | [optional] 
 **exclude_senses** | **str**| Semicolon separated list of parameters-value pairs (same as filters). Excludes only those senses of a particular headword that match specified exclusion attributes (lexical categories, domains, etc.) from results but includes the headword if it has other permitted senses. | [optional] 
 **exclude_prime_senses** | **str**| Semicolon separated list of parameters-value pairs (same as filters). Excludes a headword only if the primary sense matches the specified exclusion attributes (registers, domains only). | [optional] 
 **word_length** | **str**| Parameter to speficy the minimum (&gt;), exact or maximum (&lt;) length of the words required. E.g., &gt;5 - more than 5 chars; &lt;4 - less than 4 chars; &gt;5&lt;10 - from 5 to 10 chars; 3 - exactly 3 chars. | [optional] [default to &gt;5,&lt;10]
 **prefix** | **str**| Filter words that start with prefix parameter | [optional] [default to goal]
 **exact** | **bool**| If exact&#x3D;true wordlist returns a list of entries that exactly matches the search string. Otherwise wordlist lists entries that start with prefix string. | [optional] [default to false]
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

# **wordlist_source_lang_filters_basic_get**
> Wordlist wordlist_source_lang_filters_basic_get(source_lang, filters_basic, app_id, app_key, limit=limit, offset=offset)

Retrieve a list of words in a category

 Use this to retrieve a [list of words](documentation/glossary?term=wordlist) for particular [domain](documentation/glossary?term=domain), [lexical category](documentation/glossary?term=lexicalcategory), [register](documentation/glossary?term=registers) and/or [region](documentation/glossary?term=regions). View the full list of possible filters using the filters Utility endpoint.  The response only includes [headwords](documentation/glossary?term=headword), not all their possible [inflections](documentation/glossary?term=inflection). If you require a full [wordlist](documentation/glossary?term=wordlist) including [inflected forms](documentation/glossary?term=inflection), contact us and we can help.    <div id=\"wordlist\"></div> 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.WordlistApi()
source_lang = 'source_lang_example' # str | IANA language code
filters_basic = 'filters_basic_example' # str | Semicolon separated list of wordlist parameters, presented as value pairs: LexicalCategory, domains, regions, registers. Parameters can take comma separated list of values. E.g., lexicalCategory=noun,adjective;domains=sport. Number of values limited to 5.
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )
limit = 'limit_example' # str | Limit the number of results per response. Default and maximum limit is 5000. (optional)
offset = 'offset_example' # str | Offset the start number of the result (optional)

try:
    # Retrieve a list of words in a category
    api_response = api_instance.wordlist_source_lang_filters_basic_get(source_lang, filters_basic, app_id, app_key, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordlistApi->wordlist_source_lang_filters_basic_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **filters_basic** | **str**| Semicolon separated list of wordlist parameters, presented as value pairs: LexicalCategory, domains, regions, registers. Parameters can take comma separated list of values. E.g., lexicalCategory&#x3D;noun,adjective;domains&#x3D;sport. Number of values limited to 5. | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]
 **limit** | **str**| Limit the number of results per response. Default and maximum limit is 5000. | [optional] 
 **offset** | **str**| Offset the start number of the result | [optional] 

### Return type

[**Wordlist**](Wordlist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

