import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if len(delimiter) == 0 or delimiter == None:
        raise ValueError("must provide a delimiter")

    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            new_nodes.append(node)
        else:
            split = node.split(delimiter)
            if len(split) % 2 != 0:
                raise Exception("unmatched delimiter in markdown")
            for n, i in split:
                if i % 2 == 0:
                    new_nodes.append(TextNode(n.text, text_type))
                else:
                    new_nodes.append(n)
    return new_nodes

def extract_markdown_images(text):
    md_images= re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return md_images
