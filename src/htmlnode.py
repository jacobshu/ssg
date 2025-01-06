class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        p = " "
        if self.props != None:
            for key, value in self.props.items():
                p += f"{key}=\"{value}\" "
        return p.rstrip()

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


    def to_html(self):
        if self.value == None:
            raise ValueError("all leaf nodes must have a value")

        if self.tag == None:
            return f"{self.value}"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")

        if self.children == None or len(self.children) == 0:
            raise ValueError("ParentNode must have children")

        doc = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            doc += child.to_html()
        return f"{doc}</{self.tag}>"
