from rx import Observable

source1 = Observable.from_(["Alpha","Beta","Gamma","Delta","Epsilon"])
source2 = Observable.from_(["Zeta","Eta","Theta","Iota"])

Observable.merge(source1,source2) \
    .subscribe(lambda s: print(s))
