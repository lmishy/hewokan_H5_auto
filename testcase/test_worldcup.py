#!/usr/bin/python
# -*- coding:utf-8 -*-
# @time: 2018/6/19
import pytest
import allure
import urllib
from bs4 import BeautifulSoup


@allure.step("世界杯-咪咕钻石会员-超级视频")
def test_worldcup():
    try:
        url = "http://html5.china-plus.net/mg/worldcupy"
        res = urllib.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        test_result = soup.title.string
        # print test_result
    except Exception as e:
        print e
        raise Exception('H5页面请求出错，请检查！')

    assert res.getcode() == 200
    assert u'咪咕钻石会员-超级视频' == test_result


if __name__ == "__main__":
    # test_worldcup()
    pytest.main()