from dataclasses import dataclass, field

from edit import Edit

@dataclass
class TextEditorController:

    undo_stack: list[Edit] = field(default_factory=list)
    redo_stack: list[Edit] = field(default_factory=list)

    def execute(self, edit: Edit):
        edit.execute()
        self.redo_stack.clear()
        self.undo_stack.append(edit)

    def undo(self):
        if not self.undo_stack:
            return
        edit = self.undo_stack.pop()
        edit.undo()
        self.redo_stack.append(edit)
        print(self.undo_stack)

    def redo(self):
        if not self.redo_stack:
            return
        edit = self.redo_stack.pop()
        edit.redo()
        self.undo_stack.append(edit)
