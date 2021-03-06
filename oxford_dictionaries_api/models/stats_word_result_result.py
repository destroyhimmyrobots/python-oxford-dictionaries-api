# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StatsWordResultResult(object):
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
        'frequency': 'int',
        'lemma': 'str',
        'lexical_category': 'str',
        'match_count': 'int',
        'normalized_frequency': 'int',
        'true_case': 'str',
        'wordform': 'str'
    }

    attribute_map = {
        'frequency': 'frequency',
        'lemma': 'lemma',
        'lexical_category': 'lexicalCategory',
        'match_count': 'matchCount',
        'normalized_frequency': 'normalizedFrequency',
        'true_case': 'trueCase',
        'wordform': 'wordform'
    }

    def __init__(self, frequency=None, lemma=None, lexical_category=None, match_count=None, normalized_frequency=None, true_case=None, wordform=None):  # noqa: E501
        """StatsWordResultResult - a model defined in Swagger"""  # noqa: E501

        self._frequency = None
        self._lemma = None
        self._lexical_category = None
        self._match_count = None
        self._normalized_frequency = None
        self._true_case = None
        self._wordform = None
        self.discriminator = None

        self.frequency = frequency
        if lemma is not None:
            self.lemma = lemma
        if lexical_category is not None:
            self.lexical_category = lexical_category
        self.match_count = match_count
        self.normalized_frequency = normalized_frequency
        if true_case is not None:
            self.true_case = true_case
        if wordform is not None:
            self.wordform = wordform

    @property
    def frequency(self):
        """Gets the frequency of this StatsWordResultResult.  # noqa: E501

        The number of times a word appears in the entire corpus  # noqa: E501

        :return: The frequency of this StatsWordResultResult.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this StatsWordResultResult.

        The number of times a word appears in the entire corpus  # noqa: E501

        :param frequency: The frequency of this StatsWordResultResult.  # noqa: E501
        :type: int
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501

        self._frequency = frequency

    @property
    def lemma(self):
        """Gets the lemma of this StatsWordResultResult.  # noqa: E501

        A lemma of the word (e.g., wordforms \"lay\", \"laid\" and \"laying\" have all lemma \"lay\")  # noqa: E501

        :return: The lemma of this StatsWordResultResult.  # noqa: E501
        :rtype: str
        """
        return self._lemma

    @lemma.setter
    def lemma(self, lemma):
        """Sets the lemma of this StatsWordResultResult.

        A lemma of the word (e.g., wordforms \"lay\", \"laid\" and \"laying\" have all lemma \"lay\")  # noqa: E501

        :param lemma: The lemma of this StatsWordResultResult.  # noqa: E501
        :type: str
        """

        self._lemma = lemma

    @property
    def lexical_category(self):
        """Gets the lexical_category of this StatsWordResultResult.  # noqa: E501

        A lexical category such as 'verb' or 'noun'  # noqa: E501

        :return: The lexical_category of this StatsWordResultResult.  # noqa: E501
        :rtype: str
        """
        return self._lexical_category

    @lexical_category.setter
    def lexical_category(self, lexical_category):
        """Sets the lexical_category of this StatsWordResultResult.

        A lexical category such as 'verb' or 'noun'  # noqa: E501

        :param lexical_category: The lexical_category of this StatsWordResultResult.  # noqa: E501
        :type: str
        """

        self._lexical_category = lexical_category

    @property
    def match_count(self):
        """Gets the match_count of this StatsWordResultResult.  # noqa: E501

        The number of database records that matched the query params (stated frequency is the sum of the individual frequencies)  # noqa: E501

        :return: The match_count of this StatsWordResultResult.  # noqa: E501
        :rtype: int
        """
        return self._match_count

    @match_count.setter
    def match_count(self, match_count):
        """Sets the match_count of this StatsWordResultResult.

        The number of database records that matched the query params (stated frequency is the sum of the individual frequencies)  # noqa: E501

        :param match_count: The match_count of this StatsWordResultResult.  # noqa: E501
        :type: int
        """
        if match_count is None:
            raise ValueError("Invalid value for `match_count`, must not be `None`")  # noqa: E501

        self._match_count = match_count

    @property
    def normalized_frequency(self):
        """Gets the normalized_frequency of this StatsWordResultResult.  # noqa: E501

        The number of times a word appears on average in 1 million words  # noqa: E501

        :return: The normalized_frequency of this StatsWordResultResult.  # noqa: E501
        :rtype: int
        """
        return self._normalized_frequency

    @normalized_frequency.setter
    def normalized_frequency(self, normalized_frequency):
        """Sets the normalized_frequency of this StatsWordResultResult.

        The number of times a word appears on average in 1 million words  # noqa: E501

        :param normalized_frequency: The normalized_frequency of this StatsWordResultResult.  # noqa: E501
        :type: int
        """
        if normalized_frequency is None:
            raise ValueError("Invalid value for `normalized_frequency`, must not be `None`")  # noqa: E501

        self._normalized_frequency = normalized_frequency

    @property
    def true_case(self):
        """Gets the true_case of this StatsWordResultResult.  # noqa: E501

        A given written realisation of a an entry (e.g., \"lay\") usually lower case  # noqa: E501

        :return: The true_case of this StatsWordResultResult.  # noqa: E501
        :rtype: str
        """
        return self._true_case

    @true_case.setter
    def true_case(self, true_case):
        """Sets the true_case of this StatsWordResultResult.

        A given written realisation of a an entry (e.g., \"lay\") usually lower case  # noqa: E501

        :param true_case: The true_case of this StatsWordResultResult.  # noqa: E501
        :type: str
        """

        self._true_case = true_case

    @property
    def wordform(self):
        """Gets the wordform of this StatsWordResultResult.  # noqa: E501

        A given written realisation of a an entry (e.g., \"Lay\") preserving case  # noqa: E501

        :return: The wordform of this StatsWordResultResult.  # noqa: E501
        :rtype: str
        """
        return self._wordform

    @wordform.setter
    def wordform(self, wordform):
        """Sets the wordform of this StatsWordResultResult.

        A given written realisation of a an entry (e.g., \"Lay\") preserving case  # noqa: E501

        :param wordform: The wordform of this StatsWordResultResult.  # noqa: E501
        :type: str
        """

        self._wordform = wordform

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
        if not isinstance(other, StatsWordResultResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
