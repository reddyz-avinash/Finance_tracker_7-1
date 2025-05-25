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
setup_logger()

class TextLoader:
    def _init_(self, file_path):
        self.file_path = file_path
        self.raw_text = ""
        self.cleaned_text = ""

    def file_exists(self):
        exists = os.path.exists(self.file_path)
        logging.info(f"File exists check for {self.file_path}: {exists}")
        return exists

    def read_file(self):
        if not self.file_exists():
            logging.error(f"File {self.file_path} not found.")
            raise FileNotFoundError("File does not exist.")
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.raw_text = f.read()
        logging.info("File read successfully.")

    def clean_text(self):
        if not self.raw_text:
            logging.warning("No raw text to clean.")
            return ""
        text = self.raw_text
        text = text.lower()
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s]', '', text)
        self.cleaned_text = text
        logging.info("Text cleaned.")
        return text

    def detect_language(self):
        try:
            lang = langdetect.detect(self.cleaned_text)
            logging.info(f"Detected language: {lang}")
            return lang
        except:
            logging.error("Language detection failed.")
            return "unknown"

    def save_cleaned(self, output_file='cleaned_text.txt'):
        if not self.cleaned_text:
            logging.warning("No cleaned text to save.")
            return
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(self.cleaned_text)
        logging.info(f"Cleaned text saved to {output_file}")

