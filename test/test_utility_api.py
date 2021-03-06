# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import oxford_dictionaries_api
from oxford_dictionaries_api.api.utility_api import UtilityApi  # noqa: E501
from oxford_dictionaries_api.rest import ApiException


class TestUtilityApi(unittest.TestCase):
    """UtilityApi unit test stubs"""

    def setUp(self):
        self.api = oxford_dictionaries_api.api.utility_api.UtilityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_domains_source_domains_language_target_domains_language_get(self):
        """Test case for domains_source_domains_language_target_domains_language_get

        Lists available domains in a bilingual dataset  # noqa: E501
        """
        pass

    def test_domains_source_language_get(self):
        """Test case for domains_source_language_get

        Lists available domains in a monolingual dataset  # noqa: E501
        """
        pass

    def test_filters_endpoint_get(self):
        """Test case for filters_endpoint_get

        Lists available filters for specific endpoint  # noqa: E501
        """
        pass

    def test_filters_get(self):
        """Test case for filters_get

        Lists available filters  # noqa: E501
        """
        pass

    def test_grammatical_features_source_language_get(self):
        """Test case for grammatical_features_source_language_get

        Lists available grammatical features in a dataset  # noqa: E501
        """
        pass

    def test_languages_get(self):
        """Test case for languages_get

        Lists available dictionaries  # noqa: E501
        """
        pass

    def test_lexicalcategories_language_get(self):
        """Test case for lexicalcategories_language_get

        Lists available lexical categories in a dataset  # noqa: E501
        """
        pass

    def test_regions_source_language_get(self):
        """Test case for regions_source_language_get

        Lists available regions in a monolingual dataset  # noqa: E501
        """
        pass

    def test_registers_source_language_get(self):
        """Test case for registers_source_language_get

        Lists available registers in a  monolingual dataset  # noqa: E501
        """
        pass

    def test_registers_source_register_language_target_register_language_get(self):
        """Test case for registers_source_register_language_target_register_language_get

        Lists available registers in a bilingual dataset  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
