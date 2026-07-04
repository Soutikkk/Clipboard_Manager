# Clipboard Manager (using `clip`)

A simple, command-line based clipboard manager built with Python. It allows you to save, list, copy, search, and manage your clipboard history efficiently right from your terminal.

## Features
- **Save**: Instantly save your current clipboard content.
- **List**: View a history of your saved clipboard items (truncated to 50 characters for readability).
- **Copy**: Easily copy a saved item back to your clipboard using its index.
- **Search**: Find specific snippets in your history using keywords.
- **Delete/Clear**: Remove specific items or clear the entire history.
- **Duplicate Handling**: Automatically moves duplicated content to the top of your history instead of saving it twice.
- **History Limit**: Stores up to the last 50 clipboard items.

## Requirements
- Python 3.6+
- `pyperclip` package

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Soutikkk/Clipboard_Manager.git
   cd Clipboard_Manager
   ```

2. Install the required dependency:
   ```bash
   pip install pyperclip
   ```

## Usage
You can run the script directly using Python:

```bash
python clip.py [command] [arguments]
```

### Commands

* **Save the current clipboard content**:
  ```bash
  python clip.py save
  ```

* **List all saved clipboard entries**:
  ```bash
  python clip.py list
  ```

* **Copy an entry back to the clipboard (using its index from `list`)**:
  ```bash
  python clip.py copy <index>
  ```

* **Search for a keyword in your history**:
  ```bash
  python clip.py search "keyword"
  ```

* **Delete a specific entry**:
  ```bash
  python clip.py delete <index>
  ```

* **Clear the entire clipboard history**:
  ```bash
  python clip.py clear
  ```

## Data Storage
The clipboard history is stored locally in your user's home directory in a JSON file named `~/.clipstack.json`.
