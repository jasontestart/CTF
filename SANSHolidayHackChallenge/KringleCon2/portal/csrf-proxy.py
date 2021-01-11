#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
    def do_GET(self):
        proxies = { 'http':'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
        headers = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
        r = requests.get('https://studentportal.elfu.org/validator.php', proxies = proxies, headers = headers, verify=False)
        token = r.text

       # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = f'token={token}'
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
 
def run():
  print('starting server...')
 
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()
