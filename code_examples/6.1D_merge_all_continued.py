from rx import Observable

items = ["134/34/235/132/77", "64/22/98/112/86/11", "66/08/34/778/22/12"]

Observable.from_(items) \
    .map(lambda s: Observable.from_(s.split("/"))) \
    .merge_all() \
    .map(lambda s: int(s)) \
    .subscribe(lambda i: print(i))
