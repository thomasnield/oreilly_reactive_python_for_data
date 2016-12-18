from rx import Observable
import time

source = Observable.interval(1000).publish()

source.subscribe(lambda s: print("Subscriber 1: {0}".format(s)))
source.connect()

# sleep 5 seconds, then add another subscriber
time.sleep(5)
source.subscribe(lambda s: print("Subscriber 2: {0}".format(s)))

input("Press any key to exit\n")