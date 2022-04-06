from pprint import pprint


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    pprint(environ)
    yield b'Hello, World!\n'

