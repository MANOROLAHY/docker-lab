import os, socket
from http.server import BaseHTTPRequestHandler, HTTPServer

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = b"ok\n"
        else:
            msg = os.environ.get("MESSAGE", "Bonjour depuis Docker")
            body = f"{msg}\nconteneur: {socket.gethostname()}\n".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)

HTTPServer(("0.0.0.0", 8080), H).serve_forever()
