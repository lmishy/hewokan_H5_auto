#!/usr/bin/python
# -*- coding:utf-8 -*-
# @time: 2018/6/19
import pytest
import allure
import urllib
from bs4 import BeautifulSoup


@allure.step("中国移动139邮箱登录")
def test_139mail():
    try:
        url = "http://html5.mail.10086.cn/?Adapt-Flag=on&cguid=0939000421196&mtime=32"
        res = urllib.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        test_result = soup.title.string
        # print test_result
    except Exception as e:
        print e
        raise Exception('H5页面请求出错，请检查！')

    assert res.getcode() == 200
    assert u'中国移动139邮箱-手机号就是邮箱号' == test_result


if __name__ == "__main__":
    # test_139mail()
    pytest.main()