# coding: utf-8
"""
This module provides the base class for a Flask app decorator.
"""


class Decorator:
    '''
    A base class for decorating a Flask app with additional features.

    Some basic decorators are provided. To add more, you must sub-class this
    class.
    '''

    def decorate(self, app):
        """
        Concrete sub-classes are expected to implement this method.
        """
