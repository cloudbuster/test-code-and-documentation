import re
import math

class MultilingualTextAnalyzer:
    """
    A utility class for processing and analyzing multilingual text data.

    This class provides methods to normalize strings, extract metadata, 
    and perform calculations that handle various edge cases including 
    Unicode characters and extreme numerical values.

    :param default_language: The ISO code for the default language.
    :type default_language: str
    """

    def __init__(self, default_language: str = "en"):
        self.default_language = default_language
        self.hashtag_pattern = re.compile(r"#[\w\u0600-\u06FF\u4e00-\u9fff]+")

    def normalize_content(self, text: str, lowercase: bool = True) -> str:
        """
        Cleans and normalizes the input text.

        Handles leading/trailing whitespace and optionally converts to lowercase.
        Designed to handle massive strings and null-type inputs gracefully.

        :param text: The raw string to be normalized.
        :param lowercase: Whether to fold the case.
        :return: A cleaned version of the string.
        """
        if not text:
            return ""
        
        cleaned = text.strip()
        return cleaned.lower() if lowercase else cleaned

    def extract_hashtags(self, text: str) -> list:
        """
        Extracts hashtags from text, supporting Arabic and Chinese characters.

        :param text: The string containing potential hashtags.
        :return: A list of unique hashtags found in the text.
        """
        if not isinstance(text, str):
            return []
        
        tags = self.hashtag_pattern.findall(text)
        return list(set(tags))

    def calculate_sentiment_score(self, positive_count: int, total_words: int) -> float:
        """
        Calculates a simple sentiment ratio.

        This method is designed to test floating-point edge cases like 
        division by zero, infinity, and NaN.

        :param positive_count: Number of positive words identified.
        :param total_words: Total number of words in the text.
        :return: A float representing the sentiment density.
        :raises ValueError: If total_words is negative.
        """
        if total_words < 0:
            raise ValueError("Word count cannot be negative.")
        
        try:
            return positive_count / total_words
        except ZeroDivisionError:
            return float('inf')

    def generate_summary(self, text: str, max_chars: int) -> str:
        """
        Truncates text to a specific length with an ellipsis.

        :param text: The full text to summarize.
        :param max_chars: The character limit for the summary.
        :return: The truncated string.
        """
        if not text or max_chars <= 0:
            return ""
            
        if len(text) <= max_chars:
            return text
            
        return text[:max_chars].rstrip() + "..."
