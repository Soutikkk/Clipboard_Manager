import argparse
import json
import os
import pyperclip

CLIP_FILE = os.path.expanduser("~/.clipstack.json")
MAX_ITEMS = 50

def load_data():
    """Load clipboard history from the JSON file."""
    if not os.path.exists(CLIP_FILE):
        return []
    try:
        with open(CLIP_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # Return an empty list if the file is corrupted or unreadable
        return []

def save_data(data):
    """Save clipboard history to the JSON file."""
    try:
        with open(CLIP_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error saving to file: {e}")

def save_clip():
    """Read current clipboard content and store it."""
    current_clip = pyperclip.paste()
    if not current_clip.strip():
        print("Clipboard is empty or contains only whitespace.")
        return

    data = load_data()
    
    # Avoid duplicates: remove it if it already exists so we can move it to the top
    if current_clip in data:
        data.remove(current_clip)
    
    # Keep newest items at the top
    data.insert(0, current_clip)
    
    # Limit history to the last MAX_ITEMS
    if len(data) > MAX_ITEMS:
        data = data[:MAX_ITEMS]
        
    save_data(data)
    print("Clipboard content saved successfully.")

def list_clips():
    """Display saved clipboard entries."""
    data = load_data()
    if not data:
        print("Clipboard history is empty.")
        return
        
    print("Clipboard History:")
    for idx, item in enumerate(data):
        # Replace newlines with spaces for a single-line display
        display_item = item.replace("\n", " ").replace("\r", "")
        # Truncate long entries to 50 characters
        if len(display_item) > 50:
            display_item = display_item[:47] + "..."
            
        print(f"[{idx}] {display_item}")

def copy_clip(index):
    """Copy a saved entry back to the clipboard."""
    data = load_data()
    if not data:
        print("Clipboard history is empty.")
        return
        
    if 0 <= index < len(data):
        pyperclip.copy(data[index])
        print(f"Item at index {index} copied to clipboard.")
    else:
        print(f"Invalid index: {index}. Valid indices are 0 to {len(data) - 1}.")

def delete_clip(index):
    """Remove a specific entry from the history."""
    data = load_data()
    if not data:
        print("Clipboard history is empty.")
        return
        
    if 0 <= index < len(data):
        deleted_item = data.pop(index)
        save_data(data)
        print(f"Item at index {index} deleted.")
    else:
        print(f"Invalid index: {index}. Valid indices are 0 to {len(data) - 1}.")

def clear_clips():
    """Delete all saved entries."""
    save_data([])
    print("Clipboard history cleared.")

def search_clips(keyword):
    """Search for a keyword in the clipboard history."""
    data = load_data()
    if not data:
        print("Clipboard history is empty.")
        return
        
    results = [(idx, item) for idx, item in enumerate(data) if keyword.lower() in item.lower()]
    
    if not results:
        print(f"No entries found containing '{keyword}'.")
        return
        
    print(f"Search results for '{keyword}':")
    for idx, item in results:
        display_item = item.replace("\n", " ").replace("\r", "")
        if len(display_item) > 50:
            display_item = display_item[:47] + "..."
        print(f"[{idx}] {display_item}")

def main():
    parser = argparse.ArgumentParser(description="clip - A simple command-line clipboard manager.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Save command
    parser_save = subparsers.add_parser("save", help="Read current clipboard content and store it")
    
    # List command
    parser_list = subparsers.add_parser("list", help="Display saved clipboard entries with index numbers")
    
    # Copy command
    parser_copy = subparsers.add_parser("copy", help="Copy a saved entry back to clipboard")
    parser_copy.add_argument("index", type=int, help="Index of the item to copy")
    
    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Remove a specific entry")
    parser_delete.add_argument("index", type=int, help="Index of the item to delete")
    
    # Clear command
    parser_clear = subparsers.add_parser("clear", help="Delete all saved entries")
    
    # Search command (Optional implementation)
    parser_search = subparsers.add_parser("search", help="Search clipboard history")
    parser_search.add_argument("keyword", type=str, help="Keyword to search for")
    
    args = parser.parse_args()
    
    if args.command == "save":
        save_clip()
    elif args.command == "list":
        list_clips()
    elif args.command == "copy":
        copy_clip(args.index)
    elif args.command == "delete":
        delete_clip(args.index)
    elif args.command == "clear":
        clear_clips()
    elif args.command == "search":
        search_clips(args.keyword)
    else:
        # Print help if no command is provided
        parser.print_help()

if __name__ == "__main__":
    main()
