# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from oxford_dictionaries_api.models.examples_list import ExamplesList  # noqa: F401,E501
from oxford_dictionaries_api.models.grammatical_features_list import GrammaticalFeaturesList  # noqa: F401,E501


class SentencesLexicalEntry(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'grammatical_features': 'GrammaticalFeaturesList',
        'language': 'str',
        'lexical_category': 'str',
        'sentences': 'ExamplesList',
        'text': 'str'
    }

    attribute_map = {
        'grammatical_features': 'grammaticalFeatures',
        'language': 'language',
        'lexical_category': 'lexicalCategory',
        'sentences': 'sentences',
        'text': 'text'
    }

    def __init__(self, grammatical_features=None, language=None, lexical_category=None, sentences=None, text=None):  # noqa: E501
        """SentencesLexicalEntry - a model defined in Swagger"""  # noqa: E501

        self._grammatical_features = None
        self._language = None
        self._lexical_category = None
        self._sentences = None
        self._text = None
        self.discriminator = None

        if grammatical_features is not None:
            self.grammatical_features = grammatical_features
        self.language = language
        if lexical_category is not None:
            self.lexical_category = lexical_category
        self.sentences = sentences
        self.text = text

    @property
    def grammatical_features(self):
        """Gets the grammatical_features of this SentencesLexicalEntry.  # noqa: E501


        :return: The grammatical_features of this SentencesLexicalEntry.  # noqa: E501
        :rtype: GrammaticalFeaturesList
        """
        return self._grammatical_features

    @grammatical_features.setter
    def grammatical_features(self, grammatical_features):
        """Sets the grammatical_features of this SentencesLexicalEntry.


        :param grammatical_features: The grammatical_features of this SentencesLexicalEntry.  # noqa: E501
        :type: GrammaticalFeaturesList
        """

        self._grammatical_features = grammatical_features

    @property
    def language(self):
        """Gets the language of this SentencesLexicalEntry.  # noqa: E501

        IANA language code  # noqa: E501

        :return: The language of this SentencesLexicalEntry.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SentencesLexicalEntry.

        IANA language code  # noqa: E501

        :param language: The language of this SentencesLexicalEntry.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def lexical_category(self):
        """Gets the lexical_category of this SentencesLexicalEntry.  # noqa: E501

        A linguistic category of words (or more precisely lexical items), generally defined by the syntactic or morphological behaviour of the lexical item in question, such as noun or verb  # noqa: E501

        :return: The lexical_category of this SentencesLexicalEntry.  # noqa: E501
        :rtype: str
        """
        return self._lexical_category

    @lexical_category.setter
    def lexical_category(self, lexical_category):
        """Sets the lexical_category of this SentencesLexicalEntry.

        A linguistic category of words (or more precisely lexical items), generally defined by the syntactic or morphological behaviour of the lexical item in question, such as noun or verb  # noqa: E501

        :param lexical_category: The lexical_category of this SentencesLexicalEntry.  # noqa: E501
        :type: str
        """

        self._lexical_category = lexical_category

    @property
    def sentences(self):
        """Gets the sentences of this SentencesLexicalEntry.  # noqa: E501

        A list of examples of use sentences  # noqa: E501

        :return: The sentences of this SentencesLexicalEntry.  # noqa: E501
        :rtype: ExamplesList
        """
        return self._sentences

    @sentences.setter
    def sentences(self, sentences):
        """Sets the sentences of this SentencesLexicalEntry.

        A list of examples of use sentences  # noqa: E501

        :param sentences: The sentences of this SentencesLexicalEntry.  # noqa: E501
        :type: ExamplesList
        """
        if sentences is None:
            raise ValueError("Invalid value for `sentences`, must not be `None`")  # noqa: E501

        self._sentences = sentences

    @property
    def text(self):
        """Gets the text of this SentencesLexicalEntry.  # noqa: E501

        A given written or spoken realisation of a an entry.  # noqa: E501

        :return: The text of this SentencesLexicalEntry.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SentencesLexicalEntry.

        A given written or spoken realisation of a an entry.  # noqa: E501

        :param text: The text of this SentencesLexicalEntry.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SentencesLexicalEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
