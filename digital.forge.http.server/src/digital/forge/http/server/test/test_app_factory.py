import flask
import sys
import unittest
from unittest.mock import Mock, call

from ..app_decorator import AppDecorator
from ..app_factory import AppFactory


class TestAppFactory(unittest.TestCase):
    
    def test_add_valid_decorator(self):
        '''
        Valid decorators should be added to the internal list.
        '''
        factory = AppFactory()
        self.assertListEqual(
            factory._decorators,
            []
        )
        
        decorator = AppDecorator()
        decorator2 = AppDecorator()
        
        factory.add_decorator(decorator)
        self.assertListEqual(
            factory._decorators,
            [decorator]
        )
        
        factory.add_decorator(decorator2)
        self.assertListEqual(
            factory._decorators,
            [decorator, decorator2]
        )
        
        factory.add_decorator(decorator)
        self.assertListEqual(
            factory._decorators,
            [decorator, decorator2, decorator]
        )
    
    def test_add_invalid_decorator(self):
        '''
        Invalid decorators should throw exceptions when added.
        '''
        factory = AppFactory()
        
        with self.assertRaises(ValueError):
            factory.add_decorator(None)
        
        with self.assertRaises(ValueError):
            factory.add_decorator('protomolecule')
        
        self.assertListEqual(
            factory._decorators,
            []
        )

    def test_create_app(self):
        '''
        Creating an app should return a Flask app with the input name.
        '''
        factory = AppFactory()
        
        app = factory.create_app('Detective Miller')
        
        self.assertIsInstance(app, flask.Flask)
        self.assertEquals('Detective Miller', app.name)
    
    def test_create_app_with_invalid_name(self):
        '''
        Creating an app with an invalid name should raise an exception.
        '''
        factory = AppFactory()
        
        with self.assertRaises(ValueError):
            factory.create_app(None)
    
    def test_create_decorated_app(self):
        '''
        Creating an app with decorators should call the decorator function on
        each added decorator (including duplicates) in the order they were
        added.
        '''
        factory = AppFactory()
        
        decorate1 = Mock(name='decorate')
        decorate2 = Mock(name='decorate')
        
        decorator1 = AppDecorator()
        decorator2 = AppDecorator()
        
        decorator1.decorate = decorate1
        decorator2.decorate = decorate2
        
        manager = Mock()
        manager.attach_mock(decorate1, 'alex_kamal')
        manager.attach_mock(decorate2, 'amos_burton')
        
        factory.add_decorator(decorator1)
        factory.add_decorator(decorator2)
        factory.add_decorator(decorator1)  # duplicate is OK!
        
        app = factory.create_app('Rocinante')
        
        decorate1.assert_called_with(app)
        decorate2.assert_called_once_with(app)
        self.assertListEqual(
            manager.mock_calls,
            [call.alex_kamal(app), call.amos_burton(app), call.alex_kamal(app)]
        )
    
    def test_start_app(self):
        '''
        Starting an app should start up a server using the app with the input
        (or default) host and port.
        '''
        factory = AppFactory()
        factory.add_decorator(AppDecorator())
        app = factory.create_app('James Holden')
        app.run = Mock(name='run')
        
        factory.start_app(app)
        
        app.run.assert_called_once()
    
    def test_start_app_with_host_and_port(self):
        '''
        Starting an app should start up a server using the app with the input
        (or default) host and port.
        '''
        factory = AppFactory()
        factory.add_decorator(AppDecorator())
        app = factory.create_app('James Holden')
        app.run = Mock(name='run')
        
        for host, port in [
            (None,          None),
            (None,          1337),
            ('127.0.0.1',   None),
            ('localhost',   8080),
            ('0.0.0.0',     8081),
            ('192.168.0.1', 54321),
            ('outer.space', 65432),
        ]:
            msg = 'Valid host/port: '
            msg += 'None' if host is None else host
            msg += ', '
            msg += 'None' if port is None else str(port)
            print(msg, file=sys.stderr)
            factory.start_app(app)
            app.run.assert_called_once()
            # TODO - Check the host and port.
            app.run.reset_mock()
    
    def test_start_invalid_app(self):
        '''
        Starting an invalid app object should raise an exception.
        '''
        factory = AppFactory()
        
        with self.assertRaises(ValueError):
            factory.start_app(None)
        
        with self.assertRaises(ValueError):
            factory.start_app('Star Helix')
    
    def test_start_app_with_bad_host_or_port(self):
        '''
        Starting an app with an invalid host/port should raise an exception.
        '''
        factory = AppFactory()
        factory.add_decorator(AppDecorator())
        app = factory.create_app('Naomi Nagata')
        app.run = Mock(name='run')
        
        for host, port in [
                ('',              None),
                ('.',             None),
                ('256.0.0.0',     None),
                ('192.168.0.-1',  None),
                ('192.168.256.0', None),
                ('#$%!)(|2',      None),
                (None,            -1),
                (None,            0),
                (None,            65536),
                (None,            3.14),
            ]:
            msg = 'Invalid host/port: '
            msg += 'None' if host is None else host
            msg += ', '
            msg += 'None' if port is None else str(port)
            print(msg, file=sys.stderr)
            with self.assertRaises(ValueError):
                factory.start_app(app, host, port)
        
    
