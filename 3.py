import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        result = dict()

        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as f:
                result[file_name] = re.sub(r'( - )|[,;:.=!?]', ' ', f.read()).lower().split()

        return result

    def find(self, word):
        result = dict()
        word = word.lower()

        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word) + 1

        return result

    def count(self, word):
        result = dict()
        word = word.lower()

        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.count(word)

        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

# finder1 = WordsFinder('All/Walt Whitman - O Captain! My Captain!.txt',
#                       'All/Rudyard Kipling - If.txt',
#                       'All/Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))
