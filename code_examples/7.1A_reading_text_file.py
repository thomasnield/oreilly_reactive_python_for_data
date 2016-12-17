from rx import Observable


def read_lines(file_name):
    file = open(file_name)

    return Observable.from_(file) \
        .map(lambda l: l.strip()) \
        .filter(lambda l: l != "")


read_lines("bbc_news_article.txt").subscribe(lambda s: print(s))
