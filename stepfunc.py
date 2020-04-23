import sys
import boto3

def step_func(funcname):
    step_function_details=[""]
    try:
        client = boto3.client('stepfunctions')
        response = client.describe_state_machine(stateMachineArn=funcname)
        sfname = response['name']
        sfstat = response['status']
        sfrlarn = response['roleArn']
        sfdef = response['definition']
        step_function_details.append("Details of step function ----> " + funcname.split(":")[6] + "\n")
        step_function_details.append("\t" + "Name ---> " + sfname)
        step_function_details.append("\t" + "Status ---> " + sfstat)
        step_function_details.append("\t" + "Role ARN ---> " + sfrlarn)
        step_function_details.append("\t" + "Definition ---> " + "\n\t" + sfdef)
        step_function_details.append("\n")
    except:
        step_function_details.append(f"Error: [Step Function - {funcname}]: {sys.exc_info()[0]} | {sys.exc_info()[1]}")