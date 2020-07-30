# -*- coding:utf-8 -*-

import datetime
import pandas as pd


def seplog(path, pitch, tolerance, offset, save_dir):
    print('ファイル名\t：', path)
    print('分割ピッチ\t：', pitch, 'cm')
    print('許容範囲\t：', tolerance, 'cm')
    print('オフセット\t：', offset, 'cm')
    print('保存先\t：', save_dir)

    # ピッチ、許容範囲、オフセット値を㎜に換算
    pitch = float(pitch) * 10
    tolerance = float(tolerance) * 10
    offset = float(offset) * 10

    # targetファイルをdataframeに読み込み
    target_df = pd.read_csv(path)

    # 最初にオフセット値をZ_axisから減算しておく
    target_df['Z_axis'] -= offset

    # Z_axisが、初期値にピッチを足した値と近似のものだけ取り出して
    # データがなくなるまで、ピッチごとのデータを取り出してファイルに書き出し
    # ここで、近似はtoleranceとする
    cnt = 1
    start_time = datetime.datetime.now()
    # print(len(target_df))
    print('分割開始\t：' + start_time.strftime('%Y-%m-%d %H:%M:%S'))
    print('--------------------------------------------')

    # Z_axisの最大値を取得
    data_cnt = len(target_df.index) - 1
    # print(data_cnt)
    max_zaxis = target_df.iloc[data_cnt, 3]
    # print(max_zaxis)

    while True:
        min_pitch = (pitch * cnt) - tolerance
        max_pitch = (pitch * cnt) + tolerance
        # print('min:' + str(min_pitch) + ' ' + 'max:' + str(max_pitch))
        # separated_df = target_df[(target_df['Z_axis'] > (init_dist + min_pitch))
        #                          & (target_df['Z_axis'] < (init_dist + max_pitch))]
        separated_df = target_df[(target_df['Z_axis'] > min_pitch)
                                 & (target_df['Z_axis'] < max_pitch)]

        # print(separated_df.tail(5))
        if not separated_df.empty:
            make_file_name = save_dir + '/' + start_time.strftime('%Y%m%d_%H%M%S') + '_sep_' + str(cnt) + '.csv'
            separated_df.to_csv(make_file_name, index=False)
            print(make_file_name + 'を作成しました')
        elif max_zaxis < max_pitch:
            break

        cnt += 1

    print('--------------------------------------------')
    end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('分割完了\t：' + end_time)


