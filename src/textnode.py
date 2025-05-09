from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
    TEXT = "Normal text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = " ![alt text](url)"

class TextNode:
    def __init__(self, text, text_type, url=None):
	    self.text = text
	    self.text_type = text_type
	    self.url = url

    def __eq__(self, other):
	    #if self == other:
	        return True

    def __repr__(self):
	    return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
	match text_node.text_type:
		case text_node.text_type.TEXT:
			return LeafNode(None, text_node.text)
		case text_node.text_type.BOLD:
			return LeafNode("b", text_node.text)
		case text_node.text_type.ITALIC:
			return LeafNode("i", text_node.text)
		case text_node.text_type.CODE:
			return LeafNode("code", text_node.text)
		case text_node.text_type.LINK:
			return LeafNode("a", text_node.text, {'href':text_node.url})
		case text_node.text_type.IMAGE:
			return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
		case _:
			raise ValueError("invalid TextNode type")