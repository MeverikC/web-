from Pms.src.common.menuManage import menuManage
import unittest

class menuManage_case(unittest.TestCase):
    def setUp(self):
        self.menuManage=menuManage()
    def test_03(self):
        now_url=self.menuManage.test_menuManage()
        self.assertEqual(True, now_url)
        print('test03 successful!')