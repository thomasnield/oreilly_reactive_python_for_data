from rx import Observable, Observer

# Using Observable.range()
letters = Observable.range(1,10)
letters.subscribe(lambda value: print(value))

# Using Observable.just()
greeting = Observable.just("Hello World!")
greeting.subscribe(lambda value: print(value))
