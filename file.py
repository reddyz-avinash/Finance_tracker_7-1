# text_input.py
import os
import re
import langdetect
import logging
from datetime import datetime

# Setup logging
def setup_logger():
    logging.basicConfig(
        filename='app.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
def get_stats(self):
        return {
            'length': len(self.raw_text),
            'clean_length': len(self.cleaned_text),
            'num_lines': self.raw_text.count('\n'),
            'num_words': len(self.cleaned_text.split())
        }

def create_sample_file(path):
    sample_text = """Hello! This is a sample document.
It contains multiple lines, punctuation marks, and mixed-case letters.
We're testing how the Text Analyzer processes this input."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(sample_text)
    logging.info("Sample file created.")

def menu():
    print("\n=== Text Input Module ===")
    print("1. Load and clean text")
    print("2. Detect language")
    print("3. Show stats")
print("4. Save cleaned text")
    print("5. Exit")

def main():
    path = "sample.txt"
    if not os.path.exists(path):
        create_sample_file(path)

    processor = TextLoader(path)

    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == '1':
            processor.read_file()
            processor.clean_text()
            print("Text loaded and cleaned.")
        elif choice == '2':
            lang = processor.detect_language()
            print("Detected Language:", lang)
        elif choice == '3':
            stats = processor.get_stats()
            for k, v in stats.items():
                print(f"{k}: {v}")
        elif choice == '4':
            processor.save_cleaned()
            print("Cleaned text saved.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
    if _name_ == "_main_":
    main()
