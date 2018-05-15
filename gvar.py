import ConfigParser

conf=ConfigParser.ConfigParser()
conf.read('git_es.ini')
server=conf.get("git_es","es_server_ip")
port=conf.get("git_es","es_server_port")
index=conf.get("git_es","index")
