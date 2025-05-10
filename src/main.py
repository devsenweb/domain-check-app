import csv
import itertools

# Generate 4-letter words
def generate_words():
    # Create an alphabet string (26 letters)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Use itertools.product to generate all possible combinations of 4 characters
    return itertools.product(alphabet, repeat=4)

# Main function
def main():
    with open('words.txt', 'w') as f:
        # Generate words and join them with commas
        words = [ ''.join(word) for word in generate_words() ]
        f.write(','.join(words))
    
    print("Words have been written to words.txt")

if __name__ == "__main__":
    main()