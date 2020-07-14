import unittest
from extracttext import ExtractText


class Test_getTextFromUrl(unittest.TestCase):

    extractText = ExtractText()

    def test_ret_type(self):
        textFromUrl = self.extractText.getTextFromUrl(
            'https://sara-sabr.github.io/ITStrategy/home.html')
        assert isinstance(
            textFromUrl, str), 'getTextFromUrl did not return a string'


if __name__ == '__main__':
    unittest.main()
