#!/usr/bin/env python3
# Simple cloud web server for Google Cloud VM
# Displays "Hello Cloud" with hostname and IP

import http.server
import socket
import sys

class HelloHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        message = f"""
        <html>
        <head><title>Hello Cloud</title></head>
        <body>
            <h1>Hello Cloud</h1>
            <p><b>Hostname:</b> {hostname}</p>
            <p><b>IP Address:</b> {ip}</p>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    # Default port is 8000, can be overridden by argument
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    server_address = ("0.0.0.0", port)
    httpd = http.server.HTTPServer(server_address, HelloHandler)
    print(f"Listening for connections on port {port}")
    httpd.serve_forever()
