from rx import Observable
from urllib.request import urlopen


def read_request(link):
    f = urlopen(link)

    return Observable.from_(f) \
        .map(lambda s: s.decode("utf-8").strip()) \

read_request("https://goo.gl/rIaDyM") \
    .subscribe(lambda s: print(s))
