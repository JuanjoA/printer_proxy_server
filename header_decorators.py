from flask_jsonrpc import JSONRPC, make_response

def json_headers_old(f):
    def wrapped(*args, **kwargs):
        resp = f(*args, **kwargs)
        resp.headers['Content-Type'] = 'application/json'
        return resp
    return wrapped

def json_headers(fn):
    def wrapped(*args, **kwargs):
        response = make_response(fn(*args, **kwargs))
        response.headers['X-JSONRPC-Tag'] = 'JSONRPC 2.0'
        response.headers['Content-Type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        print('--> headers: %s' % response.headers)
        return response
    return wrapped
