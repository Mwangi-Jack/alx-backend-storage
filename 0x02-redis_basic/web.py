import requests
import redis
import time
from functools import wraps

# Initialize Redis connection
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_page(url: str) -> str:
    # Check if the URL count key exists in Redis
    count_key = f"count:{url}"
    if redis_client.exists(count_key):
        # Increment the count for this URL
        redis_client.incr(count_key)
    else:
        # Initialize the count for this URL
        redis_client.set(count_key, 1)

    # Check if the HTML content is cached in Redis
    cache_key = f"html:{url}"
    cached_html = redis_client.get(cache_key)
    if cached_html:
        return cached_html.decode('utf-8')

    # Retrieve HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    # Cache the HTML content with an expiration time of 10 seconds
    redis_client.setex(cache_key, 10, html_content)

    return html_content

# Bonus: Implement caching decorator
def cache_page(func):
    @wraps(func)
    def wrapper(url):
        cache_key = f"html:{url}"
        cached_html = redis_client.get(cache_key)
        if cached_html:
            return cached_html.decode('utf-8')

        html_content = func(url)
        redis_client.setex(cache_key, 10, html_content)
        return html_content

    return wrapper

# Usage example
if __name__ == "__main__":
    # Example usage of get_page function
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"
    html = get_page(url)
    print(f"HTML content from {url}:")
    print(html)

    # Example usage of cached version using decorator
    @cache_page
    def get_page_cached(url):
        response = requests.get(url)
        return response.text

    url2 = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.org"
    html2 = get_page_cached(url2)
    print(f"HTML content from {url2} (cached):")
    print(html2)
