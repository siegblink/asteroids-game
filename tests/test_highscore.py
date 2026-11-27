import tempfile
import unittest
from pathlib import Path

from highscore import load_high_score, save_high_score


class HighScoreTest(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.path = Path(folder.name) / "highscore"

    def test_a_missing_file_means_no_high_score(self):
        self.assertEqual(load_high_score(self.path), 0)

    def test_a_saved_score_is_read_back(self):
        save_high_score(1250, self.path)

        self.assertEqual(load_high_score(self.path), 1250)

    def test_a_damaged_file_means_no_high_score(self):
        self.path.write_text("not a number")

        self.assertEqual(load_high_score(self.path), 0)


if __name__ == "__main__":
    unittest.main()
