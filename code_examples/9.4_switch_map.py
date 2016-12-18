from rx import Observable
from rx.concurrency import ThreadPoolScheduler
from threading import current_thread
import multiprocessing, time, random


def intense_calculation(value):
    # sleep for a random short duration between 0.5 to 2.0 seconds to simulate a long-running calculation
    time.sleep(random.randint(5, 20) * .1)
    return value


# calculate number of CPU's and add 1, then create a ThreadPoolScheduler with that number of threads
optimal_thread_count = multiprocessing.cpu_count() + 1
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)

strings = Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa"])

Observable.interval(6000) \
    .switch_map(lambda i: strings.map(lambda s: intense_calculation(s)).subscribe_on(pool_scheduler)) \
    .subscribe(on_next=lambda s: print("Received {0} on {1}".format(s, current_thread().name)),
               on_error=lambda e: print(e))

input("Press any key to exit\n")
