import time
import requests
from concurrent.futures import ThreadPoolExecutor


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


start = time.time()

with ThreadPoolExecutor() as pool:
    urls = ['https://www.baidu.com' for _ in range(1000)]
    results = pool.map(get_status_code, urls)
    for result in results:
        pass

end = time.time()

print(f'finished requests in {end - start:.4f} second(s)')
