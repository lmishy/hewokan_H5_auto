#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/19

import pytest
import allure
import urllib



@allure.step("世界杯赛程安排")
def test_schedule():
    try:
        url = "http://html5.china-plus.net/worldcupinfo.html"
        res = urllib.urlopen(url)
        print res.getcode()
    except Exception as e:
        print e
        raise Exception('H5页面请求出错，请检查！')

    assert res.getcode() == 200



if __name__ == "__main__":
    # test_schedule()
    pytest.main()