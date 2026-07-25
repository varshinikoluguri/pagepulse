import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))

from parser import analyze_url


def test_valid_url():
    result = analyze_url("https://example.com")

    assert "status" in result
    assert result["status"] == 200


def test_invalid_url():
    result = analyze_url("invalid-url")

    assert "error" in result


def test_non_html_url():
    result = analyze_url("https://httpbin.org/image/png")

    assert "error" in result