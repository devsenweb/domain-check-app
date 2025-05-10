import itertools
import re
import os

def is_genai_brandable(word):
    vowels = 'aeiou'
    ai_signals = ['ai', 'ml', 'nn', 'dl']
    strong_starts = ('v', 'n', 'x', 'z', 'g')
    strong_ends = ('x', 'z', 'o', 'n', 'r')

    if len(word) != 4:
        return False
    if word[0] not in strong_starts:
        return False
    if word[-1] not in strong_ends:
        return False
    if not any(v in word for v in vowels):
        return False
    if re.search(r'(.)\1', word):  # avoid repeated characters
        return False
    if not any(sig in word for sig in ai_signals) and 'a' not in word and 'i' not in word:
        return False
    return True

def generate_ai_focused_names():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    all_combinations = [''.join(p) for p in itertools.product(alphabet, repeat=4)]
    filtered_names = [w for w in all_combinations if is_genai_brandable(w)]

    # Save next to script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(base_dir, 'ai_focused_4_letter_names.txt')
    with open(out_file, 'w') as f:
        f.write('\n'.join(filtered_names))

    print(f"{len(filtered_names)} AI-flavored brandable names saved to {out_file}")

if __name__ == "__main__":
    generate_ai_focused_names()
