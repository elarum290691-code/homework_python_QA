

import pytest
from string_utils import StringUtils


class TestStringUtils:
    """Класс для тестирования StringUtils"""

    @pytest.fixture
    def utils(self):
        """Фикстура для создания экземпляра StringUtils"""
        return StringUtils()

    # Тесты для capitalize
    def test_capitalize_positive(self, utils):
        """Позитивный тест: обычная строка"""
        assert utils.capitalize("hello") == "Hello"
        assert utils.capitalize("world") == "World"
        assert utils.capitalize("123abc") == "123abc"

    def test_capitalize_negative(self, utils):
        """Негативный тест: пустая строка"""
        assert utils.capitalize("") == ""
        assert utils.capitalize(" ") == " "

    # Тесты для trim
    def test_trim_positive(self, utils):
        """Позитивный тест: строка с пробелами"""
        assert utils.trim("  hello  ") == "hello"
        assert utils.trim("   world") == "world"
        assert utils.trim("  ") == ""

    def test_trim_negative(self, utils):
        """Негативный тест: строка без пробелов"""
        assert utils.trim("hello") == "hello"
        assert utils.trim("") == ""

    # Тесты для to_list
    def test_to_list_positive(self, utils):
        """Позитивный тест: строка с разделителем"""
        assert utils.to_list("a,b,c") == ["a", "b", "c"]
        assert utils.to_list("1,2,3,4") == ["1", "2", "3", "4"]

    def test_to_list_negative(self, utils):
        """Негативный тест: пустая строка"""
        assert utils.to_list("") == []
        assert utils.to_list("   ") == ["   "]

    # Тесты для contains
    def test_contains_positive(self, utils):
        """Позитивный тест: символ содержится в строке"""
        assert utils.contains("Hello", "H")
        assert utils.contains("Hello", "llo")

    def test_contains_negative(self, utils):
        """Негативный тест: символ не содержится в строке"""
        assert not utils.contains("Hello", "z")
        assert not utils.contains("", "a")

    # Тесты для delete_symbol
    def test_delete_symbol_positive(self, utils):
        """Позитивный тест: удаление символа"""
        assert utils.delete_symbol("Hello", "l") == "Heo"
        assert utils.delete_symbol("aaa", "a") == ""

    def test_delete_symbol_negative(self, utils):
        """Негативный тест: символ отсутствует"""
        assert utils.delete_symbol("Hello", "z") == "Hello"
        assert utils.delete_symbol("", "a") == ""

    # Тесты для starts_with
    def test_starts_with_positive(self, utils):
        """Позитивный тест: строка начинается с символа"""
        assert utils.starts_with("Hello", "H")
        assert utils.starts_with("123", "1")

    def test_starts_with_negative(self, utils):
        """Негативный тест: строка не начинается с символа"""
        assert not utils.starts_with("Hello", "e")
        assert not utils.starts_with("", "H")

    # Тесты для end_with
    def test_end_with_positive(self, utils):
        """Позитивный тест: строка заканчивается на символ"""
        assert utils.end_with("Hello", "o")
        assert utils.end_with("Hello", "llo")

    def test_end_with_negative(self, utils):
        """Негативный тест: строка не заканчивается на символ"""
        assert not utils.end_with("Hello", "H")
        assert not utils.end_with("", "o")

    # Тесты для is_empty
    def test_is_empty_positive(self, utils):
        """Позитивный тест: строка пустая"""
        assert utils.is_empty("")
        assert utils.is_empty("   ")

    def test_is_empty_negative(self, utils):
        """Негативный тест: строка не пустая"""
        assert not utils.is_empty("Hello")
        assert not utils.is_empty(" a ")

    # Тесты для list_to_string
    def test_list_to_string_positive(self, utils):
        """Позитивный тест: список с разделителем"""
        assert utils.list_to_string(["a", "b", "c"]) == "a, b, c"
        assert utils.list_to_string([1, 2, 3]) == "1, 2, 3"

    def test_list_to_string_negative(self, utils):
        """Негативный тест: пустой список"""
        assert utils.list_to_string([]) == ""
