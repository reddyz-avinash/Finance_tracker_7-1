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
def demo_statistics():
    from text_input import TextLoader
    loader = TextLoader("sample.txt")
    loader.read_file()
    loader.clean_text()

    ts = TextStats(loader.cleaned_text)
    ts.tokenize_words()
    ts.tokenize_sentences()
    ts.tokenize_paragraphs()

    print("Words:", ts.word_count())
    print("Sentences:", ts.sentence_count())
    print("Paragraphs:", ts.paragraph_count())
    print("Top 10 Words:", ts.most_common_words())

    ts.generate_wordcloud()
    ts.export_report()

if _name_ == "_main_":
    demo_statistics()
