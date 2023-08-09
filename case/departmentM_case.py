from Pms.src.common.departmentM import departmentM

import unittest

class departmentM_case(unittest.TestCase):
    def setUp(self):
        self.departmentM=departmentM()
    def test_04(self):
        now_url=self.departmentM.test_departmentM()
        self.assertEqual(True,now_url)
        print('text04 successful!')
