#!/usr/bin/env python3
"""implementing  an expiring web cache"""

import requests
from functools import wraps
import redis

redis_client = redis.Redis()

def cache_page(func):
    """this is a decorator function """
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


@cache_page
def get_page_cached(url):
    """This funtion """
    response = requests.get(url, timeout=3)
    return response.text

