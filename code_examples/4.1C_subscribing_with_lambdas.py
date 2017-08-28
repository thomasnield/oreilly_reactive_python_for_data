from rx import Observable

letters = Observable.from_(["Alpha","Beta","Gamma","Delta","Epsilon"])

letters.subscribe(on_next = lambda value: print(value),
                  on_completed = lambda: print("Completed!"),
                  on_error = lambda error: print("Error occurred: {0}".format(error)))

# to use just on_next:
# letters.subscribe(on_next = lambda value: print(value))
# letters.subscribe(lambda value: print("Received: {0}".format(value)))
