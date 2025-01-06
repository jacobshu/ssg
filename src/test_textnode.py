import unittest

from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()
