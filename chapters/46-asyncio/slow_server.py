import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

RATES = {"EUR": 0.92, "GBP": 0.79, "JPY": 149.5, "CAD": 1.36}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(0.5)  # pretend the service is slow
        code = self.path.rsplit("/", 1)[-1]
        body = json.dumps({"currency": code, "rate": RATES.get(code)}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


ThreadingHTTPServer(("127.0.0.1", 8766), Handler).serve_forever()
