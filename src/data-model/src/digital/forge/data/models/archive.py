# coding: utf-8
"""
This module provides a class for one of the models described by the API.
"""

from __future__ import absolute_import

from datetime import datetime

from digital.forge.data.models.base_model_ import Model
from digital.forge.data import util


class Archive(Model):
    """NOTE: This class is auto generated by OpenAPI Generator.

    (https://openapi-generator.tech)

    Do not edit the class manually.
    """

    openapi_types = {
        'uuid': str,
        'name': str,
        'description': str,
        'data_type': str,
        'units': str,
        'creation_time': datetime
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'description': 'description',
        'data_type': 'dataType',
        'units': 'units',
        'creation_time': 'creationTime'
    }

    def __init__(self, uuid=None, name=None, description=None, data_type=None, units=None, creation_time=None):  # noqa: E501
        """Archive - a model defined in OpenAPI

        :param uuid: The uuid of this Archive.  # noqa: E501
        :type uuid: str
        :param name: The name of this Archive.  # noqa: E501
        :type name: str
        :param description: The description of this Archive.  # noqa: E501
        :type description: str
        :param data_type: The data_type of this Archive.  # noqa: E501
        :type data_type: str
        :param units: The units of this Archive.  # noqa: E501
        :type units: str
        :param creation_time: The creation_time of this Archive.  # noqa: E501
        :type creation_time: datetime
        """

        if uuid is None:
            raise ValueError('`uuid` is a required value')
        self._uuid = uuid
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
        if creation_time is None:
            raise ValueError('`creation_time` is a required value')
        self._creation_time = creation_time

    @classmethod
    def from_dict(cls, dikt) -> 'Archive':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Archive of this Archive.  # noqa: E501
        :rtype: Archive
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uuid(self):
        """Gets the uuid of this Archive.

        A unique identifier for the archive.  # noqa: E501

        :return: The uuid of this Archive.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Archive.

        A unique identifier for the archive.  # noqa: E501

        :param uuid: The uuid of this Archive.
        :type uuid: str
        """

        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")

        if uuid is not None and not isinstance(uuid, str):
            raise ValueError("Invalid value for `uuid`, must be a `str`")

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this Archive.

        A human readable name for the archive.  # noqa: E501

        :return: The name of this Archive.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Archive.

        A human readable name for the archive.  # noqa: E501

        :param name: The name of this Archive.
        :type name: str
        """

        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        if name is not None and not isinstance(name, str):
            raise ValueError("Invalid value for `name`, must be a `str`")

        self._name = name

    @property
    def description(self):
        """Gets the description of this Archive.

        A description of the archive.  # noqa: E501

        :return: The description of this Archive.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Archive.

        A description of the archive.  # noqa: E501

        :param description: The description of this Archive.
        :type description: str
        """

        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        if description is not None and not isinstance(description, str):
            raise ValueError("Invalid value for `description`, must be a `str`")

        self._description = description

    @property
    def data_type(self):
        """Gets the data_type of this Archive.

        The type of data retained in the archive, e.g., integer or float.  # noqa: E501

        :return: The data_type of this Archive.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this Archive.

        The type of data retained in the archive, e.g., integer or float.  # noqa: E501

        :param data_type: The data_type of this Archive.
        :type data_type: str
        """

        if data_type is None:
            raise ValueError("Invalid value for `data_type`, must not be `None`")

        if data_type is not None and not isinstance(data_type, str):
            raise ValueError("Invalid value for `data_type`, must be a `str`")

        self._data_type = data_type

    @property
    def units(self):
        """Gets the units of this Archive.

        The units for the data retained in the archive.  # noqa: E501

        :return: The units of this Archive.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this Archive.

        The units for the data retained in the archive.  # noqa: E501

        :param units: The units of this Archive.
        :type units: str
        """

        if units is None:
            raise ValueError("Invalid value for `units`, must not be `None`")

        if units is not None and not isinstance(units, str):
            raise ValueError("Invalid value for `units`, must be a `str`")

        self._units = units

    @property
    def creation_time(self):
        """Gets the creation_time of this Archive.

        The date the archive was created or initialized.  # noqa: E501

        :return: The creation_time of this Archive.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Archive.

        The date the archive was created or initialized.  # noqa: E501

        :param creation_time: The creation_time of this Archive.
        :type creation_time: datetime
        """

        if creation_time is None:
            raise ValueError("Invalid value for `creation_time`, must not be `None`")

        if creation_time is not None and not isinstance(creation_time, datetime):
            raise ValueError("Invalid value for `creation_time`, must be a `datetime`")

        self._creation_time = creation_time
