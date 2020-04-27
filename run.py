import unittest, os, HTMLTestReportCN

if __name__ == '__main__':
    path = os.path.abspath('.')
    suite = unittest.TestLoader().discover(start_dir=path + '/cases', pattern='*.py')
    # unittest.TextTestRunner().run(suite)
    fp = open(path+'./reports/report.html', 'wb')
    HTMLTestReportCN.HTMLTestRunner(stream=fp, title='仓库管理系统UI自动化测试报告5').run(suite)
    fp.close()
