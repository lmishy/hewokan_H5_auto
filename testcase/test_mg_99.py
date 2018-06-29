#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/19

import pytest
import allure
import urllib
from bs4 import BeautifulSoup


@allure.step("和我看9.9开通芒果会员")
def test_mg99():
    try:
        url = "http://html5.china-plus.net/mg/lingqu"
        res = urllib.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        test_result = soup.title.string
        print test_result
    except Exception as e:
        print e
        raise Exception('H5页面请求出错，请检查！')

    assert res.getcode() == 200
    assert u'2018年9.9开通芒果会员' == test_result


if __name__ == "__main__":
    # test_mg99()
    pytest.main()