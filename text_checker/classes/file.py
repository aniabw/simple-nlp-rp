from text_checker.classes.data_source import Data_source_interface
from text_checker.classes.text_helper import Text_helper
import glob

class File(Data_source_interface):

    def __init__(self, dir_path, file_extention):
        self.dir_path = dir_path
        self.file_extention = file_extention

    def read_file(self, file_source):
        file = open(file_source, encoding="utf8")
        data = file.read()
        file.close()
        return data

    def get_files_from_directory_by_extention(self, path, extention):
        files = glob.glob(path + "*."+extention)
        return files

    def get_word_report(self):
        files = self.get_files_from_directory_by_extention(self.dir_path, self.file_extention)

        helper_set = {""}
        results = {}
        counter = 0
        for f_index, item in enumerate(files, start=0):
            data = self.read_file(item)
            th = Text_helper(data)

            sentences = th.get_sentences()
            tokens = th.split_words_by_punctuation()
            words = th.filter_out_punctuation(tokens)
            most_common_words = th.get_most_common_words(words)
            # interesting words in this case are those one which are longer that 10 :-D
            most_interesting_words = th.get_words_longer_than_10(most_common_words)

            occurance_in_file = {}
            for w_indx, word in enumerate(most_interesting_words, start=0):
                if w_indx < 5:
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

        return th.results_sorted_by_occurance(results)