import json

def unescape_unicode(text):
    return json.loads(f'"{text}"')

def load_word_banlist(filepath):
    try:
        with open(filepath, 'r') as f:
            return [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Warning: Word banlist file not found at {filepath}. Proceeding without a banlist.")
        return []