#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/19

import pytest
import allure
import urllib
from bs4 import BeautifulSoup


@allure.step("咪咕下载页")
def test_miguxiazai():
    try:
        url = "http://m.miguvideo.com/publish/h5/page/108.html"
        res = urllib.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        test_result = soup.title.string
        print test_result
    except Exception as e:
        print e
        raise Exception('H5页面请求出错，请检查！')

    assert res.getcode() == 200
    assert u'咪咕视频 让生活更有戏' in test_result


if __name__ == "__main__":
    test_miguxiazai()
    # pytest.main()