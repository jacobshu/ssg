import unittest

from nodes import split_nodes_delimiter, extract_markdown_images
from textnode import TextNode, TextType

class TestNode(unittest.TestCase):
    def test_split_nodes(self):
        self.assertEqual(True, True)

class TestExtractNodes(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), output)

if __name__ == "__main__":
    unittest.main()
