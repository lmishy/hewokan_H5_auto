#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/19

import pytest
import allure
import urllib
from bs4 import BeautifulSoup


@allure.step("签到页面")
def test_qiandao():
    try:
        url = "http://m.china-plus.net/interface/appSign/appSigntest.php"
        res = urllib.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        test_result = soup.title.string
        print test_result
    except Exception as e:
        print e
        raise Exception('H5页面请求出错，请检查！')

    assert res.getcode() == 200
    assert u'签到' in test_result


if __name__ == "__main__":
    # test_qiandao()
    pytest.main()