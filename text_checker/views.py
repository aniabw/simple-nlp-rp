from django.shortcuts import render
from text_checker.classes.file_word_report import File_word_report

files_documents_path = "text_checker/assets/documents/textdocs/"
files_extention = "txt"

def text_checker(request):
    wr = File_word_report(files_documents_path, files_extention)
    word_report = wr.get_word_report()

    context = {'interesting_words': word_report}
    return render(request, 'index.html', context)
