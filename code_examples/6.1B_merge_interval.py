from rx import Observable

source1 = Observable.interval(1000).map(lambda i: "Source 1: {0}".format(i))
source2 = Observable.interval(500).map(lambda i: "Source 2: {0}".format(i))
source3 = Observable.interval(300).map(lambda i: "Source 3: {0}".format(i))

Observable.merge(source1, source2, source3) \
    .subscribe(lambda s: print(s))

# keep application alive until user presses a key
input("Press any key to quit\n")
