import os
import boto3
import json
import rsrctag
from timestamp import starttime
from s3 import s3_func
from lambdamd import lambda_func
from eb import ebean
from stepfunc import step_func
from s3tagging import s3tag
from ebtagging import ebtag
from lambdatagging import lambdatag
from stepfunctagging import steptag

bucketname = os.environ['ApplConfigBucketName']
config_json = os.environ['ApplConfigkeyName']
output_key = os.environ['ApplOutputKeyName']
kms_alias = os.environ['KMSAlias']

if not kms_alias.strip():
    extra_args = {'ServerSideEncryption': 'AES256'}
else:
    extra_args = {'ServerSideEncryption': 'aws:kms',
                  'SSEKMSkeyID': kms_alias}

s3_resource = boto3.resource('s3')
bucket = s3_resource.Bucket(bucketname)

with open(config_json) as config_content:
    json_content = json.load(config_content)

s3buckets = json_content['s3buckets']
lambdas = json_content['lambdaext']
stepfunc = json_content['stepfunc']
ebappnames = json_content['ebapp']
appkey = json_content['key']
value = json_content['value']

s3check = json_content['s3check']
lambdacheck  = json_content['lambdacheck']
stepfuncheck = json_content['stepfuncheck']
ebcheck = json_content['ebcheck']
tagvalidation = json_content['tagvalidation']


def lambda_handler(event, context):
    output_content = []

    output_content.append("Tech shakeout started at ----> " + starttime() + "\n")

    if tagvalidation.lower() == 'true':
        output_content.append("############################## Validation for Tag ----> " + value + " <---- ########################################" + "\n")
        s3list = s3tag(appkey, value)
        output_content.append("############################## S3 Bucket Validation for Tag ----> " + value + " <---- ########################################" + "\n")
        output_content.append("\n".join(s3list))
        rsrctag.arn.clear()
        eblist = ebtag(appkey, value)
        output_content.append("############################## Beanstalk Validation for Tag ----> " + value + " <---- ########################################" + "\n")
        output_content.append("\n".join(eblist))
        rsrctag.arn.clear()
        lmdlist = lambdatag(appkey, value)
        output_content.append("############################## Lambda Validation for Tag ----> " + value + " <---- ########################################" + "\n")
        output_content.append("\n".join(lmdlist))
        rsrctag.arn.clear()
        stplist = steptag(appkey, value)
        output_content.append("############################## Step Function Validation for Tag ----> " + value + " <---- ########################################" + "\n")
        output_content.append("\n".join(stplist))
        rsrctag.arn.clear()
    if s3check.lower()=='true':
        output_content.append("############################## S3 Bucket Validation ##################################" + "\n")
        for buck in s3buckets:
            pref = s3buckets[buck]
            for i in pref:
                s3_contents = s3_func(buck, i)
                output_content.append("\n".join(s3_contents))
    if lambdacheck.lower()=='true':
        output_content.append("############################## Lambda Validation ##################################" + "\n")
        for lambda_name in lambdas:
            output_content.append("\n".join(lambda_func(lambda_name)))
    if ebcheck.lower()=='true':
        output_content.append("############################## Beanstalk Validation ##################################" + "\n")
        for ebappname in ebappnames:
            output_content.append("\n".join(ebean(ebappname)))
    if stepfuncheck.lower()=='true':
        output_content.append("############################## Step Function Validation ##################################" + "\n")
        for step_function_arn in stepfunc:
            output_content.append("\n".join(step_func(step_function_arn)))

    output_file = open('/tmp/test.txt', 'a+')
    output_file.write("\n".join(output_content))
    output_file.close()
    bucket.upload_file('/tmp/text.txt',output_key, extra_args)
    os.remove('/tmp/test.txt')
