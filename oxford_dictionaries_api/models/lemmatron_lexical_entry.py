# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from oxford_dictionaries_api.models.grammatical_features_list import GrammaticalFeaturesList  # noqa: F401,E501
from oxford_dictionaries_api.models.inflections_list import InflectionsList  # noqa: F401,E501


class LemmatronLexicalEntry(object):
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
        'inflection_of': 'InflectionsList',
        'language': 'str',
        'lexical_category': 'str',
        'text': 'str'
    }

    attribute_map = {
        'grammatical_features': 'grammaticalFeatures',
        'inflection_of': 'inflectionOf',
        'language': 'language',
        'lexical_category': 'lexicalCategory',
        'text': 'text'
    }

    def __init__(self, grammatical_features=None, inflection_of=None, language=None, lexical_category=None, text=None):  # noqa: E501
        """LemmatronLexicalEntry - a model defined in Swagger"""  # noqa: E501

        self._grammatical_features = None
        self._inflection_of = None
        self._language = None
        self._lexical_category = None
        self._text = None
        self.discriminator = None

        if grammatical_features is not None:
            self.grammatical_features = grammatical_features
        self.inflection_of = inflection_of
        self.language = language
        self.lexical_category = lexical_category
        self.text = text

    @property
    def grammatical_features(self):
        """Gets the grammatical_features of this LemmatronLexicalEntry.  # noqa: E501


        :return: The grammatical_features of this LemmatronLexicalEntry.  # noqa: E501
        :rtype: GrammaticalFeaturesList
        """
        return self._grammatical_features

    @grammatical_features.setter
    def grammatical_features(self, grammatical_features):
        """Sets the grammatical_features of this LemmatronLexicalEntry.


        :param grammatical_features: The grammatical_features of this LemmatronLexicalEntry.  # noqa: E501
        :type: GrammaticalFeaturesList
        """

        self._grammatical_features = grammatical_features

    @property
    def inflection_of(self):
        """Gets the inflection_of of this LemmatronLexicalEntry.  # noqa: E501

        The canonical form of words for which the entry is an inflection  # noqa: E501

        :return: The inflection_of of this LemmatronLexicalEntry.  # noqa: E501
        :rtype: InflectionsList
        """
        return self._inflection_of

    @inflection_of.setter
    def inflection_of(self, inflection_of):
        """Sets the inflection_of of this LemmatronLexicalEntry.

        The canonical form of words for which the entry is an inflection  # noqa: E501

        :param inflection_of: The inflection_of of this LemmatronLexicalEntry.  # noqa: E501
        :type: InflectionsList
        """
        if inflection_of is None:
            raise ValueError("Invalid value for `inflection_of`, must not be `None`")  # noqa: E501

        self._inflection_of = inflection_of

    @property
    def language(self):
        """Gets the language of this LemmatronLexicalEntry.  # noqa: E501

        IANA language code  # noqa: E501

        :return: The language of this LemmatronLexicalEntry.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this LemmatronLexicalEntry.

        IANA language code  # noqa: E501

        :param language: The language of this LemmatronLexicalEntry.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def lexical_category(self):
        """Gets the lexical_category of this LemmatronLexicalEntry.  # noqa: E501

        A linguistic category of words (or more precisely lexical items), generally defined by the syntactic or morphological behaviour of the lexical item in question, such as noun or verb  # noqa: E501

        :return: The lexical_category of this LemmatronLexicalEntry.  # noqa: E501
        :rtype: str
        """
        return self._lexical_category

    @lexical_category.setter
    def lexical_category(self, lexical_category):
        """Sets the lexical_category of this LemmatronLexicalEntry.

        A linguistic category of words (or more precisely lexical items), generally defined by the syntactic or morphological behaviour of the lexical item in question, such as noun or verb  # noqa: E501

        :param lexical_category: The lexical_category of this LemmatronLexicalEntry.  # noqa: E501
        :type: str
        """
        if lexical_category is None:
            raise ValueError("Invalid value for `lexical_category`, must not be `None`")  # noqa: E501

        self._lexical_category = lexical_category

    @property
    def text(self):
        """Gets the text of this LemmatronLexicalEntry.  # noqa: E501

        A given written or spoken realisation of a an entry.  # noqa: E501

        :return: The text of this LemmatronLexicalEntry.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this LemmatronLexicalEntry.

        A given written or spoken realisation of a an entry.  # noqa: E501

        :param text: The text of this LemmatronLexicalEntry.  # noqa: E501
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
        if not isinstance(other, LemmatronLexicalEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
