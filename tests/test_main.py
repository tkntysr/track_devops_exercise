from src.main import add
import pytest

def test_add():
    # 既存テスト
    assert add(2, 3) == 5
    assert add(1.2, 3.5) == 4

    # 追加テスト20件以上

    # 基本的な整数
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-5, -7) == -12
    assert add(10, -3) == 7

    # c を指定するテスト
    assert add(2, 3, 4) == 9
    assert add(1.2, 3.5, 2) == 6
    assert add(-5, 10, -3) == 2

    # 浮動小数が整数にキャストされる確認
    assert add(2.9, 3.1) == 6
    assert add(2.9, 3.1, 4.9) == 10

    # 文字列で渡された場合
    assert add("2", "3") == 23
    assert add("2", "3", "4") == 27
    assert add("10", "-3") == 7

    # 数値化できない文字列
    assert add("a", 3) == "error"
    assert add(3, "b") == "error"
    assert add("a", "b") == "error"
    assert add("1.2x", "3") == "error"

    # None を渡す
    assert add(None, 3) == "error"
    assert add(3, None) == "error"
    assert add(None, None) == "error"

    # リストや辞書など不正な型
    assert add([], 3) == "error"
    assert add(3, {}) == "error"
    assert add([], {}) == "error"

    # 大きい値
    assert add(10**6, 10**6) == 2000000

    # 片方を bool にする (bool は int として扱われる)
    assert add(True, 3) == 4
    assert add(False, 3) == 3
