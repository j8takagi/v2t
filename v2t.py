import sys
import os
import whisper

def format_timestamp(seconds):
    """秒数を [MM:SS] 形式の文字列に変換する"""
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    hours = mins // 60
    if hours > 0:
        mins = mins % 60
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"

def log(message):
    """進捗やステータス情報は必ず標準エラー出力へ流す"""
    sys.stderr.write(message + "\n")
    sys.stderr.flush()

def main():
    if len(sys.argv) < 2:
        log("Usage: python3 v2t.py <audio_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        log(f"Error: ファイルが見つかりません: {input_file}")
        sys.exit(1)

    output_file = os.path.splitext(input_file)[0] + ".txt"

    log("[*] モデルをロード中 (base)...")
    model = whisper.load_model("base")

    log(f"[*] 文字起こしを開始します: {input_file}")
    # language="ja" を明示的に指定することで、
    # 余計な "Detected language: ..." の自動検出メッセージやブレを防ぎます
    result = model.transcribe(input_file, language="ja", fp16=False, verbose=False)

    log("[*] タイムスタンプ付きログを生成中...")
    log_lines = []
    for segment in result["segments"]:
        start_time = format_timestamp(segment["start"])
        text = segment["text"].strip()
        line = f"[{start_time}] {text}"
        log_lines.append(line)

    output_content = "\n".join(log_lines) + "\n"

    # 1. テキストファイルに保存
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_content)

    # 2. リダイレクト先（> 1.txt など）へ純粋なテキストを渡すため標準出力に出力
    # （※ 途中のログはすべて標準エラー出力に出ているため、1.txt にはテキストのみが入ります）
    sys.stdout.write(output_content)

    log(f"[*] 保存しました: {output_file}")

print = None # 余計なグローバル汚染を防ぐ

if __name__ == "__main__":
    main()
