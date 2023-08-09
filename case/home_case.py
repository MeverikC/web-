from Pms.src.common.home import home
import unittest

class home_case(unittest.TestCase):
    def setUp(self):
        home().mjh_home()
    def test_09(self):
        now_url = home().mjh_home()
        self.assertEqual(True, now_url)
        print('text09 successful!')