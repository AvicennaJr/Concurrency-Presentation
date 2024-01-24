import urllib.request
import multiprocessing
import time

session = None


def set_global_session():
    global session
    if not session:
        session = urllib.request.build_opener()


def download_site(url):
    with session.open(url) as response:
        content = response.read()
        name = multiprocessing.current_process().name
        print(f"{name}: Read {len(content)} from {url}")


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 20
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")

