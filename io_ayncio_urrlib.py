import asyncio
import time
import urllib.request

async def download_site(url):
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Read {0} from {1}".format(len(content), url))

async def download_all_sites(sites):
    tasks = [download_site(url) for url in sites]
    await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 20
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")

