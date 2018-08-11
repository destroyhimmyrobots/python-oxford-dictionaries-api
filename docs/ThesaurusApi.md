# oxford_dictionaries_api.ThesaurusApi

All URIs are relative to *https://od-api.oxforddictionaries.com:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entries_source_lang_word_id_antonyms_get**](ThesaurusApi.md#entries_source_lang_word_id_antonyms_get) | **GET** /entries/{source_lang}/{word_id}/antonyms | Retrieve words that mean the opposite
[**entries_source_lang_word_id_synonyms_get**](ThesaurusApi.md#entries_source_lang_word_id_synonyms_get) | **GET** /entries/{source_lang}/{word_id}/synonyms | Retrieve words that are similar
[**entries_source_lang_word_id_synonymsantonyms_get**](ThesaurusApi.md#entries_source_lang_word_id_synonymsantonyms_get) | **GET** /entries/{source_lang}/{word_id}/synonyms;antonyms | Retrieve synonyms and antonyms for a given word


# **entries_source_lang_word_id_antonyms_get**
> Thesaurus entries_source_lang_word_id_antonyms_get(source_lang, word_id, app_id, app_key)

Retrieve words that mean the opposite

 Retrieve words that are opposite in meaning to the input word ([antonym](documentation/glossary?term=thesaurus)).    <div id=\"antonyms\"></div> 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.ThesaurusApi()
source_lang = 'source_lang_example' # str | IANA language code
word_id = 'word_id_example' # str | An Entry identifier. Case-sensitive.
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Retrieve words that mean the opposite
    api_response = api_instance.entries_source_lang_word_id_antonyms_get(source_lang, word_id, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThesaurusApi->entries_source_lang_word_id_antonyms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **word_id** | **str**| An Entry identifier. Case-sensitive. | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**Thesaurus**](Thesaurus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entries_source_lang_word_id_synonyms_get**
> Thesaurus entries_source_lang_word_id_synonyms_get(source_lang, word_id, app_id, app_key)

Retrieve words that are similar

 Use this to retrieve words that are similar in meaning to the input word ([synonym](documentation/glossary?term=synonym)).    <div id=\"synonyms\"></div> 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.ThesaurusApi()
source_lang = 'source_lang_example' # str | IANA language code
word_id = 'word_id_example' # str | An Entry identifier. Case-sensitive.
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Retrieve words that are similar
    api_response = api_instance.entries_source_lang_word_id_synonyms_get(source_lang, word_id, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThesaurusApi->entries_source_lang_word_id_synonyms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **word_id** | **str**| An Entry identifier. Case-sensitive. | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**Thesaurus**](Thesaurus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entries_source_lang_word_id_synonymsantonyms_get**
> Thesaurus entries_source_lang_word_id_synonymsantonyms_get(source_lang, word_id, app_id, app_key)

Retrieve synonyms and antonyms for a given word

 Retrieve available [synonyms](documentation/glossary?term=thesaurus) and [antonyms](documentation/glossary?term=thesaurus) for a given word and language.     <div id=\"synonyms_and_antonyms\"></div> 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.ThesaurusApi()
source_lang = 'source_lang_example' # str | IANA language code
word_id = 'word_id_example' # str | An Entry identifier. Case-sensitive.
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Retrieve synonyms and antonyms for a given word
    api_response = api_instance.entries_source_lang_word_id_synonymsantonyms_get(source_lang, word_id, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThesaurusApi->entries_source_lang_word_id_synonymsantonyms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_lang** | **str**| IANA language code | 
 **word_id** | **str**| An Entry identifier. Case-sensitive. | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**Thesaurus**](Thesaurus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

