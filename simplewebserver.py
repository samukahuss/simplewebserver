from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
from jinja2 import Template
import socket

class SimpleWebServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        hostname = socket.gethostname()
        title = "SimpleWebServer"
        dt = datetime.now()
        ts = datetime.timestamp(dt)
        fts = datetime.fromtimestamp(ts, tz=None)
        
        data = {
            "title" : title,
            "hostname" :  hostname,
            "time" : fts
        }
        
        saida = ''
        with open('simpletext.j2', 'r') as f:
            saida = f.read()
            
        template = Template(saida)
        msg = template.render(data)
        
        self.send_response(200)

        # Envia os cabeçalhos
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Envia a mensagem como corpo da resposta
        self.wfile.write(bytes(msg, "utf8"))
        


if __name__=='__main__':
    ADDRESS = 'localhost'
    PORT = 8080
    AMOUNT=0
    labserver = HTTPServer((ADDRESS, PORT), SimpleWebServer)
    
    try:
        labserver.serve_forever()
    except KeyboardInterrupt:
        pass
    
    labserver.server_close()