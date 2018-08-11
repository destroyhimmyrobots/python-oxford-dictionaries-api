# oxford_dictionaries_api.UtilityApi

All URIs are relative to *https://od-api.oxforddictionaries.com:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domains_source_domains_language_target_domains_language_get**](UtilityApi.md#domains_source_domains_language_target_domains_language_get) | **GET** /domains/{source_domains_language}/{target_domains_language} | Lists available domains in a bilingual dataset
[**domains_source_language_get**](UtilityApi.md#domains_source_language_get) | **GET** /domains/{source_language} | Lists available domains in a monolingual dataset
[**filters_endpoint_get**](UtilityApi.md#filters_endpoint_get) | **GET** /filters/{endpoint} | Lists available filters for specific endpoint
[**filters_get**](UtilityApi.md#filters_get) | **GET** /filters | Lists available filters
[**grammatical_features_source_language_get**](UtilityApi.md#grammatical_features_source_language_get) | **GET** /grammaticalFeatures/{source_language} | Lists available grammatical features in a dataset
[**languages_get**](UtilityApi.md#languages_get) | **GET** /languages | Lists available dictionaries
[**lexicalcategories_language_get**](UtilityApi.md#lexicalcategories_language_get) | **GET** /lexicalcategories/{language} | Lists available lexical categories in a dataset
[**regions_source_language_get**](UtilityApi.md#regions_source_language_get) | **GET** /regions/{source_language} | Lists available regions in a monolingual dataset
[**registers_source_language_get**](UtilityApi.md#registers_source_language_get) | **GET** /registers/{source_language} | Lists available registers in a  monolingual dataset
[**registers_source_register_language_target_register_language_get**](UtilityApi.md#registers_source_register_language_target_register_language_get) | **GET** /registers/{source_register_language}/{target_register_language} | Lists available registers in a bilingual dataset


# **domains_source_domains_language_target_domains_language_get**
> UtilityLabels domains_source_domains_language_target_domains_language_get(source_domains_language, target_domains_language, app_id, app_key)

Lists available domains in a bilingual dataset

Returns a list of the available [domains](documentation/glossary?term=domain) for a given bilingual language dataset. 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.UtilityApi()
source_domains_language = 'source_domains_language_example' # str | IANA language code
target_domains_language = 'target_domains_language_example' # str | IANA language code
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Lists available domains in a bilingual dataset
    api_response = api_instance.domains_source_domains_language_target_domains_language_get(source_domains_language, target_domains_language, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->domains_source_domains_language_target_domains_language_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_domains_language** | **str**| IANA language code | 
 **target_domains_language** | **str**| IANA language code | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**UtilityLabels**](UtilityLabels.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_source_language_get**
> UtilityLabels domains_source_language_get(source_language, app_id, app_key)

Lists available domains in a monolingual dataset

Returns a list of the available [domains](documentation/glossary?term=domain) for a given monolingual language dataset. 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.UtilityApi()
source_language = 'source_language_example' # str | IANA language code
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Lists available domains in a monolingual dataset
    api_response = api_instance.domains_source_language_get(source_language, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->domains_source_language_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_language** | **str**| IANA language code | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**UtilityLabels**](UtilityLabels.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filters_endpoint_get**
> Filters filters_endpoint_get(endpoint, app_id, app_key)

Lists available filters for specific endpoint

Returns a list of all the valid filters for a given endpoint to construct API calls. 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.UtilityApi()
endpoint = 'endpoint_example' # str | Name of the endpoint.
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Lists available filters for specific endpoint
    api_response = api_instance.filters_endpoint_get(endpoint, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->filters_endpoint_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**| Name of the endpoint. | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**Filters**](Filters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filters_get**
> Filters filters_get(app_id, app_key)

Lists available filters

Returns a list of all the valid filters to construct API calls. 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.UtilityApi()
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Lists available filters
    api_response = api_instance.filters_get(app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->filters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**Filters**](Filters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grammatical_features_source_language_get**
> UtilityLabels grammatical_features_source_language_get(source_language, app_id, app_key)

Lists available grammatical features in a dataset

Returns a list of the available [grammatical features](documentation/glossary?term=grammaticalfeatures) for a given language dataset. 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.UtilityApi()
source_language = 'source_language_example' # str | IANA language code. If provided output will be filtered by sourceLanguage.
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Lists available grammatical features in a dataset
    api_response = api_instance.grammatical_features_source_language_get(source_language, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->grammatical_features_source_language_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_language** | **str**| IANA language code. If provided output will be filtered by sourceLanguage. | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**UtilityLabels**](UtilityLabels.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **languages_get**
> Languages languages_get(app_id, app_key, source_language=source_language, target_language=target_language)

Lists available dictionaries

Returns a list of monolingual and bilingual language datasets available in the API 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.UtilityApi()
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )
source_language = 'source_language_example' # str | IANA language code. If provided output will be filtered by sourceLanguage. (optional)
target_language = 'target_language_example' # str | IANA language code. If provided output will be filtered by sourceLanguage. (optional)

try:
    # Lists available dictionaries
    api_response = api_instance.languages_get(app_id, app_key, source_language=source_language, target_language=target_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->languages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]
 **source_language** | **str**| IANA language code. If provided output will be filtered by sourceLanguage. | [optional] 
 **target_language** | **str**| IANA language code. If provided output will be filtered by sourceLanguage. | [optional] 

### Return type

[**Languages**](Languages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lexicalcategories_language_get**
> UtilityLabels lexicalcategories_language_get(language, app_id, app_key)

Lists available lexical categories in a dataset

Returns a list of available [lexical categories](documentation/glossary?term=lexicalcategory) for a given language dataset. 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.UtilityApi()
language = 'language_example' # str | IANA language code
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Lists available lexical categories in a dataset
    api_response = api_instance.lexicalcategories_language_get(language, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->lexicalcategories_language_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| IANA language code | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**UtilityLabels**](UtilityLabels.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regions_source_language_get**
> Regions regions_source_language_get(source_language, app_id, app_key)

Lists available regions in a monolingual dataset

Returns a list of the available [regions](documentation/glossary?term=regions) for a given monolingual language dataset. 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.UtilityApi()
source_language = 'source_language_example' # str | IANA language code
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Lists available regions in a monolingual dataset
    api_response = api_instance.regions_source_language_get(source_language, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->regions_source_language_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_language** | **str**| IANA language code | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**Regions**](Regions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registers_source_language_get**
> UtilityLabels registers_source_language_get(source_language, app_id, app_key)

Lists available registers in a  monolingual dataset

Returns a list of the available [registers](documentation/glossary?term=registers) for a given monolingual language dataset. 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.UtilityApi()
source_language = 'source_language_example' # str | IANA language code
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Lists available registers in a  monolingual dataset
    api_response = api_instance.registers_source_language_get(source_language, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->registers_source_language_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_language** | **str**| IANA language code | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**UtilityLabels**](UtilityLabels.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registers_source_register_language_target_register_language_get**
> UtilityLabels registers_source_register_language_target_register_language_get(source_register_language, target_register_language, app_id, app_key)

Lists available registers in a bilingual dataset

Returns a list of the available [registers](documentation/glossary?term=registers) for a given bilingual language dataset. 

### Example
```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oxford_dictionaries_api.UtilityApi()
source_register_language = 'source_register_language_example' # str | IANA language code
target_register_language = 'target_register_language_example' # str | IANA language code
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Lists available registers in a bilingual dataset
    api_response = api_instance.registers_source_register_language_target_register_language_get(source_register_language, target_register_language, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->registers_source_register_language_target_register_language_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_register_language** | **str**| IANA language code | 
 **target_register_language** | **str**| IANA language code | 
 **app_id** | **str**| App ID Authentication Parameter | [default to ]
 **app_key** | **str**| App Key Authentication Parameter | [default to ]

### Return type

[**UtilityLabels**](UtilityLabels.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

