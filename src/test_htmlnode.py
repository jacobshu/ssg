import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("strong", "strong text")
        node2 = HTMLNode("a", "link text", None, { "href": "test.com" })
        self.assertEqual(repr(node), "HTMLNode(strong, strong text, None, None)")
        self.assertEqual(repr(node2), "HTMLNode(a, link text, None, {'href': 'test.com'})")

    def test_props_to_html(self):
        node = HTMLNode("a", "test", None, { "href": "test.org" })
        node2 = HTMLNode("strong", "test", None, { "data-id": "the-id", "style": "color: red;" })
        self.assertEqual(node.props_to_html(), "href=\"test.org\"")
        self.assertEqual(node2.props_to_html(), "data-id=\"the-id\" style=\"color: red;\"")

if __name__ == "__main__":
    unittest.main()
