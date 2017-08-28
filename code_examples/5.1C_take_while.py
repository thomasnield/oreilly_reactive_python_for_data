from rx import Observable

Observable.from_([2,5,21,5,2,1,5,63,127,12]) \
    .take_while(lambda i: i < 100) \
    .subscribe(on_next = lambda i: print(i), on_completed = lambda: print("Done!"))
