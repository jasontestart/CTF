#!/usr/bin/python2
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import SocketServer
import sys

class S(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')                
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "Accept, Content-Type, Content-Length")
        self.end_headers()

    def do_GET(self):
        self.send_response(404)
        seld.end_headers()

    def do_POST(self):
        self.send_response(200)
        self.end_headers()

        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        print self.data_string
        return

def run(server_class=HTTPServer, handler_class=S, port=8444):
    server_address = ('',port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
