#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/19

import pytest
import allure
import urllib
from bs4 import BeautifulSoup


@allure.step("世界杯-竞猜活动")
def test_worldguess():
    try:
        url = "http://shijiebei.0ymfyz.com:6003/share.html"
        res = urllib.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        test_result = soup.title.string
        print test_result
    except Exception as e:
        print e
        raise Exception('H5页面请求出错，请检查！')

    assert res.getcode() == 200
    assert u'世界杯' == test_result


if __name__ == "__main__":
    # test_worldguess()
    pytest.main()