from enum import Enum


class Shingou(Enum):
    TOMARE = "とまれ"
    SUSUME = "すすめ"
    CHUUI = "ちゅうい"


def act_shingou(color):
    try:
        color = int(color)
        if color == 1:
            action = Shingou.TOMARE
        elif color == 2:
            action = Shingou.SUSUME
        elif color == 3:
            action = Shingou.CHUUI
        else:
            raise ValueError("信号機の色に対応していません")

        print(action.value)

        return action
    except ValueError as e:
        print(f"エラー: {e}")
        raise


# テスト
act_shingou(1)  # とまれ
act_shingou(2)  # すすめ
act_shingou(3)  # ちゅうい
act_shingou(4)  # 例外発生
