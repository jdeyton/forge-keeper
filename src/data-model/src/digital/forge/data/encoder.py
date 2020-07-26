# coding: utf-8
"""
This module provides a class for encoding API model objects to JSON.
"""
import json
import six

from digital.forge.data.models.base_model_ import Model


class JSONEncoder(json.JSONEncoder):
    """
    A JSONEncoder implementation for API model objects.

    This class is automatically generated! **DO NOT TOUCH!**
    """
    include_nulls = False

    def default(self, o):
        if isinstance(o, Model):
            dikt = {}
            for attr, _ in six.iteritems(o.openapi_types):
                value = getattr(o, attr)
                if value is None and not self.include_nulls:
                    continue
                attr = o.attribute_map[attr]
                dikt[attr] = value
            return dikt
        return json.JSONEncoder.default(self, o)
