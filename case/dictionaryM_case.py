from Pms.src.common.dictionaryM import dictionaryM
import unittest

class dictionaryM_case(unittest.TestCase):
    def setUp(self):
        self.dictionaryM=dictionaryM()
    def test_05(self):
        now_url=self.dictionaryM.test_dictionaryM()
        self.assertEqual(True, now_url)
        print('text05 successful!')