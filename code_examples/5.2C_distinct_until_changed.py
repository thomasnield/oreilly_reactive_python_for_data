from rx import Observable

Observable.from_(["Alpha", "Theta", "Kappa", "Beta", "Gamma", "Delta", "Epsilon"]) \
    .map(lambda s: len(s)) \
    .distinct_until_changed() \
    .subscribe(lambda i: print(i))


Observable.from_(["Alpha", "Theta", "Kappa", "Beta", "Gamma", "Delta", "Epsilon"]) \
    .distinct_until_changed(lambda s: len(s)) \
    .subscribe(lambda i: print(i))
