import urllib.request
import concurrent.futures
import threading
import time

thread_local = threading.local()


def get_opener():
    if not hasattr(thread_local, "opener"):
        thread_local.opener = urllib.request.build_opener()
    return thread_local.opener


def download_site(url):
    opener = get_opener()
    with opener.open(url) as response:
        content = response.read()
        print(f"Read {len(content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 20
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")

