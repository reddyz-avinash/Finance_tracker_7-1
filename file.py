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

