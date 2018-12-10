# Important: Run from one level up in order to find the api folder.

import sys
sys.path.append("api")
from server_Objects import text_Transformation, link_Analysis, crawling
from connect import connect
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT_NUMBER = 5350
# PORT_NUMBER = 5432

# This dict translates the path to which the POST request was made
# into its corresponding handler.
sobjs = {
    "/text_Transformation": text_Transformation,
    "/link_Analysis": link_Analysis,
    "/crawling": crawling
}

# Handle requests.

class messageHandler(BaseHTTPRequestHandler):

    # For now, we only care about handling POST requests.
    def do_POST(self):
        contentLength = int(self.headers['Content-Length'])
        postData = self.rfile.read(contentLength)
        
        print("Request to %s" % self.path)
        
        # Get the associated handler for the path
        apiHandler = sobjs.get(self.path)
        
        if apiHandler is None:
            print('Warning: Unrecognized path %s' % self.path)
        else:
            message = json.loads(postData)
            
            print('On %s received %r' % (self.path, message))
            
            # Initialize the handler with the JSON request
            # we received
            apiHandler.__init__(apiHandler, message)
            
            # Pass it off to connect which communicates
            # with the database
            result = connect.insert(apiHandler)
            
            # Determine which error code we'll respond to the client
            # with
            if result is "It Works":
                self.send_response(200)
                print("Handler returned without error. Responding with 200 OK")
            else:
                self.send_response(500)
                print("Handler encountered an error. Responding with 500 Internal Server Error")

            message = {}

            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(json.dumps(message).encode('utf-8'))
        return


try:
    server = HTTPServer(('', PORT_NUMBER), messageHandler)
    print('Serving on port ', PORT_NUMBER)

    server.serve_forever()

except KeyboardInterrupt:
    print('Shutting down')
    server.socket.close()
