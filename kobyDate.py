#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn

import datetime
import sys

if len(sys.argv) > 1:
    try:
        port = int(sys.argv[1])
    except:
        port = 80
else:
    port = 80

class Handler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        if self.path.startswith('/tikal'):
            self.send_response(200)
            self.send_header('Content-type',    'text/plain')
            self.end_headers()
            self.wfile.write( "KOBY TEST TO TIKAL: %s"%(datetime.datetime.now()) )
            self.wfile.write("\n\n\n")
            with open("/opt/git_commit", 'r') as fin:
                commit = fin.read()
            self.wfile.write( "Commit:\n\n%s "%(commit) )

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

server = ThreadedHTTPServer(('0.0.0.0', port), Handler)
print 'Starting server, use <Ctrl-C> to stop'
print "Started on port: %s"%port
server.serve_forever()

