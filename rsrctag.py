import boto3
from os import environ

accesskey = environ.get('AWS_ACCESS_KEY_ID')
secretkey = environ.get('AWS_SECRET_ACCESS_KEY_ID')
sessiontoken = environ.get('AWS_SESSION_TOKEN')
region = environ.get('aws_region')

client = boto3.client('resourcegroupstaggingapi',
                      aws_access_key_id = accesskey,
                      aws_secret_access_key_id = secretkey,
                      aws_session_token = sessiontoken,
                      region_name = region)
arn=[]
def filterfunc(pgtoken,key,value,rsrc):
    rsrclst = client.get_resource(PaginationToken=pgtoken, TagFilters=[{'key':key,'Values':[value]}], ResourceTypeFilters=[rsrc])
    rsrclst1 = rsrclst['ResourceTagMappingList']
    for resp in rsrclst1:
        arnname = resp['ResourceARN']
        arn.append(arnname)
    pgtoken = rsrclst['PaginationToken']

    if pgtoken:
        filterfunc(pgtoken,key,value,rsrc)
    return arn
