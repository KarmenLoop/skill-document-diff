from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from run import process


class LineEndingTests(unittest.TestCase):
    def test_final_newline_is_a_real_change(self):
        result = process({"before": "hello", "after": "hello\n"})
        self.assertEqual((result["added_lines"], result["removed_lines"]), (1, 1))
        self.assertIn("\\ No newline at end of file", result["unified_diff"])

    def test_crlf_conversion_is_visible(self):
        result = process({"before": "hello\r\n", "after": "hello\n"})
        self.assertEqual((result["added_lines"], result["removed_lines"]), (1, 1))

    def test_same_text_has_no_diff(self):
        result = process({"before": "hello\n", "after": "hello\n"})
        self.assertEqual(result["unified_diff"], "")
        self.assertEqual((result["added_lines"], result["removed_lines"]), (0, 0))


if __name__ == "__main__":
    unittest.main()
