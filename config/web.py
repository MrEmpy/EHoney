import http.server as SimpleHTTPServer
import socketserver as SocketServer
import os
from datetime import date, datetime
import linecache

date_today = date.today()
now = datetime.now()

class Run:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        try:
            os.mkdir(f'/etc/ehoney/logs/web-hp-{date_today}')
        except FileExistsError:
            pass

        class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
            def do_GET(self):
                logging.error(self.headers)
                SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
            log_file = open(f'/etc/ehoney/logs/web-hp-{date_today}/log.txt', 'w', 1)
            def log_message(self, format, *args):
                self.log_file.write('IP: %s\nDate: [%s]\n%s%s\n\n\n\n' % (self.client_address[0], self.log_date_time_string(), self.headers, format%args))

        web_dir = os.path.join(os.path.dirname(__file__), '/etc/ehoney/web')
        os.chdir(web_dir)
        Handler = GetHandler
        httpd = SocketServer.TCPServer((host, port), Handler)
        httpd.serve_forever()

Run(host='127.0.0.1', port=int(linecache.getline('/etc/ehoney/config/ports.conf', 5).split('=')[1]))
