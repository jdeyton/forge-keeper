# coding: utf-8
"""
    Forge Keeper - Conductor

    This API focuses on managing data archives and drones that submit data to them.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: not@vailable
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

from datetime import datetime
import unittest

from digital.forge.data.models.drone import Drone


class TestDrone(unittest.TestCase):
    """Drone unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @staticmethod
    def make_instance():
        """Returns an instance with example values as defined in the API."""
        return Drone(
            uuid='8b9aed83-ed5a-47bf-a02a-8530369d545d',
            name='Server room',
            description='Monitors temperature in the server room.',
            creation_time='2020-07-25T17:35:14Z'
        )

    def test_drone(self):
        """Test Drone"""
        instance = TestDrone.make_instance()
        self.assertEqual('8b9aed83-ed5a-47bf-a02a-8530369d545d', instance.uuid)
        self.assertEqual('Server room', instance.name)
        self.assertEqual(
            'Monitors temperature in the server room.',
            instance.description
        )
        self.assertEqual('2020-07-25T17:35:14Z', instance.creation_time)

    def test_uuid(self):
        """Test the "uuid" property"""
        instance = TestDrone.make_instance()

        # This value can't be set to null.
        with self.assertRaises(
                ValueError,
                msg='uuid cannot be set to null'
        ):
            instance.uuid = None

        # Check some valid values.
        valid_values = [
            '3674b8a6-dd3e-4ef9-bb8a-443c4103e5cc',
            'f3d3a9ce-42a1-4223-a723-ae9c67d017ce',
        ]
        for value in valid_values:
            instance.uuid = value
            self.assertEqual(
                value,
                instance.uuid,
                msg='uuid can be set to valid value "%r"' % (value)
            )

        # Check some invalid values raise ValueError exceptions.
        invalid_values = [
            -1,
            [],
            {},
        ]
        for value in invalid_values:
            with self.assertRaises(
                    ValueError,
                    msg='uuid cannot be set to an invalid value'
            ):
                instance.uuid = value

    def test_name(self):
        """Test the "name" property"""
        instance = TestDrone.make_instance()

        # This value can't be set to null.
        with self.assertRaises(
                ValueError,
                msg='name cannot be set to null'
        ):
            instance.name = None

        # Check some valid values.
        valid_values = [
            'Fili',
            'Kili',
            'Oin',
            'Gloin',
        ]
        for value in valid_values:
            instance.name = value
            self.assertEqual(
                value,
                instance.name,
                msg='name can be set to valid value "%r"' % (value)
            )

        # Check some invalid values raise ValueError exceptions.
        invalid_values = [
            9001,
            [],
            {},
        ]
        for value in invalid_values:
            with self.assertRaises(
                    ValueError,
                    msg='name cannot be set to an invalid value'
            ):
                instance.name = value

    def test_description(self):
        """Test the "description" property"""
        instance = TestDrone.make_instance()

        # This value can't be set to null.
        with self.assertRaises(
                ValueError,
                msg='description cannot be set to null'
        ):
            instance.description = None

        # Check some valid values.
        valid_values = [
            'That\'s what Bilbo Baggins hates!',
            'So carefully! Carefully with the plates!',
            '',
        ]
        for value in valid_values:
            instance.description = value
            self.assertEqual(
                value,
                instance.description,
                msg='description can be set to valid value "%r"' % (value)
            )

        # Check some invalid values raise ValueError exceptions.
        invalid_values = [
            123456789,
            [],
            {},
        ]
        for value in invalid_values:
            with self.assertRaises(
                    ValueError,
                    msg='description cannot be set to an invalid value'
            ):
                instance.description = value

    def test_creation_time(self):
        """Test the "creation_time" property"""
        instance = TestDrone.make_instance()

        # This value can't be set to null.
        with self.assertRaises(
                ValueError,
                msg='creation_time cannot be set to null'
        ):
            instance.creation_time = None

        # Check some valid values.
        valid_values = [
            datetime(2063, 4, 5),
            datetime(2157, 1, 1, 12, 34, 56),
        ]
        for value in valid_values:
            instance.creation_time = value
            self.assertEqual(
                value,
                instance.creation_time,
                msg='creation_time can be set to valid value "%r"' % (value)
            )

        # Check some invalid values raise ValueError exceptions.
        invalid_values = [
            'long ago',
            'there and back again',
            410,
            [],
            {},
        ]
        for value in invalid_values:
            with self.assertRaises(
                    ValueError,
                    msg='creation_time cannot be set to an invalid value'
            ):
                instance.creation_time = value

    def test_equals(self):
        """Test equality operations"""
        obj_a = TestDrone.make_instance()
        obj_b = TestDrone.make_instance()
        obj_c = TestDrone.make_instance()

        # Create a different object.
        obj_x = TestDrone.make_instance()
        obj_x.name = 'Beorn'

        self.assertEqual(obj_a, obj_a, msg='Reflexive property: a == a')
        self.assertEqual(obj_a, obj_b, msg='Symmetric property: a == b')
        self.assertEqual(obj_b, obj_a, msg='Symmetric property: b == a')
        self.assertEqual(obj_b, obj_c, msg='Transitive property: b == c')
        self.assertEqual(obj_a, obj_c, msg='Transitive property: a == c')

        self.assertNotEqual(obj_a, obj_x, msg='Not equals: a != x')

        self.assertNotEqual(obj_a, 'foobar', msg='The object is not a string')
        self.assertNotEqual(obj_a, None, msg='The object is not null')


if __name__ == '__main__':
    unittest.main()
