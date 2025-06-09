import http.server
import socketserver

class SimpleHandler(http.server.BaseHTTPRequestHandler):
    """
    this is a simple handler class
    """
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, this is a simple API!')

PORT = 8000

class MyTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
    print(f"serving at PORT {PORT}")
    httpd.serve_forever()
