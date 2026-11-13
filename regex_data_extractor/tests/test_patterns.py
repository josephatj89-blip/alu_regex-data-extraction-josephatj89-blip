import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from patterns import extract

CASES = {
    "email": (
        ["user@example.com", "firstname.lastname@company.co.uk"],
        ["user@", "@example.com", "user@example", "user example.com"],
    ),
    "url": (
        ["https://www.example.com", "https://subdomain.example.org/page"],
        ["htp://example.com", "https://", "example.com"],
    ),
    "phone": (
        ["(123) 456-7890", "123-456-7890", "123.456.7890"],
        ["123-45-67890", "12345678901", "1234-5678-9012-3456"],
    ),
    "card": (
        ["1234 5678 9012 3456", "1234-5678-9012-3456"],
        ["1234 5678 9012", "12345 6789 0123 4567"],
    ),
    "time": (
        ["14:30", "2:30 PM", "12:00 am"],
        ["25:99", "99:30", "14:75"],
    ),
    "html": (
        ["<p>", '<div class="example">', '<img src="image.jpg" alt="description">'],
        ["a < b > c", "<3", "<>"],
    ),
    "hashtag": (
        ["#example", "#ThisIsAHashtag"],
        ["#", "# space", "#123", "no#tag"],
    ),
    "currency": (
        ["$19.99", "$1,234.56", "$5"],
        ["19.99", "$", "$,234"],
    ),
}


class TestPatterns(unittest.TestCase):
    def test_valid(self):
        for kind, (valid, _) in CASES.items():
            for sample in valid:
                with self.subTest(kind=kind, sample=sample):
                    self.assertEqual(extract(kind, sample), [sample])

    def test_invalid(self):
        for kind, (_, invalid) in CASES.items():
            for sample in invalid:
                with self.subTest(kind=kind, sample=sample):
                    self.assertEqual(extract(kind, sample), [])

    def test_multiple_in_one_string(self):
        text = "Call 123-456-7890 or (123) 456-7890"
        self.assertEqual(extract("phone", text), ["123-456-7890", "(123) 456-7890"])

    def test_url_trailing_punctuation(self):
        self.assertEqual(extract("url", "see https://example.com."), ["https://example.com"])


if __name__ == "__main__":
    unittest.main()
