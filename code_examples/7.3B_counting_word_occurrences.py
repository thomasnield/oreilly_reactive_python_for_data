from rx import Observable
import re


def words_from_file(file_name):
    file = open(file_name)

    # parse, clean, and push words in text file
    return Observable.from_(file) \
        .flat_map(lambda s: Observable.from_(s.split())) \
        .map(lambda w: re.sub(r'[^\w\s]', '', w)) \
        .filter(lambda w: w != "") \
        .map(lambda w: w.lower()) \



def word_counter(file_name):

    # count words using `group_by()`
    # tuple the word with the count
    return words_from_file(file_name) \
        .group_by(lambda word: word) \
        .flat_map(lambda grp: grp.count().map(lambda ct: (grp.key, ct)))

article_file = "bbc_news_article.txt"
word_counter(article_file).subscribe(lambda w: print(w))
