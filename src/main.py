import csv
# Generate 4-letter words
def generate_words():
    # Create an alphabet string (26 letters)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Use itertools.product to generate all possible combinations of 4 characters
    return list(itertools.product(alphabet, repeat=4))

# Process data function
def process_data(data):
    result = []
    for row in data:
        word = ''.join(row)
        result.append(word)

    return result

# Main function
def main():
    words = generate_words()
    # Write each word on a new line to a CSV file
    with open('data.csv', 'w') as f:
        writer = csv.writer(f)
        for word in words:
            writer.writerow([word])
if __name__ == "__main__":
    main()