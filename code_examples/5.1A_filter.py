from rx import Observable

Observable.from_(["Alpha","Beta","Gamma","Delta","Epsilon"]) \
    .filter(lambda s: len(s) >= 5) \
    .subscribe(lambda s: print(s))
