# -*- coding: utf-8 -*-

import os
import pandas as pd
import datetime
from configs.config import log


def get_result_img_name(result_csv_path=None):
    """获取当天已经爬取的图片名称"""
    img_name_exist = []
    if not result_csv_path:
        today = datetime.date.today()
        filename = f'./data/result/{today}_result.csv'
        if not os.path.exists(filename):
            log.info('没有数据，还没开始爬取')

        else:
            df = pd.read_csv(filename)
            img_name_exist = list(set(list(df['imgName'])))

    else:
        if not os.path.exists(result_csv_path) or '.csv' not in result_csv_path:
            log.info('传入的文件路径不正确或不是csv格式，请重新输入')

        else:
            df = pd.read_csv(result_csv_path)
            img_name_exist = list(set(list(df['imgName'])))


    # print(img_name_exist)
    return img_name_exist



# get_result_img_name('../data/result/2021-12-13_result.csv')
