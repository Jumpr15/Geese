import httpx

import inspect
import os
from dotenv import load_dotenv

load_dotenv()

def web_search_tool(query):
     client = httpx.Client()

     url = "https://api.search.brave.com/res/v1/web/search"
     headers = {
          "Accept": "application/json",
          "Accept-Encoding": "gzip",
          "X-Subscription-Token": os.getenv("BRAVE_SEARCH_API_KEY")
     }

     params = {
          "q": query
     }

     response = client.get(
          url, 
          headers=headers,
          params=params
     )

     results = response.json()

     results_list = []
     if results.get("web", {}).get("results"):
          results = results["web"]["results"]
          for result in results:
               results_list.append(
                    {
                         "title": result['title'],
                         "content": result['description']
                    }
               )
               
     query_res = {
          "query": query,
          "headers": headers, ### hash/fuzz api key later
          "params": params,
          "search_results": results_list
     }
     
     tool_name = inspect.currentframe().f_code.co_name
     
     arg_list = []
     sig = inspect.signature(web_search_tool) ### Manually set
     args = sig.parameters.values()
     for arg in args:
          arg_list.append(
               arg.name
          )

     res = {
          "tool_name": tool_name,
          "parameters": arg_list,
          "web_search_content": query_res
     }
     return res
