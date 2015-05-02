import http.server
import ssl


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def do_GET(self):
        self.send_response(200)
        f = open('index.html', 'rb')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

    def do_POST(self):
        length = int(self.headers.get('Content-Length'))
        data = self.rfile.read(length).decode('utf8')
        print(data)

        self.send_response(200, 'OK')


server_address = ('localhost', 8000)
httpd = http.server.HTTPServer(server_address, MyHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               certfile='cert.pem',
                               server_side=True,
                               keyfile='key.pem')

print('starting server at: https://localhost:8000')
httpd.serve_forever()
