import sys
import boto3
from urlcheck import respcheck
import datetime

def ebean(appname):
    elastic_beanstalk_details = [""]
    try:
        client = boto3.client('elasticbeanstalk')
        response = client.describe_environments(ApplicationName=appname)
        response1 = response['Environments']
        elastic_beanstalk_details.append("Details of beanstalk application ---> " + appname + "\n")
        for resp in response1:
            envname = resp["EnvironmentName"]
            health = resp["Health"]
            lstupdt = datetime.datetime.strftime(resp['DateUpdated'], "%m/%d/%Y %H:%M:%S")
            elastic_beanstalk_details.append("\t" + "Environment ----> " + envname)
            elastic_beanstalk_details.append("\t" + "Health ---> " + health)
            elastic_beanstalk_details.append("\t" + "Last Updated -----> " + lstupdt)

            if cname in resp:
                cname = resp["CNAME"]
                respcd = respcheck(cname)
                elastic_beanstalk_details.append("\t" + "CNAME ----> " + cname )
                elastic_beanstalk_details.append("\t" + "CNAME Response code ----> " + str(respcd))
            elastic_beanstalk_details.append("\n")
    except:
        elastic_beanstalk_details.append(f"Error [Elastic Beanstalk - {envname}]: {sys.exc_info()[0]} | {sys.exc_info()[1]}")
