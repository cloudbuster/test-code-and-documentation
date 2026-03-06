# Multilingual Text Analyzer - AI Course Assignment

This project provides a robust text analysis utility designed to handle complex internationalization and mathematical edge cases. It satisfies the requirements of Assignment #24 by providing comprehensive unit testing and standard-compliant documentation.

## 🛠 Features & Assignment Requirements

The `MultilingualTextAnalyzer` class includes four primary methods that address the following "hard" cases:

1.  **Unicode Support:** The `extract_hashtags` method uses a custom regex pattern (`\u0600-\u06FF\u4e00-\u9fff`) to identify tags in Arabic and Chinese, moving beyond standard A-Z limitations.
2.  **Mathematical Edge Cases:** The `calculate_sentiment_score` method handles division by zero by returning `float('inf')` and includes validation for negative word counts.
3.  **Data Scalability:** The `normalize_content` method is tested against strings of 1,000,000 characters to ensure performance stability.
4.  **Standard Compliance:** * **PEP 8:** Code follows standard Python style guidelines.
    * **PEP 257/287:** Documentation uses reStructuredText (reST) format for professional-grade docstrings.

## 📁 Project Structure

* `multilingual_text_analyzer.py`: Main logic and documentation.
* `test_analyzer.py`: Unit test suite utilizing `unittest`.
* `pyproject.toml`: Project configuration and dependencies (managed via `uv`).

## 🚀 How to Run

### Prerequisites
This project uses **uv** for dependency management. If you don't have it, you can run the code using standard Python 3.10+.

### Running Tests
To execute the unit tests and verify the edge cases:
```bash
python3 test_analyzer.py
# test-code-and-documentation
