# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from oxford_dictionaries_api.api_client import ApiClient


class SearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_source_lang_get(self, source_lang, app_id, app_key, **kwargs):  # noqa: E501
        """Retrieve possible matches to input  # noqa: E501

         Use this to retrieve possible [headword](documentation/glossary?term=headword) matches for a given string of text. The results are culculated using headword matching, fuzzy matching, and [lemmatization](documentation/glossary?term=lemma)     <div id=\"search\"></div>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_source_lang_get(source_lang, app_id, app_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str source_lang: IANA language code (required)
        :param str app_id: App ID Authentication Parameter (required)
        :param str app_key: App Key Authentication Parameter (required)
        :param str q: Search string
        :param bool prefix: Set prefix to true if you'd like to get results only starting with search string.
        :param str regions: If searching in English, filter words with specific region(s) either 'us' or 'gb'.
        :param str limit: Limit the number of results per response. Default and maximum limit is 5000.
        :param str offset: Offset the start number of the result.
        :return: Wordlist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_source_lang_get_with_http_info(source_lang, app_id, app_key, **kwargs)  # noqa: E501
        else:
            (data) = self.search_source_lang_get_with_http_info(source_lang, app_id, app_key, **kwargs)  # noqa: E501
            return data

    def search_source_lang_get_with_http_info(self, source_lang, app_id, app_key, **kwargs):  # noqa: E501
        """Retrieve possible matches to input  # noqa: E501

         Use this to retrieve possible [headword](documentation/glossary?term=headword) matches for a given string of text. The results are culculated using headword matching, fuzzy matching, and [lemmatization](documentation/glossary?term=lemma)     <div id=\"search\"></div>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_source_lang_get_with_http_info(source_lang, app_id, app_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str source_lang: IANA language code (required)
        :param str app_id: App ID Authentication Parameter (required)
        :param str app_key: App Key Authentication Parameter (required)
        :param str q: Search string
        :param bool prefix: Set prefix to true if you'd like to get results only starting with search string.
        :param str regions: If searching in English, filter words with specific region(s) either 'us' or 'gb'.
        :param str limit: Limit the number of results per response. Default and maximum limit is 5000.
        :param str offset: Offset the start number of the result.
        :return: Wordlist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_lang', 'app_id', 'app_key', 'q', 'prefix', 'regions', 'limit', 'offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_source_lang_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_lang' is set
        if ('source_lang' not in params or
                params['source_lang'] is None):
            raise ValueError("Missing the required parameter `source_lang` when calling `search_source_lang_get`")  # noqa: E501
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params or
                params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `search_source_lang_get`")  # noqa: E501
        # verify the required parameter 'app_key' is set
        if ('app_key' not in params or
                params['app_key'] is None):
            raise ValueError("Missing the required parameter `app_key` when calling `search_source_lang_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source_lang' in params:
            path_params['source_lang'] = params['source_lang']  # noqa: E501

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'prefix' in params:
            query_params.append(('prefix', params['prefix']))  # noqa: E501
        if 'regions' in params:
            query_params.append(('regions', params['regions']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}
        if 'app_id' in params:
            header_params['app_id'] = params['app_id']  # noqa: E501
        if 'app_key' in params:
            header_params['app_key'] = params['app_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/search/{source_lang}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Wordlist',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_source_search_language_translationstarget_search_language_get(self, source_search_language, target_search_language, app_id, app_key, **kwargs):  # noqa: E501
        """Retrieve possible translation matches to input  # noqa: E501

         Use this to find matches in our translation dictionaries.    <div id=\"search_translation\"></div>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_source_search_language_translationstarget_search_language_get(source_search_language, target_search_language, app_id, app_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str source_search_language: IANA language code (required)
        :param str target_search_language: IANA language code (required)
        :param str app_id: App ID Authentication Parameter (required)
        :param str app_key: App Key Authentication Parameter (required)
        :param str q: Search string.
        :param bool prefix: Set prefix to true if you'd like to get results only starting with search string.
        :param str regions: Filter words with specific region(s) E.g., regions=us. For now gb, us are available for en language.
        :param str limit: Limit the number of results per response. Default and maximum limit is 5000.
        :param str offset: Offset the start number of the result.
        :return: Wordlist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_source_search_language_translationstarget_search_language_get_with_http_info(source_search_language, target_search_language, app_id, app_key, **kwargs)  # noqa: E501
        else:
            (data) = self.search_source_search_language_translationstarget_search_language_get_with_http_info(source_search_language, target_search_language, app_id, app_key, **kwargs)  # noqa: E501
            return data

    def search_source_search_language_translationstarget_search_language_get_with_http_info(self, source_search_language, target_search_language, app_id, app_key, **kwargs):  # noqa: E501
        """Retrieve possible translation matches to input  # noqa: E501

         Use this to find matches in our translation dictionaries.    <div id=\"search_translation\"></div>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_source_search_language_translationstarget_search_language_get_with_http_info(source_search_language, target_search_language, app_id, app_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str source_search_language: IANA language code (required)
        :param str target_search_language: IANA language code (required)
        :param str app_id: App ID Authentication Parameter (required)
        :param str app_key: App Key Authentication Parameter (required)
        :param str q: Search string.
        :param bool prefix: Set prefix to true if you'd like to get results only starting with search string.
        :param str regions: Filter words with specific region(s) E.g., regions=us. For now gb, us are available for en language.
        :param str limit: Limit the number of results per response. Default and maximum limit is 5000.
        :param str offset: Offset the start number of the result.
        :return: Wordlist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_search_language', 'target_search_language', 'app_id', 'app_key', 'q', 'prefix', 'regions', 'limit', 'offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_source_search_language_translationstarget_search_language_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_search_language' is set
        if ('source_search_language' not in params or
                params['source_search_language'] is None):
            raise ValueError("Missing the required parameter `source_search_language` when calling `search_source_search_language_translationstarget_search_language_get`")  # noqa: E501
        # verify the required parameter 'target_search_language' is set
        if ('target_search_language' not in params or
                params['target_search_language'] is None):
            raise ValueError("Missing the required parameter `target_search_language` when calling `search_source_search_language_translationstarget_search_language_get`")  # noqa: E501
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params or
                params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `search_source_search_language_translationstarget_search_language_get`")  # noqa: E501
        # verify the required parameter 'app_key' is set
        if ('app_key' not in params or
                params['app_key'] is None):
            raise ValueError("Missing the required parameter `app_key` when calling `search_source_search_language_translationstarget_search_language_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source_search_language' in params:
            path_params['source_search_language'] = params['source_search_language']  # noqa: E501
        if 'target_search_language' in params:
            path_params['target_search_language'] = params['target_search_language']  # noqa: E501

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'prefix' in params:
            query_params.append(('prefix', params['prefix']))  # noqa: E501
        if 'regions' in params:
            query_params.append(('regions', params['regions']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}
        if 'app_id' in params:
            header_params['app_id'] = params['app_id']  # noqa: E501
        if 'app_key' in params:
            header_params['app_key'] = params['app_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/search/{source_search_language}/translations={target_search_language}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Wordlist',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)