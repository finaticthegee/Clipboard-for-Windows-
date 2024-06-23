# Clipboard Manager

## Description

Clipboard Manager is a simple Python application that helps you manage your clipboard history. It allows you to copy text to the clipboard, view the clipboard history, search through the clipboard history, and paste text from the clipboard history. This application is built using the `tkinter` library for the graphical user interface and `pyperclip` for clipboard management.

## Features

- Copy text to the clipboard.
- View the clipboard history in a separate window.
- Search through the clipboard history.
- Paste text from the clipboard history by selecting it from a Listbox.
- Clear clipboard history (upcoming feature).
- Delete specific items from clipboard history (upcoming feature).

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/clipboard-manager.git
   cd clipboard-manager
   ```

2. **Install the required dependencies**:
   ```bash
   pip install pyperclip
   ```

## Usage

1. **Run the application**:

   ```bash
   python clipboard_manager.py
   ```

2. **Using the Application**:
   - **Copy to Clipboard**: Click the "Copy to Clipboard" button and enter the text you want to copy.
   - **View Clipboard History**: Click the "View Clipboard History" button to see all previously copied texts in a separate window.
   - **Search History**: Enter a search term in the search box and click the "Search" button to find matching entries in the clipboard history.
   - **Paste from Clipboard**: Select an item from the Listbox and click the "Paste from Clipboard" button to copy the selected item back to the clipboard.

## Code Overview

### `ClipboardManager` Class

- **Attributes**:

  - `self.root`: Main application window.
  - `self.clipboard_history`: List to store clipboard history.
  - `self.frame`: Frame widget to hold buttons and entry.
  - `self.add_button`: Button to copy text to clipboard.
  - `self.view_button`: Button to view clipboard history.
  - `self.paste_button`: Button to paste text from clipboard.
  - `self.search_entry`: Entry widget for search input.
  - `self.search_button`: Button to search clipboard history.
  - `self.history_listbox`: Listbox widget to display clipboard history.

- **Methods**:
  - `__init__(self, root)`: Initializes the GUI components and sets up the main window.
  - `copy_to_clipboard(self)`: Prompts the user for text and copies it to the clipboard. Updates clipboard history.
  - `view_history(self)`: Opens a new window displaying the clipboard history.
  - `paste_from_clipboard(self)`: Copies the selected item from the Listbox to the clipboard.
  - `search_history(self)`: Searches the clipboard history for matching entries.
  - `update_history_listbox(self)`: Updates the Listbox with the current clipboard history.

## Upcoming Features

- **Clear Clipboard History**: Add functionality to clear all items from the clipboard history.
- **Delete Specific Item**: Allow users to delete specific items from the clipboard history.
- **Drag-and-Drop Reordering**: Enable drag-and-drop functionality for reordering clipboard history.

## Contributing

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes**:
   ```bash
   git commit -m "Add your commit message"
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a pull request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please open an issue on the GitHub repository.
