from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import json

LOG_FILE = "honeypot_log.json"

class HoneyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        entry = {
            "time": str(datetime.datetime.now()),
            "ip": self.client_address[0],
            "path": self.path,
            "agent":self.headers.get("User-Agent","?" )
        }


        print(json.dumps(entry, indent=2))

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "/n")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Thanks for visiting!")

    def log_message(self, *args):
        pass

print("Honeypot running on http://localhost:8080")

HTTPServer(("127.0.0.1", 8080), HoneyHandler).serve_forever()