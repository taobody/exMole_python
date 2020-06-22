# -*- coding:utf-8 -*-
import pandas as pd


def seplog(path, pitch, offset, save_dir):
    print('パス：', path)
    print('ピッチ：', pitch, 'cm')
    print('オフセット：', offset, 'cm')
    print('保存先：', save_dir)

    # ピッチを㎜に換算
    pitch = float(pitch) * 10

    # targetファイルをdataframeに読み込み
    target_df = pd.read_csv(path)

    # 距離の初期値（データの一行目のZ_axis）を取得
    init_dist = target_df.iloc[1, 3]

    # Z_axisが、初期値にピッチを足した値と近似のものだけ取り出して
    # データがなくなるまで、ピッチごとのデータを取り出してファイルに書き出し
    # ここで、近似は±50㎜とする
    cnt = 1
    print('分割開始')
    print('--------------------------------------------')

    while True:
        min_pitch = (pitch * cnt) - 50
        max_pitch = (pitch * cnt) + 50
        separated_df = target_df[(target_df['Z_axis'] > init_dist + min_pitch)
                                 & (target_df['Z_axis'] < init_dist + max_pitch)]
        if not separated_df.empty:
            make_file_name = save_dir + '/sep_' + str(cnt) + '.csv'
            separated_df.to_csv(make_file_name, index=False)
            print(make_file_name + 'を作成しました')
            cnt += 1
        else:
            break

    print('--------------------------------------------')
    print('分割終了')


