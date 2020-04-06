import nltk
nltk.download('punkt')
from nltk import word_tokenize, sent_tokenize
import collections
from django.utils.safestring import mark_safe


class Text_helper():
    def __init__(self, data):
        self.data = data

    def get_sentences(self):
        return sent_tokenize(self.data)

    def split_words_by_punctuation(self):
        return word_tokenize(self.data)

    def filter_out_punctuation(self, tokens):
        return [word for word in tokens if word.isalpha()]

    def get_most_common_words(self, words):
        return collections.Counter(words).most_common()

    def get_words_longer_than(self, most_common_words, lenght):
        return [w for w in most_common_words if len(w[0]) > lenght]

    def get_sentences_with_highlited_words(self, sentence, word):
        return mark_safe(sentence.replace(word, '<span class="bg-primary">' + word + '</span>'))

    def results_sorted_by_occurance(self, results):
        return {k: v for k, v in sorted(results.items(), key=lambda item: item[1]['occurance'], reverse=True)}

