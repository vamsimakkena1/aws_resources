import sys
import boto3

def lambda_func(lambdaname):
    lambda_details = [""]
    environment_variables = [""]
    try:
        client = boto3.client('lambda')
        lamdconf = client.get_function(FuntionName=lambdaname)
        lamdconf1 = lamdconf['Configuration']
        funcname = lamdconf1['FuntionName']
        funcarn = lamdconf1['FuntionArn']
        funcrt = lamdconf1['Runtime']
        funcrole = lamdconf1['Role']
        funchndlr = lamdconf1['Handler']
        lstmdfd = lamdconf1['LastModified']
        lambda_details.append("Details of lambda Function -----> " + funcname + "\n")
        lambda_details.append("\t" + "Function Name -----> " + funcname)
        lambda_details.append("\t" + "ARN -----> " + funcarn)
        lambda_details.append("\t" + "Run Time -----> " + funcrt)
        lambda_details.append("\t" + "Role -----> " + funcrole)
        lambda_details.append("\t" + "Handler -----> " + funchndlr)
        if "Environment" in lamdconf1:
            funcenv = lamdconf1['Environment']
            envvar = funcenv['Variables']
            lambda_details.append("\t" + "Environment Variables in Function ----> " + funcname)
            for key,value in envvar.items():
                environment_variables.append("\t" + key + ":" + value)
            lambda_details.append("\n\t".join(environment_variables))
        else:
            lambda_details.append("\t" + "Environment Variables doesn't exist in Function ----> " + funcname)

    except:
        lambda_details.append(f"Error: [Lambda - {lambdaname}]: {sys.exc_info()[0]} | {sys.exc_info()[1]}")
