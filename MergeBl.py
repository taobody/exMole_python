# -*- coding:utf-8 -*-

import sys
import datetime
import pandas as pd

# from tqdm import tqdm


def merge(selected_button, enc_path, lidar_path, save_dir):

    lidar_enc_df = pd.DataFrame()

    # pandasでcvsファイルを読み込んでデータフレームに格納する
    enc_df = pd.read_csv(enc_path, sep=',', header=None, names=['date', 'Z_axis'])
    lidar_df = pd.read_csv(lidar_path, sep=',', header=None, names=['date', 'X_axis', 'Y_axis'])

    # 結合開始
    start_time = datetime.datetime.now()
    print('結合開始：' + start_time.strftime('%Y-%m-%d %H:%M:%S'))

    print('--------------------------------------------')
    # date列　21文字目(ミリセカンド1桁)
    # date列　19文字目(セカンド)

    # ラジオボタンの値が
    # 0(レーザー)なら21文字目まで
    # 1(エンコーダー)なら19文字目までをマッチングさせる
    if selected_button == 0:
        date_length = 21
    else:
        date_length = 19

    # todo
    # エンコーダーベース（みりセカンド）でマッチングさせる場合
    # ピッタリ一致はありえないので、近似を取るようなロジックを追加する。

    # enc_dfのdate列を19文字（秒）に変更
    enc_df['date'] = enc_df['date'].str[:date_length]
    enc_df['Z_axis'] = enc_df['Z_axis'] * 100

    # lidar_dfのdate列を19文字（秒）に変更
    lidar_df['date'] = lidar_df['date'].str[:date_length]

    # 日付データのミリセカンドまでで重複しないもののみ出力
    # print(enc_df.drop_duplicates().info())

    # lidar_dfとenc_dfを右外部結合
    lidar_enc_df = pd.merge(lidar_df, enc_df, how="right", on='date')
    # # 再度重複行を削除
    lidar_enc_df = lidar_enc_df.drop_duplicates()
    # # 重複しないNaNを含む行を削除
    lidar_enc_df = lidar_enc_df.dropna(axis=0, how='any')

    # 出力（1列目は不要なのでindexはFalseを指定）
    make_file_name = save_dir + '/' + start_time.strftime('%Y%m%d_%H%M%S') + '_treated.csv'
    end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("出力ファイル名：" + make_file_name)
    print("データ数（行）：" + str(len(lidar_enc_df)))
    print('--------------------------------------------')
    print('結合完了：' + end_time)
