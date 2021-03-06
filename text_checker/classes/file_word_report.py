from text_checker.classes.text_helper import Text_helper
from text_checker.classes.word_report import Word_report
from simple_nlp.classes.file import File

class File_word_report(Word_report):
    def __init__(self, dir_path, extention):
        self.dir_path = dir_path
        self.file = File(self.dir_path, extention)
        self.word_length = 10

    def get_word_report(self):
        helper_set = {""}
        results = {}
        counter = 0

        for f_index, item in enumerate(self.file.get_files_from_directory_by_extention(), start=0):
            file_data = self.file.read_file(item)
            th = Text_helper(file_data)

            sentences = th.get_sentences()
            tokens = th.split_words_by_punctuation()
            words = th.filter_out_punctuation(tokens)
            most_common_words = th.get_most_common_words(words)
            most_interesting_words = th.get_words_longer_than(most_common_words, self.word_length)

            if most_interesting_words:
                occurance_in_file = {}
                for w_indx, word in enumerate(most_interesting_words, start=0):
                    if w_indx < 10:
                        exists_in_sentence = {}
                        for s_indx, sentence in enumerate(sentences, start=0):
                            if word[0] in sentence:
                                exists_in_sentence[s_indx] = th.get_sentences_with_highlited_words(sentence, word[0])

                        occurance_in_file[f_index] = item.replace(self.dir_path, '')

                        if word[0] not in helper_set:
                            results[counter] = {
                                "word": word[0],
                                "occurance": word[1],
                                "filename": item.replace(self.dir_path, ''),
                                "sentences": exists_in_sentence
                            }
                        else:
                            for k, v in results.items():
                                if v['word'] == word[0]:
                                    v['sentences'].update(exists_in_sentence)
                                    v['filename'] = v['filename'] + ', ' + item.replace(self.dir_path, '')
                                    v['occurance'] = v['occurance'] + word[1]

                        helper_set.add(word[0])
                        counter += 1
            else:
                raise ValueError("No word found with at least %s characters." % self.word_length)

        return th.results_sorted_by_occurance(results)