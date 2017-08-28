from rx import Observable

Observable.empty() \
    .subscribe(on_next= lambda s: print(s),
               on_completed= lambda: print("Done!")
               )
