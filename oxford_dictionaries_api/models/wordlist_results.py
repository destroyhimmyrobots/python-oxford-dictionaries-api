# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WordlistResults(object):
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
        'id': 'str',
        'match_type': 'str',
        'region': 'str',
        'word': 'str'
    }

    attribute_map = {
        'id': 'id',
        'match_type': 'matchType',
        'region': 'region',
        'word': 'word'
    }

    def __init__(self, id=None, match_type=None, region=None, word=None):  # noqa: E501
        """WordlistResults - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._match_type = None
        self._region = None
        self._word = None
        self.discriminator = None

        self.id = id
        if match_type is not None:
            self.match_type = match_type
        if region is not None:
            self.region = region
        self.word = word

    @property
    def id(self):
        """Gets the id of this WordlistResults.  # noqa: E501

        The identifier of a word  # noqa: E501

        :return: The id of this WordlistResults.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WordlistResults.

        The identifier of a word  # noqa: E501

        :param id: The id of this WordlistResults.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def match_type(self):
        """Gets the match_type of this WordlistResults.  # noqa: E501


        :return: The match_type of this WordlistResults.  # noqa: E501
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this WordlistResults.


        :param match_type: The match_type of this WordlistResults.  # noqa: E501
        :type: str
        """

        self._match_type = match_type

    @property
    def region(self):
        """Gets the region of this WordlistResults.  # noqa: E501

        Name of region.  # noqa: E501

        :return: The region of this WordlistResults.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this WordlistResults.

        Name of region.  # noqa: E501

        :param region: The region of this WordlistResults.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def word(self):
        """Gets the word of this WordlistResults.  # noqa: E501

        A given written or spoken realisation of a an entry, lowercased.  # noqa: E501

        :return: The word of this WordlistResults.  # noqa: E501
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        """Sets the word of this WordlistResults.

        A given written or spoken realisation of a an entry, lowercased.  # noqa: E501

        :param word: The word of this WordlistResults.  # noqa: E501
        :type: str
        """
        if word is None:
            raise ValueError("Invalid value for `word`, must not be `None`")  # noqa: E501

        self._word = word

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
        if not isinstance(other, WordlistResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
