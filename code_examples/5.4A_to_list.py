from rx import Observable

Observable.from_(["Alpha","Beta","Gamma","Delta","Epsilon"]) \
    .to_list() \
    .subscribe(lambda s: print(s))
