##安装配置 ：1、python2.7
           2、下载allure2 报告生成工具 附链接（https://bintray.com/qameta/generic/allure2/2.6.0）

##安装相关包： 1、pytest
             2、pytest-allure-adaptor
             3、urllib
             4、BeautifulSoup

##运行
1、在pycham等编辑器，直接右键运行即可

2、pyth 命令运行：cd hewokan
                 py.test testcase/ --alluredir report/

3、结合jenkins运行：构建一个git/svn项目，构建后操作添加allure report,点击构建即可


##查看报告：
1、命令运行完之后，运行命令allure generate report/ -o report/html 生成报告，进入report/html文件夹点击index.html即可查看相关报告

2、构建完成之后，点击构建项目右侧图标即可查看相关报告