from rx import Observable

x = 1
y = 5

integers = Observable.defer(lambda: Observable.range(x, y))
integers.subscribe(lambda i: print(i))

print("\nSetting y = 10\n")
y = 10

integers.subscribe(lambda i: print(i))