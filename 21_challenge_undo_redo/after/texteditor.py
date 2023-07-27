from dataclasses import dataclass

@dataclass
class TextEditor:
    text: str = ""

    def insert(self, text: str) -> None:
        self.text += text

    def delete(self, num_chars: int) -> None:
        self.text = self.text[:-num_chars]

    def undo(self) -> None:
        self.text = self.text

    def redo(self) -> None:
        self.text = self.text

    def print_text(self) -> None:
        print(self.text)

