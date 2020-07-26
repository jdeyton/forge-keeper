# coding: utf-8
"""
This module provides a class for one of the models described by the API.
"""

from __future__ import absolute_import


from digital.forge.data.models.base_model_ import Model
from digital.forge.data import util


class ErrorResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator.

    (https://openapi-generator.tech)

    Do not edit the class manually.
    """

    def __init__(self, code=None, message=None):  # noqa: E501
        """ErrorResponse - a model defined in OpenAPI

        :param code: The code of this ErrorResponse.  # noqa: E501
        :type code: int
        :param message: The message of this ErrorResponse.  # noqa: E501
        :type message: str
        """
        self.openapi_types = {
            'code': int,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        if code is None:
            raise ValueError('`code` is a required value')
        self._code = code
        if message is None:
            raise ValueError('`message` is a required value')
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'ErrorResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ErrorResponse of this ErrorResponse.  # noqa: E501
        :rtype: ErrorResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this ErrorResponse.

        An error code corresponding to some internal state of the server.  # noqa: E501

        :return: The code of this ErrorResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorResponse.

        An error code corresponding to some internal state of the server.  # noqa: E501

        :param code: The code of this ErrorResponse.
        :type code: int
        """

        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        if code is not None and not isinstance(code, int):
            raise ValueError("Invalid value for `code`, must be a `int`")

        self._code = code

    @property
    def message(self):
        """Gets the message of this ErrorResponse.

        A human-readable message explaining the error code or what went wrong.  # noqa: E501

        :return: The message of this ErrorResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorResponse.

        A human-readable message explaining the error code or what went wrong.  # noqa: E501

        :param message: The message of this ErrorResponse.
        :type message: str
        """

        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        if message is not None and not isinstance(message, str):
            raise ValueError("Invalid value for `message`, must be a `str`")

        self._message = message