from Pms.src.common.Per_C import Per_C
import unittest

class Per_C_case(unittest.TestCase):
    def setUp(self):
        self.Per_C=Per_C()
    def test_06(self):
        now_url=self.Per_C.test_Per_C()
        self.assertEqual(True, now_url)
        print('text06 successful!')