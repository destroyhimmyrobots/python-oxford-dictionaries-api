# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import oxford_dictionaries_api
from oxford_dictionaries_api.api.the_sentence_dictionary_api import TheSentenceDictionaryApi  # noqa: E501
from oxford_dictionaries_api.rest import ApiException


class TestTheSentenceDictionaryApi(unittest.TestCase):
    """TheSentenceDictionaryApi unit test stubs"""

    def setUp(self):
        self.api = oxford_dictionaries_api.api.the_sentence_dictionary_api.TheSentenceDictionaryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_entries_source_language_word_id_sentences_get(self):
        """Test case for entries_source_language_word_id_sentences_get

        Retrieve corpus sentences for a given word  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
