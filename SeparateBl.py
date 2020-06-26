# -*- coding:utf-8 -*-

import datetime
import pandas as pd


def seplog(path, pitch, tolerance, offset, save_dir):
    print('ファイル名：', path)
    print('分割ピッチ：', pitch, 'cm')
    print('許容範囲：', tolerance, 'cm')
    print('オフセット：', offset, 'cm')
    print('保存先：', save_dir)

    # ピッチ、許容範囲、オフセット値を㎜に換算
    pitch = float(pitch) * 10
    tolerance = float(tolerance) * 10
    offset = float(offset) * 10

    # targetファイルをdataframeに読み込み
    target_df = pd.read_csv(path)

    # 距離の初期値（データの一行目のZ_axis）を取得
    init_dist = target_df.iloc[1, 3]

    # Z_axisが、初期値にピッチを足した値と近似のものだけ取り出して
    # データがなくなるまで、ピッチごとのデータを取り出してファイルに書き出し
    # ここで、近似は±50㎜とする
    cnt = 1
    start_time = datetime.datetime.now()
    # print(len(target_df))
    print('分割開始：' + start_time.strftime('%Y-%m-%d %H:%M:%S'))
    print('--------------------------------------------')

    while True:
        min_pitch = (pitch * cnt) + offset - tolerance
        max_pitch = (pitch * cnt) + offset + tolerance
        separated_df = target_df[(target_df['Z_axis'] > init_dist + min_pitch)
                                 & (target_df['Z_axis'] < init_dist + max_pitch)]
        if not separated_df.empty:
            make_file_name = save_dir + '/' + start_time.strftime('%Y%m%d_%H%M%S') + '_sep_' + str(cnt) + '.csv'
            separated_df.to_csv(make_file_name, index=False)
            print(make_file_name + 'を作成しました')
            cnt += 1
        else:
            break
            
    print('--------------------------------------------')
    end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('分割完了：' + end_time)


