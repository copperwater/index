from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT_NUMBER = 5350

# Handle requests.
class messageHandler(BaseHTTPRequestHandler):
    
    # For now, we only care about handling POST requests.
    def do_POST(self):
        contentLength = int(self.headers['Content-Length'])
        postData = self.rfile.read(contentLength)
        
        message = json.loads(postData)
        
        print('Received %r' % message)
        
        self.send_response(200)
        
        message = {'testkey' : 'testresponse'}
        
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(json.dumps(message).encode('utf-8'))
        return

try:
    server = HTTPServer(('', PORT_NUMBER), messageHandler)
    print('Serving on port ' , PORT_NUMBER)

    server.serve_forever()

except KeyboardInterrupt:
    print('Shutting down')
    server.socket.close()
