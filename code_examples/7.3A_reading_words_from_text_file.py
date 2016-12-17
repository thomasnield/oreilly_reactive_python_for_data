from rx import Observable
import re


def words_from_file(file_name):
    file = open(file_name)

    # parse, clean, and push words in text file
    return Observable.from_(file) \
        .flat_map(lambda s: Observable.from_(s.split())) \
        .map(lambda w: re.sub(r'[^\w]', '', w)) \
        .filter(lambda w: w != "") \
        .map(lambda w: w.lower())

article_file = "bbc_news_article.txt"
words_from_file(article_file).subscribe(lambda w: print(w))
