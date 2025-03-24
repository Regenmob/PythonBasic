class Predicter:
    def predict(self, word: str, ngram: dict) -> None | tuple[str, float]:
        if word in ngram:
            next_word_data = ngram[word]
            total_occurrences = sum(next_word_data.values())
            # Find the most common next word
            predicted_word = None
            max_count = 0
            for word, count in next_word_data.items():
                if count > max_count:
                    max_count = count
                    predicted_word = word
            probability = (max_count / total_occurrences) * 100
            return predicted_word, probability
        else:
            return None
