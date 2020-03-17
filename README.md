# frame2jpeg

指定した動画から指定したフレームを画像として切り出す

## 目次

* [実行環境](#実行環境)
* [開発環境](#開発環境)
* [実行方法](#実行方法)
* [エラーチェック](#エラーチェック)

## 実行環境

### 必要なソフトウェア

* [asdf]

## 開発環境

GitHubからリポジトリーをクローンする

    $ cd && git clone git@github.com:RyoWakabayashi/frame2jpeg.git \
        && cd frame2jpeg

プラグインを追加する

    $ asdf plugin-add python

必要なソフトウェアをインストールする

    $ asdf install

必要なパッケージをインストールする

    $ pip install -r requirements.txt

## 実行方法

以下のコマンドでヘルプを表示し、使用方法を参照する

    $ python frame2jpeg.py --help

## エラーチェック

変更時は以下のコマンドでエラーがないか確認し、OKであれば `git push` してPRをしてください

    $ pre-commit run --all-files

💡 エラーチェックは `pre-commit install` で自動化できます。

[asdf]: https://github.com/asdf-vm/asdf
