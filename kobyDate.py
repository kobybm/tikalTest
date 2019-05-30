#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn

import datetime


class Handler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        if self.path.startswith('/tikal'):
            self.send_response(200)
            self.send_header('Content-type',    'text/html')
            self.end_headers()
            self.wfile.write( "<h1>KOBY TEST TO TIKAL: %s</h1>"%(datetime.datetime.now()) )
            with open("/opt/git_commit", 'r') as fin:
                commit = fin.read()
            self.wfile.write( "<br>Commit ID = %s "%(commit) )

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

server = ThreadedHTTPServer(('0.0.0.0', 80), Handler)
print 'Starting server, use <Ctrl-C> to stop'
print "Started on port: 80"
server.serve_forever()

