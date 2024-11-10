import unittest
from extract_title import extract_title_markdown

class TestExtractTitleMarkdown(unittest.TestCase):

    def test_single_title(self):
        # Test a markdown string with a single top-level title
        markdown = "# Main Title\nSome content here."
        self.assertEqual(extract_title_markdown(markdown), "Main Title")

    def test_multiple_titles(self):
        # Test a markdown string with multiple top-level titles
        markdown = "# Main Title\nSome content here.\n# Another Title"
        with self.assertRaises(Exception):
            extract_title_markdown(markdown)

    def test_no_title(self):
        # Test a markdown string with no top-level title
        markdown = "Some content here without a title."
        with self.assertRaises(Exception):
            extract_title_markdown(markdown)

    def test_title_with_subtitles(self):
        # Test a markdown string with a single top-level title and subtitles
        markdown = "# Main Title\n## Subtitle 1\n## Subtitle 2\nContent here."
        self.assertEqual(extract_title_markdown(markdown), "Main Title")

    def test_title_with_whitespace(self):
        # Test a markdown string where the title has extra whitespace around it
        markdown = "    #    Main Title   \nSome content here."
        self.assertEqual(extract_title_markdown(markdown), "Main Title")

# Run the tests
if __name__ == "__main__":
    unittest.main()
