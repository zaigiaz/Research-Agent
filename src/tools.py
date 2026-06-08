# Regular tools like reading and writing to a file

from pydantic import BaseModel, ValidationError, field_validator
from typing import Any, List
from ddgs import DDGS
import json
import re

# TODO :: arxiv or wikipedia api for more narrowed search
# NOTE :: I want Claude/Opencodes Read/Write Tool, most efficient.
# NOTE :: I want to not include web fetches into ctx window, just write that to file and let orchestrator handle that.

# result = DDGS().extract("https://en.wikipedia.org/wiki/Modularity_(networks)", fmt="text_rich")
# print(result['content'])

parsed_items: List[dict] = []

class Tool(BaseModel):
   tool_name: str
   tool_type: str

def extract_json_from_response(msg: str) -> dict:
   json_match = re.search(r'\{.*\}', msg)
   if json_match:
      return json.loads(json_match.group())
   raise ValueError("no JSON found in LLM response")
   
def parse_review(llm_output: str) -> Tool:
   try:
      data = extract_json_from_response(llm_output)
      review = Tool(**data)
   except json.JSONDecodeError as e:
      print(f"JSON parsing error: {e}")
      raise
   except ValidationError as e:
      print(f"Validation error: {e}")
      raise
   except Exception as e:
      print(f"Unexpected error: {e}")
      raise

def add_to_list(item: dict):
   parsed_items.append(item)

def web_search(query: str) -> str:
   results = DDGS().text(query, max_results=5)
   for i,v in enumerate(results):
      print("--------------------")
      print(results[i]['title'])
      print(results[i]['href'])
      print(results[i]['body'])
      print("--------------------")
