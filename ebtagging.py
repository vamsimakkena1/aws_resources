from rsrctag import filterfunc
from eb import ebean

def ebtag(appkey, value):
    ebenvlst = []
    envdet = []
    ebarn = filterfunc("",appkey,value,"elasticbeanstalk")
    for i in ebarn:
        ebenvlst.append(i.split("/")[1])
    ebenv = list(dict.fromkeys(ebenvlst))
    for i in ebenv:
        envdet.extend(ebean(i))
    return envdet