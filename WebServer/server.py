from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the HTTP request handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Handler for GET requests
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
        
        # Send message back to client
        message = "Hello, world!"
        
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

# Define the server address
host = 'localhost'
port = 8000

# Create an instance of the HTTP server
server = HTTPServer((host, port), SimpleHTTPRequestHandler)

# Print server information
print(f"Server started on http://{host}:{port}")

# Run the server
server.serve_forever()
