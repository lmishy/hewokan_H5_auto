#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/19

import pytest
import allure
import urllib
from bs4 import BeautifulSoup


@allure.step("移动用户登录页面")
def test_yidong():
    try:
        url = "http://wap.sc.10086.cn/wap/rwybxl.html"
        res = urllib.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        test_result = soup.title.string
        print test_result
    except Exception as e:
        print e
        raise Exception('H5页面请求出错，请检查！')

    assert res.getcode() == 200
    assert u'用户登录' == test_result


if __name__ == "__main__":
    # test_yidong()
    pytest.main()