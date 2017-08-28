from rx import Observable

letters = Observable.from_(["A","B","C","D","E","F"])
numbers = Observable.range(1,5)

Observable.zip(letters,numbers, lambda l,n: "{0}-{1}".format(l,n)) \
    .subscribe(lambda i: print(i))
