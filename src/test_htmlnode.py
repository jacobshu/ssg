import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("strong", "strong text")
        node2 = HTMLNode("a", "link text", None, { "href": "test.com" })
        self.assertEqual(repr(node), "HTMLNode(strong, strong text, None, None)")
        self.assertEqual(repr(node2), "HTMLNode(a, link text, None, {'href': 'test.com'})")

    def test_props_to_html(self):
        node = HTMLNode("a", "test", None, { "href": "test.org" })
        node2 = HTMLNode("strong", "test", None, { "data-id": "the-id", "style": "color: red;" })
        self.assertEqual(node.props_to_html(), " href=\"test.org\"")
        self.assertEqual(node2.props_to_html(), " data-id=\"the-id\" style=\"color: red;\"")

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"}) 

        self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(leaf2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        parent = ParentNode("div", [ LeafNode("p", "content") ], { "style": "color: lime;" })
        empty_children = ParentNode("div", [])
        none_children = ParentNode("div", None)
        nested_parents = ParentNode("li", [ 
            ParentNode("div", [ 
                LeafNode("a", "link", { "href": "dot.com" }) 
            ], { "id": "nested" })
        ])

        self.assertEqual(parent.to_html(), "<div style=\"color: lime;\"><p>content</p></div>")
        self.assertRaises(ValueError, empty_children.to_html)
        self.assertRaises(ValueError, none_children.to_html)
        self.assertEqual(nested_parents.to_html(), 
            f"<li><div id=\"nested\"><a href=\"dot.com\">link</a></div></li>")


if __name__ == "__main__":
    unittest.main()
