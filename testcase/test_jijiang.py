#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/19

import pytest
import allure
import urllib
from bs4 import BeautifulSoup


@allure.step("爱看-即将上线")
def test_jijiang():
    try:
        url = "http://html5.china-plus.net/xct.html"
        res = urllib.urlopen(url)
    except Exception as e:
        print e
        raise Exception('H5页面请求出错，请检查！')

    assert res.getcode() == 200



if __name__ == "__main__":
    test_jijiang()
    # pytest.main()