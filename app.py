import http.server
import ssl


class MyHandler(http.server.SimpleHTTPRequestHandler):  # custom way of handlign requests
    def log_message(self, format, *args):  # disable logs on requests
        return

    def do_GET(self):  # handling get requests
        # to act based on url requests use:
        # if self.path == path:
        #     self.wfile.write('response text)
        #     self.send_response(200
        self.send_response(200)  # response code
        f = open('index.html', 'rb')  # open file for response as binary
        self.send_header('Content-type', 'text/html')  # set response headers
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

    def do_POST(self):  # handling post requests
        length = int(self.headers.get('Content-Length'))  # read data length
        data = self.rfile.read(length).decode('utf8')  # read whole request data as utf8
        print(data)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.send_response(200, 'OK')


server_address = ('localhost', 8000)  # port
httpd = http.server.HTTPServer(server_address, MyHandler)  # start server with settings

# ssl settings, making server https, remove it to have simple http version
httpd.socket = ssl.wrap_socket(httpd.socket,
                               certfile='cert.pem',
                               server_side=True,
                               keyfile='key.pem')

print('starting server at: https://localhost:8000')
httpd.serve_forever()  # start server
