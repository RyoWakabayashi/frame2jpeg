# -*- coding: utf-8 -*-
"""
指定した動画から指定したフレームを画像として切り出す
"""

import argparse
import os
import textwrap

import cv2
import pandas as pd
from tqdm import tqdm

#######################################################################
def parse_args():
    """
    引数をパースする
    :return: パース結果
    """
    usage = textwrap.dedent(
        """
        ヘルプ:
            python frame2jpeg.py -h
        フレーム保存:
            python frame2jpeg.py -v sample.mp4 -c sample.csv [-r out]
        """
    )
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument(
        "-v", "--video", type=str, required=True,
        help="path to input video file."
    )
    parser.add_argument(
        "-c", "--csv", type=str, required=True,
        help="path to input csv file."
    )
    parser.add_argument(
        "-o", "--output", type=str, default="out",
        help="path to output jpeg directory path."
    )
    parsed_args = parser.parse_args()

    return parsed_args

#######################################################################
def write_frame(capture, frame_number, output_path):
    """
    フレームの書込み
    :param capture: 入力動画キャプチャー
    :param frame_number: フレーム番号
    :param output_path: 出力画像ファイルパス
    """

    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = capture.read()
    if ret:
        cv2.imwrite(output_path, frame)

#######################################################################
def main(args):
    """
    メイン処理
    :param args: 引数
    """

    capture = cv2.VideoCapture(args.video)
    if not capture.isOpened():
        print("Can't open video file.")
        return

    os.makedirs(args.output, exist_ok=True)

    frame_df = pd.read_csv(args.csv)

    for _, row in tqdm(frame_df.iterrows(), total=len(frame_df)):

        frame_num = row["frame_num"]

        output_filename = os.path.splitext(args.video)[0] + "_" + str(frame_num).zfill(6) + ".jpg"

        write_frame(
            capture, frame_num,
            os.path.join(args.output, output_filename)
        )

#######################################################################
if __name__ == "__main__":
    FLAGS = parse_args()
    main(FLAGS)
