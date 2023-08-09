from Pms.src.common.roles_add import roles_add
import unittest

class roles_add_case(unittest.TestCase):
    def setUp(self):
        self.roles_add=roles_add()
    def test_01(self):
        now_url=self.roles_add.roles_add_test()
        self.assertEqual(True,now_url)
        print('test01 OK')