from rx import Observable, Observer

def push_numbers(observer):
    observer.on_next(100)
    observer.on_next(300)
    observer.on_next(500)
    observer.on_completed()

Observable.create(push_numbers).subscribe(on_next = lambda i: print(i))
