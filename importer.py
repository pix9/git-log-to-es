import ConfigParser
import httplib
import urllib
import gvar
from json import dumps

class Importer:

    def __init__(self):
        self.conn = httplib.HTTPConnection(gvar.server, gvar.port)
        self.conn.connect()

    def commit(self, commit):
        json = dumps(commit, indent=2)
        headers = {
            "Content-type": "application/json"
        }
        path = gvar.index + '/commits/' + commit['hash']
        self.conn.request("PUT", path, json, headers)
        resp = self.conn.getresponse()
        resp.read()
