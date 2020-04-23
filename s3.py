import sys
import boto3
import datetime
from os import environ

accesskey = environ.get('AWS_ACCESS_KEY_ID')
secretkey = environ.get('AWS_SECRET_ACCESS_KEY_ID')
sessiontoken = environ.get('AWS_SESSION_TOKEN')
region = environ.get('aws_region')

def s3_func(confbuck, confpref):
    s3_contents = [""]
    try:
        client = boto3.client('s3')
        response = client.list_objects_v2(Bucket=confbuck,Prefix=confpref)
        response1 = response['Contents']
        if not confpref:
            s3_contents.append("Contents of bucket -------> " + confbuck + "\n")
        else:
            s3_contents.append("Contents of prefix -------> " + confpref + " in bucket " + confbuck + "\n")

        for i in response1:
            if "//" not in i['Key'] or not i['Key']:
                s3_contents.append("\t"+i['Key'] + "\t" + datetime.datetime.strftime(i['LastModified'], "%m/%d/%Y %H:%M:%S"))
        s3_contents.append("\n")
    except:
        s3_contents.append(f"Error: [S3 - {confpref}]: {sys.exc_info()[0]} | {sys.exc_info()[1]}")
    return s3_contents