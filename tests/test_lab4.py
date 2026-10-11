import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab4 import (
    find_substring, replace_substring, split_text,
    format_string_f, format_string_method, extract_emails,
    validate_phone_number, extract_hashtags, extract_mentions,
    count_words, count_sentences, word_frequency
)

class TestTextAnalyzer(unittest.TestCase):

    def test_find_substring(self):
        self.assertEqual(find_substring("Hello, world!", "world"), 7)
        self.assertEqual(find_substring("Hello", "x"), -1)

    def test_replace_substring(self):
        self.assertEqual(replace_substring("Hello, world!", "world", "Python"), "Hello, Python!")

    def test_split_text(self):
        self.assertEqual(split_text("Hello, world!", ", "), ["Hello", "world!"])

    def test_format_string_f(self):
        self.assertEqual(format_string_f("Alice", 30), "Мене звати Alice і мені 30 років.")

    def test_format_string_method(self):
        self.assertEqual(format_string_method("Bob", 25), "Мене звати Bob і мені 25 років.")

    def test_extract_emails(self):
        text = "Contact us at info@example.com or support@test.com"
        expected = ["info@example.com", "support@test.com"]
        self.assertEqual(extract_emails(text), expected)

    def test_validate_phone_number(self):
        self.assertTrue(validate_phone_number("+380123456789"))
        self.assertFalse(validate_phone_number("12345"))
        self.assertFalse(validate_phone_number("+38012345678")) # Занадто короткий

    def test_extract_hashtags(self):
        text = "I love #Python and #Programming"
        expected = ["#Python", "#Programming"]
        self.assertEqual(extract_hashtags(text), expected)

    def test_extract_mentions(self):
        text = "Hello @user1 and @admin_user"
        expected = ["@user1", "@admin_user"]
        self.assertEqual(extract_mentions(text), expected)

    def test_count_words(self):
        self.assertEqual(count_words("Один, два, три слова!"), 4)

    def test_count_sentences(self):
        self.assertEqual(count_sentences("Перше. Друге! Третє?"), 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)