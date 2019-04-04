import http.server
import socketserver

PORT = 8888
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as http:
    print("serving at port: ",PORT)
    httpd.serve_forever()
