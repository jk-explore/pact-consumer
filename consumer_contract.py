import atexit
import unittest

from pact import Consumer, Provider
from consumer import get_user

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
            result = get_user(1, 'http://localhost:1234')

        self.assertEqual(result, expected)
        #requests.put('http://192.168.99.100/pacts/provider/UsersProvider/consumer/UsersConsumer/latest', )


pact = Consumer('UsersConsumer').has_pact_with(Provider('UsersProvider'), port=1234)
pact.start_service()
unittest.main()
atexit.register(pact.stop_service)