#!/usr/bin/python3

import requests

cache_page = __import__('web').cache_page
get_page = __import__('web').cache_page

# # Example usage of get_page function
# url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"
# html = get_page(url)
# print(f"HTML content from {url}:")
# print(html)


url2 = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.org"
html2 =get_page(url2)
print(f"HTML content from {url2} (cached):")
print(html2)
