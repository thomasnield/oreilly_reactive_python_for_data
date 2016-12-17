from rx import Observable

Observable.from_([4,76,22,66,881,13,35]) \
    .filter(lambda i: i < 100) \
    .reduce(lambda total, value: total + value) \
    .subscribe(lambda s: print(s))
