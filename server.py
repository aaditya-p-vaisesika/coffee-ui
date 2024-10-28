from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Content-Security-Policy', 'frame-ancestors \'self\' https://app.powerbi.com/')
        BaseHTTPRequestHandler.end_headers(self)

def run_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running on port 8000...')
    httpd.serve_forever()

run_server()