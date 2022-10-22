# coding=utf-8
# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2
sentences_1d = [(j.lower()).rstrip(',') for sub in list(map(lambda a: a.split(" "), sentences)) for j in sub]
set_sentences = set(sentences_1d)
dict_sentences = { a : 0 for a in sentences_1d }
for i in range(len(sentences_1d)):
    if sentences_1d[i] in set_sentences:
        dict_sentences[sentences_1d[i]]+=1
list1 = (sorted(dict_sentences.items(), key=lambda item: item[1], reverse=True))[:3]
[print(j) for i in list1 for j in i]


# Good luck! You can write all the code in this file.
