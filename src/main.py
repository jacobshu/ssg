from textnode import TextNode, TextType

def main():
    code = TextNode("print('hello world')", TextType.CODE)
    print(code)
    code2 = TextNode("print('hello world')", TextType.CODE)

    print(code == code2)

if __name__ == "__main__":
    main()
