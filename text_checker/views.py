from django.shortcuts import render
import nltk
nltk.download('punkt')
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import collections

def text_checker(request):

    file = open('text_checker/assets/documents/textdocs/doc1.txt', encoding="utf8")
    data = file.read()
    file.close()

    # print first sentence
    sentences = sent_tokenize(data)

    # words with what's what s
    tokens = word_tokenize(data)
    # filter out punctuation
    words = [word for word in tokens if word.isalpha()]
    most_common_words = collections.Counter(words).most_common()
    words_longer_than_10 = [w for w in most_common_words if len(w[0]) > 10]

    interesting_words = {}
    exists_in_sentence = {}
    for c_indx, word in enumerate(words_longer_than_10, start=0):
        if c_indx < 10:
            for s_indx, sentence in enumerate(sentences, start=0):
                if word[0] in sentence:
                    exists_in_sentence[s_indx] = sentence
            interesting_words[c_indx] = {"word": word[0],"occurance": word[1],"sentences": exists_in_sentence}

    context = {'most_common_words': most_common_words[:10], 'interesting_words': interesting_words}
    return render(request, 'index.html', context)