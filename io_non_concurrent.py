import urllib.request
import time


def download_site(url):
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print(f"Read {len(content)} from {url}")


def download_all_sites(sites):
    for url in sites:
        download_site(url)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 20
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")

