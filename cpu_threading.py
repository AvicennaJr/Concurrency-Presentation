import threading
import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    results = []
    threads = []

    def worker(number):
        result = cpu_bound(number)
        results.append(result)

    for number in numbers:
        thread = threading.Thread(target=worker, args=(number,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")

