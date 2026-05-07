import os
from collections import Counter

STOP_WORDS = {
    'the','a','an','and','or','but','in','on','at','to','for',
    'of','with','is','it','this','that','was','are','be','as','by'
}

def read_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    if not filepath.endswith('.txt'):
        raise ValueError("Only .txt files are supported.")
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    return len(text)

def count_lines(text):
    return len(text.splitlines())

def most_common_word(text, top=10):
    words = [w.strip('.,!?";:()').lower() for w in text.split()]
    words = [w for w in words if w and w not in STOP_WORDS and len(w) > 1]
    return Counter(words).most_common(top)

def analyze_file(filepath):
    try:
        text = read_file(filepath)

        words      = count_words(text)
        characters = count_characters(text)
        lines      = count_lines(text)
        common     = most_common_word(text)

        print(f"\n--- Analysis of '{filepath}' ---")
        print(f"  Words      : {words}")
        print(f"  Characters : {characters}")
        print(f"  Lines      : {lines}")
        print(f"\n  Top 10 most common words:")
        for word, count in common:
            print(f"    {word:<20} {count}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    filepath = input("Enter path to your .txt file: ")
    analyze_file(filepath)