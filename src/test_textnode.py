import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC, "https://website")
        node4 = TextNode("This is a text node", TextType.ITALIC, "https://website")
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        node3 = TextNode("This is a code node", TextType.CODE)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node3)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("image", TextType.IMAGE, "https://site.image")
        node3 = TextNode("rm -rf", TextType.CODE)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")
        self.assertEqual(repr(node2), "TextNode(image, image, https://site.image)")
        self.assertEqual(repr(node3), "TextNode(rm -rf, code, None)")

    def test_text_node_to_html_node(self):
        text = text_node_to_html_node(TextNode("text node", TextType.TEXT)).to_html()
        bold = text_node_to_html_node(TextNode("bold node", TextType.BOLD)).to_html()
        italic = text_node_to_html_node(TextNode("italic node", TextType.ITALIC)).to_html()
        code = text_node_to_html_node(TextNode("code node", TextType.CODE)).to_html()
        link = text_node_to_html_node(TextNode("link node", TextType.LINK, "target.ninja")).to_html()
        image = text_node_to_html_node(TextNode("image node", TextType.IMAGE, "image.com")).to_html()

        self.assertEqual(text, "text node")
        self.assertEqual(bold, "<b>bold node</b>")
        self.assertEqual(italic, "<i>italic node</i>")
        self.assertEqual(code, "<code>code node</code>")
        self.assertEqual(link, "<a href=\"target.ninja\">link node</a>")
        self.assertEqual(image, "<img src=\"image.com\" alt=\"image node\"></img>")
if __name__ == "__main__":
    unittest.main()
