from rx import Observable

items = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]

Observable.from_(items) \
    .group_by(lambda s: len(s)) \
    .flat_map(lambda grp: grp.to_list()) \
    .subscribe(lambda i: print(i))
