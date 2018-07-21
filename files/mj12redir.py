#!/usr/local/bin/python3
import http.server
import socketserver
class handler(http.server.BaseHTTPRequestHandler):
 def do_GET(self):
  self.send_response(302)
  self.send_header('Location', 'https://mj12bot.com/')
  self.end_headers()
 do_HEAD = do_GET
 do_POST = do_GET
with socketserver.TCPServer(("", 80), handler) as httpd:
 httpd.serve_forever()
