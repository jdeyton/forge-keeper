# coding: utf-8
"""
This module provides a class for one of the models described by the API.
"""

from __future__ import absolute_import


from digital.forge.data.models.base_model_ import Model
from digital.forge.data import util


class ArchiveInputs(Model):
    """NOTE: This class is auto generated by OpenAPI Generator.

    (https://openapi-generator.tech)

    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, data_type=None, units=None):  # noqa: E501
        """ArchiveInputs - a model defined in OpenAPI

        :param name: The name of this ArchiveInputs.  # noqa: E501
        :type name: str
        :param description: The description of this ArchiveInputs.  # noqa: E501
        :type description: str
        :param data_type: The data_type of this ArchiveInputs.  # noqa: E501
        :type data_type: str
        :param units: The units of this ArchiveInputs.  # noqa: E501
        :type units: str
        """
        self.openapi_types = {
            'name': str,
            'description': str,
            'data_type': str,
            'units': str
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'data_type': 'dataType',
            'units': 'units'
        }

        if name is None:
            raise ValueError('`name` is a required value')
        self._name = name
        if description is None:
            raise ValueError('`description` is a required value')
        self._description = description
        if data_type is None:
            raise ValueError('`data_type` is a required value')
        self._data_type = data_type
        if units is None:
            raise ValueError('`units` is a required value')
        self._units = units

    @classmethod
    def from_dict(cls, dikt) -> 'ArchiveInputs':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ArchiveInputs of this ArchiveInputs.  # noqa: E501
        :rtype: ArchiveInputs
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ArchiveInputs.

        A human readable name for the archive.  # noqa: E501

        :return: The name of this ArchiveInputs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArchiveInputs.

        A human readable name for the archive.  # noqa: E501

        :param name: The name of this ArchiveInputs.
        :type name: str
        """

        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        if name is not None and not isinstance(name, str):
            raise ValueError("Invalid value for `name`, must be a `str`")

        self._name = name

    @property
    def description(self):
        """Gets the description of this ArchiveInputs.

        A description of the archive.  # noqa: E501

        :return: The description of this ArchiveInputs.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ArchiveInputs.

        A description of the archive.  # noqa: E501

        :param description: The description of this ArchiveInputs.
        :type description: str
        """

        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        if description is not None and not isinstance(description, str):
            raise ValueError("Invalid value for `description`, must be a `str`")

        self._description = description

    @property
    def data_type(self):
        """Gets the data_type of this ArchiveInputs.

        The type of data retained in the archive, e.g., integer or float.  # noqa: E501

        :return: The data_type of this ArchiveInputs.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ArchiveInputs.

        The type of data retained in the archive, e.g., integer or float.  # noqa: E501

        :param data_type: The data_type of this ArchiveInputs.
        :type data_type: str
        """

        if data_type is None:
            raise ValueError("Invalid value for `data_type`, must not be `None`")

        if data_type is not None and not isinstance(data_type, str):
            raise ValueError("Invalid value for `data_type`, must be a `str`")

        self._data_type = data_type

    @property
    def units(self):
        """Gets the units of this ArchiveInputs.

        The units for the data retained in the archive.  # noqa: E501

        :return: The units of this ArchiveInputs.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this ArchiveInputs.

        The units for the data retained in the archive.  # noqa: E501

        :param units: The units of this ArchiveInputs.
        :type units: str
        """

        if units is None:
            raise ValueError("Invalid value for `units`, must not be `None`")

        if units is not None and not isinstance(units, str):
            raise ValueError("Invalid value for `units`, must be a `str`")

        self._units = units