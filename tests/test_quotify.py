import unittest
from notif import send_notification

class NotifTestCase(unittest.TestCase):
    def test_send_notification(self):
        result = send_notification("Hello, World!")
        self.assertTrue(result)
        # Add additional assertions to validate the result of the send_notification function

if __name__ == '__main__':
    unittest.main()
