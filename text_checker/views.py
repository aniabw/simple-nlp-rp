from django.shortcuts import render
from text_checker.classes.file import File


def text_checker(request):
    file = File("text_checker/assets/documents/textdocs/", "txt")

    context = {'interesting_words': file.get_word_report()}
    return render(request, 'index.html', context)
