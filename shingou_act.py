import sys


def shingou_action(color_code):
    if color_code == 1:
        return "「とまれ」"
    elif color_code == 2:
        return "「すすめ」"
    elif color_code == 3:
        return "「ちゅうい」"
    else:
        return "無効な色のコードです"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("正しい引数がありません。色の数値を1つ指定してください。")
    else:
        try:
            color_code = int(sys.argv[1])
            result = shingou_action(color_code)
            print(result)
        except ValueError:
            print("無効な色の数値です。整数を指定してください。")

