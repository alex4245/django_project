import time
from googletrans import Translator


def translate(dest, words=None):
    translator = Translator()
    if not words:
        return []

    c = 0
    while True:
        c += 1
        if c == 5:
            raise Exception

        try:
            return translator.translate(words, dest=dest)
        except AttributeError:
            time.sleep(1)
            continue
