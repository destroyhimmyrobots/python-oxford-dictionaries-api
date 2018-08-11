# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from oxford_dictionaries_api.models.arrayofstrings import Arrayofstrings  # noqa: F401,E501


class ArrayOfRelatedEntriesInner(object):
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
        'domains': 'Arrayofstrings',
        'id': 'str',
        'language': 'str',
        'regions': 'Arrayofstrings',
        'registers': 'Arrayofstrings',
        'text': 'str'
    }

    attribute_map = {
        'domains': 'domains',
        'id': 'id',
        'language': 'language',
        'regions': 'regions',
        'registers': 'registers',
        'text': 'text'
    }

    def __init__(self, domains=None, id=None, language=None, regions=None, registers=None, text=None):  # noqa: E501
        """ArrayOfRelatedEntriesInner - a model defined in Swagger"""  # noqa: E501

        self._domains = None
        self._id = None
        self._language = None
        self._regions = None
        self._registers = None
        self._text = None
        self.discriminator = None

        if domains is not None:
            self.domains = domains
        self.id = id
        if language is not None:
            self.language = language
        if regions is not None:
            self.regions = regions
        if registers is not None:
            self.registers = registers
        self.text = text

    @property
    def domains(self):
        """Gets the domains of this ArrayOfRelatedEntriesInner.  # noqa: E501

        A subject, discipline, or branch of knowledge particular to the Sense  # noqa: E501

        :return: The domains of this ArrayOfRelatedEntriesInner.  # noqa: E501
        :rtype: Arrayofstrings
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this ArrayOfRelatedEntriesInner.

        A subject, discipline, or branch of knowledge particular to the Sense  # noqa: E501

        :param domains: The domains of this ArrayOfRelatedEntriesInner.  # noqa: E501
        :type: Arrayofstrings
        """

        self._domains = domains

    @property
    def id(self):
        """Gets the id of this ArrayOfRelatedEntriesInner.  # noqa: E501

        The identifier of the word  # noqa: E501

        :return: The id of this ArrayOfRelatedEntriesInner.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArrayOfRelatedEntriesInner.

        The identifier of the word  # noqa: E501

        :param id: The id of this ArrayOfRelatedEntriesInner.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def language(self):
        """Gets the language of this ArrayOfRelatedEntriesInner.  # noqa: E501

        IANA language code specifying the language of the word  # noqa: E501

        :return: The language of this ArrayOfRelatedEntriesInner.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ArrayOfRelatedEntriesInner.

        IANA language code specifying the language of the word  # noqa: E501

        :param language: The language of this ArrayOfRelatedEntriesInner.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def regions(self):
        """Gets the regions of this ArrayOfRelatedEntriesInner.  # noqa: E501

        A particular area in which the pronunciation occurs, e.g. 'Great Britain'  # noqa: E501

        :return: The regions of this ArrayOfRelatedEntriesInner.  # noqa: E501
        :rtype: Arrayofstrings
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ArrayOfRelatedEntriesInner.

        A particular area in which the pronunciation occurs, e.g. 'Great Britain'  # noqa: E501

        :param regions: The regions of this ArrayOfRelatedEntriesInner.  # noqa: E501
        :type: Arrayofstrings
        """

        self._regions = regions

    @property
    def registers(self):
        """Gets the registers of this ArrayOfRelatedEntriesInner.  # noqa: E501

        A level of language usage, typically with respect to formality. e.g. 'offensive', 'informal'  # noqa: E501

        :return: The registers of this ArrayOfRelatedEntriesInner.  # noqa: E501
        :rtype: Arrayofstrings
        """
        return self._registers

    @registers.setter
    def registers(self, registers):
        """Sets the registers of this ArrayOfRelatedEntriesInner.

        A level of language usage, typically with respect to formality. e.g. 'offensive', 'informal'  # noqa: E501

        :param registers: The registers of this ArrayOfRelatedEntriesInner.  # noqa: E501
        :type: Arrayofstrings
        """

        self._registers = registers

    @property
    def text(self):
        """Gets the text of this ArrayOfRelatedEntriesInner.  # noqa: E501


        :return: The text of this ArrayOfRelatedEntriesInner.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ArrayOfRelatedEntriesInner.


        :param text: The text of this ArrayOfRelatedEntriesInner.  # noqa: E501
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
        if not isinstance(other, ArrayOfRelatedEntriesInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other