from rsrctag import filterfunc
from s3 import s3_func

def s3tag(appkey, value):
    s3contents = []
    s3list = []
    s3arn = filterfunc("",appkey,value,"s3")
    for i in s3arn:
        s3list.append(i.split(":::")[1])
    for i in s3list:
        s3contents.extend(s3_func(i,""))
    return s3contents