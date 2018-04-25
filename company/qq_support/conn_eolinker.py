from urllib import request

def api_interface():
    api = 'http://result.eolinker.com/uuzXvTFb148a117768a7c0cfa61c8b016c26066af3e0a47?uri=/test/v1'
    response = request.urlopen(api)
    html = response.read()
    html = html.decode('utf-8')
    data = eval(html)

    return data

