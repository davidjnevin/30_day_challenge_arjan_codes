from dataclasses import dataclass

from texteditor import TextEditor


@dataclass
class Insert:
    editor: TextEditor
    text: str

    @property
    def edit_details(self):
        return f"{self.text} inserted into editor"

    def execute(self):
        self.editor.insert(self.text)
        print(self.edit_details)

    def undo(self) -> None:
        self.editor.undo()
        print(f"Undid insertion of {self.text}")

    def redo(self) -> None:
        self.editor.redo()
        print(f"Re-inserted insertion of {self.text}")


@dataclass
class Delete:
    editor: TextEditor
    num_chars: int

    @property
    def edit_details(self) -> str:
        return f"{self.num_chars} deleted from editor"

    def execute(self) -> None:
        self.editor.delete(self.num_chars)
        print(self.edit_details)

    def undo(self) -> None:
        self.editor.undo()
        print(f"Undid deletion of {self.num_chars}")

    def redo(self) -> None:
        self.editor.redo()
        print(f"Re-deleted of {self.num_chars}")

@dataclass
class PrintText:
    editor: TextEditor

    @property
    def edit_details(self):
        return "Printed editor"

    def execute(self):
        # self.editor.print_text()
        print(self.edit_details)

    def undo(self) -> None:
        # breakpoint()
        ...

    def redo(self) -> None:
        ...
