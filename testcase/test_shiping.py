#!/usr/bin/python
# -*- coding:utf-8 -*-
#@time: 2018/6/19
import pytest
import allure
import urllib
from bs4 import BeautifulSoup


@allure.step("视频彩铃小常识")
def test_shipingcangshi():
    try:
        url = "http://html5.china-plus.net/x.html"
        res = urllib.urlopen(url)
        soup = BeautifulSoup(res,"html.parser")
        test_result = soup.title.string
    except Exception as e :
        print e
        raise Exception('H5页面请求出错，请检查！')
    
    assert res.getcode() == 200
    assert u'视频彩铃小常识'== test_result
    
if __name__ == "__main__":
    pytest.main()