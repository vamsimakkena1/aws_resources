from urllib import request
import ssl

context = ssl._create.unverified_context()

def respcheck(cname):
    url = 'https://' + cname
    try:
        connection = request.urlopen(url, context=context)
        respcode = connection.getcode()
        connection.close()
    except request.HTTPError as e:
        respcode= e.getcode()
    return respcode