# Задача "Найдёт везде":
class WordsFinder:
    def __init__(self, *files):
        self.file_names = files
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r',  encoding='utf-8') as file:
                string = file.read().lower() # считывает единые строки, переводя их в нижний регистр
                for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        string = string.replace(punctuation, '')  # избавление от пунктуации в строке
                words = string.split()
                all_words[file_name] = words
        return all_words

    def find(self, word): #   Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла
        all_words = self.get_all_words()
        dict_ = {}
        for name, words in all_words.items():
            if word.lower() in words:
                dict_[name] = words.index(word.lower()) + 1
                return dict_
    def count(self, word): # Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла
       all_words = self.get_all_words()
       dict_ = {}
       for name, words in all_words.items():
           dict_[name] = words.count(word.lower())
           return dict_




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего