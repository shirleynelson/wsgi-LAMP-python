def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!<br><a href="https://github.com/shirleynelson/wsgi-LAMP-python">GitHub LAMP Source</a>'

    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
