class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] = None):
        self.tag = tag 
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string = ""
        if self.props is None:
            return string
        for key in self.props:
            string += f' {key}="{self.props[key]}"'
        return string

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

