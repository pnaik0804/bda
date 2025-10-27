import sys

def main():
    # Check for input arguments
    if len(sys.argv) < 2:
        print("Usage: python wordcount.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    word_count = {}

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                words = line.split()  # Split by whitespace

                for word in words:
                    if word:
                        word = word.strip().upper()  # Convert to uppercase
                        word_count[word] = word_count.get(word, 0) + 1

        # Print results (like reducer output)
        for word, count in word_count.items():
            print(f"{word}\t{count}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


python wordcount.py input.txt

HADOOP  2
MAPREDUCE       1
EXAMPLE 2