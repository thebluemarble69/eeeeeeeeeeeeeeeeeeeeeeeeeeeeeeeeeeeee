from http.server import BaseHTTPRequestHandler, HTTPServer
from html import escape
from strawberry import *
import urllib.parse
import datetime
import sys


eeeee2 = """
    <form style="position:absolute;bottom:0;" action="/e" method="post">
        <input id="c" type="text" placeholder="xyz" name="msg" required>
        <input id="ce" type="submit" value="submit">
    </form>
    </div>


    <script src="./s.js"></script>
</body>
</html>
"""

chat=[]

class XYZ(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Server", "Guu/13")
            self.end_headers()
            with open("index.html", 'rb') as dg:
                self.wfile.write(dg.read())
            print(type(self.headers))
            print(self.client_address)
        elif self.path == "/after.css":
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.send_header("Server", "Guu/13")
            self.end_headers()
            with open('after.css', 'rb') as ff:
                self.wfile.write(ff.read())
        elif self.path == "/s.js":
            self.send_response(200)
            self.send_header("Content-type", "text/javascript")
            self.send_header("Server", "Guu/13") 
            self.end_headers()
            with open("s.js", 'rb') as je:
                self.wfile.write(je.read())
        elif self.path == "/styIle.css":
            self.send_response(200)
            self.send_header("Content-type", 'text/css')
            self.end_headers()
            with open('styIle.css', 'rb') as x:
                self.wfile.write(x.read())
        elif self.path == "/favicon.ico":
            self.send_response(200)
            self.send_header('Content-type', "image/x-icon")
            self.end_headers()
            with open("favicon.ico", 'rb') as d:
                self.wfile.write(d.read())
        elif self.path == "/ee.png":
            server_version = "Linus/16.2"
            sys_version = "Linus/13"
            print(self.version_string())
            self.send_response(200)
            self.send_header("Content-type","image/png")
            self.send_header("Server", "Guu/13")
            self.end_headers()
            with open("ee.png", 'rb') as op:
                self.wfile.write(op.read())
        elif self.path == "/oo":
            self.send_response(301)
            self.send_header("Location", "https://instagram.com")
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header("Server", "Guu/13")
            self.end_headers()
            self.wfile.write(b"<h1>Fuck off Daddy!</h1>")
    def do_POST(self):
        if self.path == "/e":
            eeeee = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="shortcut icon" href="./favicon.ico" type="image/x-icon">
                <link rel="stylesheet" href="./styIle.css">
                <title>Chattttts</title>
                <noscript><b>FUck u btch use <span style="color:aqua">javascript</span></b></noscript>
            </head>
            <body>
                <div class="stars" id="stars"></div>
                <div class="vg"></div>
                <div class="vg2"></div>
                <div class="x">
                    <h1>Chat through the connected server.</h1>

                    """
            leng=int(self.headers.get("Content-Length", 0))
            f = self.rfile.read(leng)
            #print(f)
            xe = self.client_address[0]
            try:
                global data
                data = urllib.parse.parse_qs(f.decode("utf-8")).get("msg")[0]                           #f.decode("utf-8").split("=")[1]                    #urllib.parse.unquote(f.decode("utf-8").split("=")[1]
            except Exception:
                self.send_response(301)
                self.send_header("Location", "/")
                self.end_headers()
                print("ERROR", Exception)
            datta = str(datetime.datetime.now())[:19]
            print(data)
            bb("data:     " + f.decode("utf-8"))
            rite(datta,str(urllib.parse.quote(data)), str(xe))        # data = str(f.decode("utf-8").split("=")[1]))
            # print(f"data: {data}");print(f"datta: {datta}"); print(f"xe: {xe}")
            print(urllib.parse.parse_qs(f.decode('utf-8')))
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # with open('after.html', 'r') as fd:
            #     self.wfile.write(bytes(fd.read().format(escape(data)), 'utf-8'))
            # u = eeeee + get_temp(escape(data)) + eeeee2
            # self.wfile.write(bytes(u, 'utf-8'))
            uv = do()
            for i in uv:
                eeeee += get_temp(escape(urllib.parse.unquote(i)))
            self.wfile.write(bytes(eeeee + eeeee2, 'utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"FUCK YOU BITCH")
try:
    x = HTTPServer(("0.0.0.0",25565), XYZ)
    x.serve_forever()
except KeyboardInterrupt:
    print("Exitting now.")

    sys.exit()
