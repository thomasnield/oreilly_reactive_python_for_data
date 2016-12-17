# Schedules a reactive process that counts the words in a text file every three seconds,
# but only prints it as a dict if it has changed

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


# composes the above word_counter() into a dict
def word_counter_as_dict(file_name):
    return word_counter(file_name).to_dict(lambda t: t[0], lambda t: t[1])


# Schedule to create a word count dict every three seconds an article
# But only re-print if text is edited and word counts change

article_file = "bbc_news_article.txt"

# create a dict every three seconds, but only push if it changed
Observable.interval(3000) \
    .flat_map(lambda i: word_counter_as_dict(article_file))
    .distinct_until_changed() \
    .subscribe(lambda word_ct_dict: print(word_ct_dict))

# Keep alive until user presses any key
input("Starting, press any key to quit\n")
