import unittest
import math
from multilingual_text_analyzer import MultilingualTextAnalyzer

class TestMultilingualTextAnalyzer(unittest.TestCase):
    """
    Unit tests for the MultilingualTextAnalyzer class.

    These tests cover standard functionality as well as edge cases involving
    Unicode (Arabic/Chinese), floating-point infinity, and large data inputs
    to comply with PEP 8 and PEP 287 standards.
    """

    def setUp(self):
        """
        Initialize the analyzer instance before each test.
        """
        self.analyzer = MultilingualTextAnalyzer()

    def test_normalize_content_massive_string(self):
        """
        Test normalization with a 1-million character string.
        
        Verifies that the tool handles extreme input lengths without crashing.
        """
        large_input = "  " + ("A" * 1000000) + "  "
        result = self.analyzer.normalize_content(large_input)
        self.assertEqual(len(result), 1000000)
        self.assertFalse(result.startswith(" "))

    def test_extract_hashtags_unicode(self):
        """
        Test hashtag extraction with non-Latin characters (Arabic and Chinese).
        
        Ensures the regex properly identifies Unicode word boundaries.
        """
        text = "Welcome to #Dubai (#دبي) and #Beijing (#北京)!"
        tags = self.analyzer.extract_hashtags(text)
        
        # Checking for specific Unicode tags
        self.assertIn("#دبي", tags)
        self.assertIn("#北京", tags)
        self.assertEqual(len(tags), 4)

    def test_calculate_sentiment_infinity(self):
        """
        Test sentiment calculation with zero total words.
        
        Verifies that the method returns float infinity rather than crashing,
        simulating a specific mathematical edge case.
        """
        result = self.analyzer.calculate_sentiment_score(10, 0)
        self.assertTrue(math.isinf(result))
        self.assertGreater(result, 0)

    def test_calculate_sentiment_negative_input(self):
        """
        Test that negative word counts raise a ValueError.
        """
        with self.assertRaises(ValueError):
            self.analyzer.calculate_sentiment_score(5, -1)

    def test_generate_summary_edge_cases(self):
        """
        Test summary generation with zero/negative limits and empty strings.
        """
        self.assertEqual(self.analyzer.generate_summary("Hello", 0), "")
        self.assertEqual(self.analyzer.generate_summary("", 10), "")
        self.assertEqual(self.analyzer.generate_summary("Short", 5), "Short")
        
    def test_normalize_content_none(self):
        """
        Test normalization with None input to ensure robust type handling.
        """
        # Note: In standard Python this might be handled by type hinting,
        # but runtime checks are better for robust AI tools.
        self.assertEqual(self.analyzer.normalize_content(None), "")

if __name__ == "__main__":
    unittest.main()
