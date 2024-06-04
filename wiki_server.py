from bs4 import BeautifulSoup
import requests
import http.server
import socketserver
from urllib.parse import urlparse, parse_qs 

PORT = 30080

def get_wiki(input):
  # Set wikipedia base url
  base_url = 'https://en.wikipedia.org/wiki/'

  # Append the title passed in the url to construct the final url 
  full_url = base_url + input

  # Get the wikipedia page and parse with BeautifulSoup
  response = requests.get(full_url)
  html = response.content
  html_formatted = BeautifulSoup(html, "html.parser")

  # Write the wikipedia html page to index.html
  with open('index.html', 'w') as file:
    file.write(str(html_formatted))

# Custom handler class to process GET requests to the http server
class CustomHandler(http.server.SimpleHTTPRequestHandler):
   def do_GET(self):
      # Parse the url passed to the http server
      parsed_path_from_url = urlparse(self.path)

      # Extract the query from the parsed path
      # Query will be stored in a dictionary. Ex: {'title': ['United_States']}
      parsed_query_from_url = parse_qs(parsed_path_from_url.query)

      # Check if the title parameter is present in the query
      if 'title' in parsed_query_from_url:
         # Get the value for the title parameter
         title = parsed_query_from_url['title'][0]

         # Call the get_wiki function to download and save the wikipedia page
         get_wiki(title)
      return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Start a TCP server to handle http requests on port 30080
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()
