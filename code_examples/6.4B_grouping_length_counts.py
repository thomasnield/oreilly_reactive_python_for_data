from rx import Observable

items = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]

Observable.from_(items) \
    .group_by(lambda s: len(s)) \
    .flat_map(lambda grp:
         grp.count().map(lambda ct: (grp.key, ct))
    ) \
    .to_dict(lambda key_value: key_value[0], lambda key_value: key_value[1]) \
    .subscribe(lambda i: print(i))
