import tkinter as tk
from tkinter import simpledialog, messagebox
import pyperclip as pc

# Debugging tools
from memory_profiler import profile




class ClipBoardManager:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("TheCopyPaster")
        # Empty window initialised

        self.clipboard_history = []

        # Creating a frame within the window
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Creating copy to clipboard button complete with function
        self.add_button = tk.Button(
            self.frame, text="Copy to Clipboard", command=self.copy_to_clipboard
        )
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.view_button = tk.Button(
            self.frame, text="View Clips", command=self.view_history
        )
        self.view_button.pack(side=tk.LEFT, padx=5)

        self.paste_button = tk.Button(
            self.frame, text="Paste from clipboard", command=self.paste_from_clipboard
        )
        self.paste_button.pack(side=tk.LEFT, padx=5)

        # Copies a text to the system clipboard
    @profile
    # track method memory usage
    def copy_to_clipboard(self):
        text = simpledialog.askstring("Input", "Enter text to copy to clipboard: ")
        if text:
            pc.copy(text)
            self.clipboard_history.append(text)
            messagebox.showinfo("Succces", "Text copied to clipboard")

    # View history of copied text ========= A list of all past copied texts
    @profile
    def view_history(self):
        history = "\n".join(self.clipboard_history)
        messagebox.showinfo(
            "Clipboard History", history if history else "No history available"
        )
        # Whats this method checking called again ???

    # Paste from our clipboard to the system clipboard
    @profile
    def paste_from_clipboard(self):
        if not self.clipboard_history:
            #  if clipboard_history is empty
            messagebox.showinfo(
                "Paste from clipboard", "Clipboard history is empty!!🙈"
            )
            return
            # Exit function if clipboard history
        selected_text = simpledialog.askstring(
            "Paste from clipboard",
            "Enter the index of the text to paste (0-based index): ",
        )
        try:
            index = int(selected_text)
            if 0 <= index < len(self.clipboard_history):
                # Specify upper and lower index boundaries to accept
                pc.copy(self.clipboard_history[index])
                messagebox.showinfo("Success", "Text copied to clipboard")
            else:
                messagebox.showwarning("Invalid Index", "Index out of range")
        except ValueError:
            messagebox.showwarning("Invalid input", "Please enter a valid input 😒")
            # Out of range exception handled by manually by if statement , exception handles value erro instead


if __name__ == "__main__":
    root = tk.Tk()
    app = ClipBoardManager(root)
    root.mainloop()
