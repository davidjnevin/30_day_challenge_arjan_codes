from controller import TextEditorController
from commands import Insert, Delete, PrintText
from texteditor import TextEditor

def main() -> None:
    # Test the text editor
    editor = TextEditor()

    # create a TextEditor controller
    controller = TextEditorController()

    # Since there is no text, these commands should do nothing
    controller.undo()
    controller.redo()

    controller.execute(Insert(editor, "Hello"))
    controller.execute(Insert(editor, " World!"))

    controller.execute(PrintText(editor))

    controller.execute(Delete(editor, 6))
    controller.undo()
    controller.execute(PrintText(editor))

    controller.redo()
    # controller.execute(PrintText(editor))

    controller.execute(Insert(editor, "!!!"))

    # controller.execute(PrintText(editor))

    controller.undo()
    controller.undo()
    controller.execute(PrintText(editor))

    print(TextEditor)


if __name__ == "__main__":
    main()
