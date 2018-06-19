#!/usr/bin/python
# -*- coding:utf-8 -*-
# @time: 2018/6/19
import pytest
import allure
import urllib
from bs4 import BeautifulSoup


@allure.step("开通芒果TV特惠流量包")
def test_mgVIP():
    try:
        url = "http://flow.m.mgtv.com:8089/orderService/scyd/index.html"
        res = urllib.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        test_result = soup.title.string
        # print test_result
    except Exception as e:
        print e
        raise Exception('H5页面请求出错，请检查！')

    assert res.getcode() == 200
    assert u'芒果TV特惠流量包' == test_result


if __name__ == "__main__":
    # test_mgVIP()
    pytest.main()