import http.server
import socketserver
import json

class SimpleHandler(http.server.BaseHTTPRequestHandler):
    """
    this is a simple handler class
    """
    def do_GET(self):
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'plain/text')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')

PORT = 8000

class MyTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
    print(f"serving at PORT {PORT}")
    httpd.serve_forever()
