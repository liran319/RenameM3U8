#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

dir_path = sys.argv[1]
# dir_path = r"E:\m3u8s"
# m3u8_list = []


def rename(filepath):
    """
    重命名:
    abcd%5Fefg-1.m3u8 --> abcd_efg-1.m3u8
    abcd%5Fefg-2.m3u8 --> abcd_efg-2.m3u8
    """
    files = os.listdir(filepath)
    for i in files:
        if i.endswith(".m3u8"):  # 对该目录下所有的m3u8文件进行检查和重命名
            # print i
            try:
                j = i.replace(r"%5F", "_")
            except Exception as e:
                print e
            oldfile = os.path.join(filepath, i)
            newfile = os.path.join(filepath, j)
            try:
                os.rename(oldfile, newfile)
            except Exception as e:
                print e
        else:
            pass


if __name__ == '__main__':
    rename(dir_path)
