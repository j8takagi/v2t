# v2t

OpenAI Whisper を利用したコマンドライン音声文字起こしツール。MITライセンスの下で自由に利用・改変・配布が可能

## 動作要件

実行には以下が必要です。

* **Python**: 3.10 以上
* **FFmpeg**: Whisper の音声デコードに使用します。

  ```bash
  brew install ffmpeg
  ```

## インストール

1. リポジトリをクローンします:

   ```bash
   git clone https://github.com/j8takagi/v2t.git
   cd v2t
   ```

2. 必要な Python パッケージをインストールします:

   ```bash
   pip install openai-whisper torch
   ```

## 使い方

対象の音声ファイルを引数として渡して実行します。ターミナル上で進捗を確認しながらテキスト保存したい場合は、標準出力のリダイレクトを利用してください:

```bash
python3 v2t.py sample.mp3 > sample.txt
```

## ライセンス

本プロジェクトは MIT ライセンス の下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。
