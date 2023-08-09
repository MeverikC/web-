import unittest
from parameterized import parameterized
from Pms.src.common.user_login import user_login

class login_Testcase(unittest.TestCase):
    #初始化
    def setUp(self):
        #实例化
        self.login=user_login()
    @parameterized.expand([('admin','admin123'),('admin','iuabvav'),('cavhy','aiucsvbg')])
    def test_01(self,a,b):
        login_jg=self.login.test_login(a,b)
        self.assertEqual(True,login_jg)