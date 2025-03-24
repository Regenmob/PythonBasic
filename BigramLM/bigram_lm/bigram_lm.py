import re

from .ngram_getter import NgramGetter
from .predicter import Predicter


class BigramLM:
    def __init__(self):
        self.ngram_getter = NgramGetter()
        self.predicter = Predicter()

    def run(self):
        with open("corpus.txt", "r", encoding="utf-8") as file:
            corpus = file.read()

        # Step 1: Split the corpus into sentences using punctuation (., !, ?)
        sentences = re.split(r"(?<=[.!?])\s+", corpus)
        ngram = self.ngram_getter.get_ngram(sentences)

        while True:
            user_input = input("Enter a word (or 'exit' to quit): ").lower().strip()
            if user_input == "exit":
                break
            prediction = self.predicter.predict(user_input, ngram)
            if prediction:
                predicted_word, probability = prediction
                print(
                    f'Predicted next word: "{predicted_word}" with {probability:.2f}% probability.'
                )
            else:
                print("None")