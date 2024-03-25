from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from loguru import logger
class TextFilter:
    def __init__(self, stop_sentences):
        self.vectorizer = TfidfVectorizer()
        self.stop_sentences = stop_sentences
        self.stop_vectors = self.vectorizer.fit_transform(stop_sentences)

    def filter_texts(self, texts, threshold=0.5):
        text_vectors = self.vectorizer.transform(texts)
        excluded_texts = []

        for i, text_vector in enumerate(text_vectors):
            similarity = cosine_similarity(text_vector, self.stop_vectors)
            max_similarity = similarity.max()
            if max_similarity < threshold:
                excluded_texts.append(texts[i])

        return excluded_texts

# Пример использования:
# stop_sentences = [
#     "лист"
# ]

# filter_instance = TextFilter(stop_sentences)
# filtered_texts = filter_instance.filter_texts(names)



# if set(names)==set(filtered_texts):
#     print("Не изменился")
# else:
#     print("изменился")

# print("Тексты после фильтрации:")
# for text in filtered_texts:
#     print(text)
