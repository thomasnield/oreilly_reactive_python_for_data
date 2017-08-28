from rx import Observable

Observable.from_([4,76,22,66,881,13,35]) \
    .scan(lambda total, value: total + value) \
    .subscribe(lambda s: print(s))
