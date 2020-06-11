# -*- coding:utf-8 -*-

import sys
import pandas as pd


def merge(enc_path, lidar_path, save_dir):

    # pandasでcvsファイルを読み込んでデータフレームに格納するパターン
    enc_df = pd.read_csv(enc_path, sep=',', header=None, names=['date', 'Z_axis'])
    lidar_df = pd.read_csv(lidar_path, sep=',', header=None, names=['date', 'X_axis', 'Y_axis'])

    # date列を21文字(ミリセカンド1桁)に変更
    # enc_df['date'] = enc_df['date'].str[:21]
    # print(enc_df.head(5))
    print('--------------------------------------------')

    # enc_dfのdate列を19文字（秒）に変更
    enc_df['date'] = enc_df['date'].str[:19]
    enc_df['Z_axis'] = enc_df['Z_axis'] * 100
    print(enc_df.tail(5))
    print('--------------------------------------------')

    # lidar_dfのdate列を19文字（秒）に変更
    lidar_df['date'] = lidar_df['date'].str[:19]
    print(lidar_df.tail(5))
    print('--------------------------------------------')

    # 日付データのミリセカンドまでで重複しないもののみ出力
    # print(enc_df.drop_duplicates().info())

    # lidar_dfとenc_dfを右外部結合
    lidar_enc_df = pd.merge(lidar_df, enc_df, how="right", on='date')
    # 再度重複行を削除
    lidar_enc_df = lidar_enc_df.drop_duplicates()
    # 重複しないNaNを含む行を削除
    lidar_enc_df = lidar_enc_df.dropna(axis=0, how='any')
    print(lidar_enc_df)

    # 出力（1列目は不要なのでindexはFalseを指定）
    make_file_name = save_dir + '/treated.csv'
    print(make_file_name)
    lidar_enc_df.to_csv(make_file_name, index=False)

    # print(lidar_df['date'].head(3))
