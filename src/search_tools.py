import pydantic
from ddgs import DDGS
from typing import Any

# TODO :: arxiv or wikipedia api for more narrowed search

results = DDGS().text("butterfly wing patterns 2026", max_results=5)

for i,v in enumerate(results):
   print("--------------------")
   print(results[i]['title'])
   print(results[i]['href'])
   print(results[i]['body'])
   print("--------------------")


# result = DDGS().extract("https://en.wikipedia.org/wiki/Modularity_(networks)", fmt="text_rich")
# print(result['content'])
