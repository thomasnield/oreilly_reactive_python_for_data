from rx import Observable

letters = Observable.from_(["Alpha","Beta","Gamma","Delta","Epsilon"])
intervals = Observable.interval(1000)

Observable.zip(letters,intervals, lambda s,i: s) \
    .subscribe(lambda s: print(s))

input("Press any key to quit\n")
