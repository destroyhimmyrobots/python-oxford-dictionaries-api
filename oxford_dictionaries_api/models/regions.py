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


class Regions(object):
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
        'metadata': 'object',
        'results': 'dict(str, Arrayofstrings)'
    }

    attribute_map = {
        'metadata': 'metadata',
        'results': 'results'
    }

    def __init__(self, metadata=None, results=None):  # noqa: E501
        """Regions - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._results = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if results is not None:
            self.results = results

    @property
    def metadata(self):
        """Gets the metadata of this Regions.  # noqa: E501

        Additional Information provided by OUP  # noqa: E501

        :return: The metadata of this Regions.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Regions.

        Additional Information provided by OUP  # noqa: E501

        :param metadata: The metadata of this Regions.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def results(self):
        """Gets the results of this Regions.  # noqa: E501

        A mapping of regions available.  # noqa: E501

        :return: The results of this Regions.  # noqa: E501
        :rtype: dict(str, Arrayofstrings)
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this Regions.

        A mapping of regions available.  # noqa: E501

        :param results: The results of this Regions.  # noqa: E501
        :type: dict(str, Arrayofstrings)
        """

        self._results = results

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
        if not isinstance(other, Regions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other