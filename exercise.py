import enum
import sys


# 列挙型の定義
class TrafficLightColor(enum.Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3


# ジェネレータ関数の定義
def generate_messages():
    return iter({"「とまれ」", "「すすめ」", "「ちゅうい」"})


# クロージャを使用したメッセージ取得関数の定義
class MessageGenerator:
    def __init__(self):
        self.messages = generate_messages()

    def get_message(self):
        return next(self.messages)


# セットの利用
valid_color_codes = {color.value for color in TrafficLightColor}


# コマンドライン引数の処理
def process_command_line_argument():
    if len(sys.argv) != 2:
        print("正しい引数がありません。色の数値を1つ指定してください。")
        sys.exit(1)

    try:
        color_code = int(sys.argv[1])
        if color_code not in valid_color_codes:
            print("無効な色のコードです。1から3までの整数を指定してください。")
            sys.exit(1)
        return color_code
    except ValueError:
        print("無効な色の数値です。整数を指定してください。")
        sys.exit(1)


# メインプログラム
if __name__ == "__main__":
    color_code = process_command_line_argument()

    # 列挙型から色を取得
    color = TrafficLightColor(color_code)

    # クロージャからメッセージを取得
    message_generator = MessageGenerator()
    message = message_generator.get_message()

    print(f"信号の色: {color.name}")
    print(f"メッセージ: {message}")
