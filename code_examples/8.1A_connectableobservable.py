from rx import Observable

source = Observable.from_(["Alpha","Beta","Gamma","Delta","Epsilon"]).publish()

source.subscribe(lambda s: print("Subscriber 1: {0}".format(s)))
source.subscribe(lambda s: print("Subscriber 2: {0}".format(s)))

source.connect()
