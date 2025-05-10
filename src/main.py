import itertools
import re
import os

# STEP 1: Generate all 4-letter combinations
def generate_all_combinations():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    all_combinations = [''.join(letters) for letters in itertools.product(alphabet, repeat=4)]
    return all_combinations

# STEP 2: Filter for catchy/brandable names
def is_catchy(word):
    vowels = 'aeiou'
    tech_endings = ('x', 'z', 'o', 'n', 'r')
    ai_keywords = ('ai', 'ml', 'nn')
    
    # Must contain at least one vowel
    if not any(v in word for v in vowels):
        return False
    
    # No double letters (like 'zz', 'aa')
    if re.search(r'(.)\1', word):
        return False

    # Optional pattern logic for AI-style or techy endings
    if word.endswith(tech_endings) or 'ai' in word:
        return True

    return False

# STEP 3: Write output files
def save_to_file(filename, word_list, comma_separated=False):
    with open(filename, 'w') as f:
        if comma_separated:
            f.write(','.join(word_list))
        else:
            f.write('\n'.join(word_list))

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # go to project root
    all_output = os.path.join(base_dir, 'all_4_letter_names.txt')
    catchy_output = os.path.join(base_dir, 'cooler_4_letter_names.txt')

    print("Generating all 4-letter combinations...")
    all_names = generate_all_combinations()
    save_to_file(all_output, all_names, comma_separated=True)
    print(f"Saved {len(all_names)} total combinations to {all_output}")

    print("Filtering for catchy names...")
    catchy_names = [name for name in all_names if is_catchy(name)]
    save_to_file(catchy_output, catchy_names)
    print(f"Saved {len(catchy_names)} catchy combinations to {catchy_output}")

if __name__ == "__main__":
    main()
