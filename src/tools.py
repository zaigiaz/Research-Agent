# Regular tools like reading and writing to a file

from pydantic import BaseModel, ValidationError, field_validator
from typing import Any, List
from ddgs import DDGS
import json
import re

class Tool(BaseModel):
   tool_name: str
   tool_type: str

def extract_json_from_response(msg: str) -> dict:
   json_match = re.findall(r'\{(?:[^{}]|\\.|"(?:\\.|[^"\\])*")*\}', msg, flags=re.DOTALL)
   if json_match:
      return [json.loads(data) for data in json_match]
   raise ValueError("no JSON found in LLM response")

def parse_review(llm_output: str) -> Tool:
   try:
      data = extract_json_from_response(llm_output)
      review = [Tool(**d) for d in data]
      return review
   except json.JSONDecodeError as e:
      print(f"JSON parsing error: {e}")
      raise
   except ValidationError as e:
      print(f"Validation error: {e}")
      raise
   except Exception as e:
      print(f"Unexpected error: {e}")
      raise

def web_search(query: str) -> str:
   results = DDGS().text(query, max_results=5)
   for i,v in enumerate(results):
      print("--------------------")
      print(results[i]['title'])
      print(results[i]['href'])
      print(results[i]['body'])
      print("--------------------")
