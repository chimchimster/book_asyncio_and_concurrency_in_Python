import time
import requests
from concurrent.futures import ThreadPoolExecutor


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


start = time.time()

with ThreadPoolExecutor(max_workers=100) as pool:
    urls = ['https://example.com' for _ in range(1000)]
    results = pool.map(get_status_code, urls)

    for result in results:
        print(result)

    end = time.time()

    print(f'Выполнение запросов завершено за {end - start:.4f} с')