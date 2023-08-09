from Pms.src.common.userManage import userManage
import unittest

class userManage_case_case(unittest.TestCase):
    def setUp(self):
        self.userManage=userManage()
    def test_02(self):
        now_url=self.userManage.test_Manage()
        self.assertEqual(True,now_url)
        print('test02 successful!')