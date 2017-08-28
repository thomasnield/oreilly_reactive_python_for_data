from rx import Observable

Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]) \
    .distinct(lambda s: len(s)) \
    .subscribe(lambda i: print(i))
