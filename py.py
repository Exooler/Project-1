
def delete_word_from_file(filename: str, target: str) -> bool:
    """
    Removes all occurrences of `target` from the given .txt file.

    Returns True if target was found and removed, False otherwise.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        if target not in content:
            return False

        updated_content = content.replace(target, '')

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        return True

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
filename = input("Enter the filename: ")
target = input("Enter the word/character to delete: ")

delete_word_from_file(filename, target)
