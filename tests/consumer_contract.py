import atexit
import unittest

from pact import Consumer, Provider

pact = Consumer('UsersConsumer').has_pact_with(Provider('UsersProvider'), port=8080)
pact.start_service()
atexit.register(pact.stop_service)


class GetUserInfoContract(unittest.TestCase):
    def test_get_user(self):
        expected = {
            "username": "admin",
            "email": "admin@dev.net"
        }

        (pact
         .given('admin exists and is not an administrator')
         .upon_receiving('a request for admin')
         .with_request('get', '/users/1')
         .will_respond_with(200, body=expected))

        with pact:
            result = consumer.get_user('admin', 'http://localhost:1235')

        self.assertEqual(result, expected)
        #requests.put('http://192.168.99.100/pacts/provider/UsersProvider/consumer/UsersConsumer/latest', )