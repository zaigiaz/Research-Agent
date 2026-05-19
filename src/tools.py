# Regular tools like reading and writing to a file

from ddgs import DDGS
from typing import Any
import pydantic
import json

# TODO :: Follow Tutorial for tool-calling etc. (pydantic)
# TODO :: create basic read and write tools or create basic bash or python interpreter env to work out of
# TODO :: arxiv or wikipedia api for more narrowed search

# NOTE :: I want Claude/Opencodes Read/Write Tool, most efficient.
# NOTE :: I want to not include web fetches into ctx window, just write that to file and let orchestrator handle that.

results = DDGS().text("butterfly wing patterns 2026", max_results=5)

for i,v in enumerate(results):
   print("--------------------")
   print(results[i]['title'])
   print(results[i]['href'])
   print(results[i]['body'])
   print("--------------------")


# result = DDGS().extract("https://en.wikipedia.org/wiki/Modularity_(networks)", fmt="text_rich")
# print(result['content'])
