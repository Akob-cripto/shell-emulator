"""Тесты парсера эмулятора."""

import unittest

from src.main import parser


class ParserTest(unittest.TestCase):
    """Проверка разбора строки ввода."""

    def test_split(self):
        """Команда и аргументы разделяются по пробелам."""
        self.assertEqual(parser("ls -l /home"), ["ls", "-l", "/home"])

    def test_empty(self):
        """Пустая строка даёт пустой список."""
        self.assertEqual(parser("    "), [])


if __name__ == "__main__":
    unittest.main()