import unittest

from nodes import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestNode(unittest.TestCase):
    def test_split_nodes(self):
        self.assertEqual(True, True)

class TestExtractNodes(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), output)

        no_image = "This is text with no image"
        self.assertEqual(extract_markdown_images(no_image), [])

        malformed_image = "This is text with ![borked]() image"
        self.assertEqual(extract_markdown_images(malformed_image), [("borked", "")])

    def test_extract_markdown_links(self):
        links = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        output = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(links), output)
 
if __name__ == "__main__":
    unittest.main()
