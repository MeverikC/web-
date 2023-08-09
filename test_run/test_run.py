import unittest
from Pms.src.common.HTMLTestRunner import HTMLTestRunner
from Pms.src.case.login_Testcase import login_Testcase
from Pms.src.case.roles_add_case import roles_add_case
from Pms.src.case.userManage_case import userManage_case_case
from Pms.src.case.menuManage_case import menuManage_case
from Pms.src.case.departmentM_case import departmentM_case
from Pms.src.case.dictionaryM_case import dictionaryM_case
from Pms.src.case.Per_C_case import Per_C_case
from Pms.src.case.home_case import home_case

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(login_Testcase))
suite.addTest(unittest.makeSuite(roles_add_case))
suite.addTest(unittest.makeSuite(userManage_case_case))
suite.addTest(unittest.makeSuite(menuManage_case))
suite.addTest(unittest.makeSuite(departmentM_case))
suite.addTest(unittest.makeSuite(dictionaryM_case))
suite.addTest(unittest.makeSuite(Per_C_case))
suite.addTest(unittest.makeSuite(home_case))
file=open('../reports/测试报告.html', 'wb')
runner= HTMLTestRunner(stream=file, title='干部绩效管理系统测试报告')
runner.run(suite)
file.close()


