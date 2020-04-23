from rsrctag import filterfunc
from lambdamd import lambda_func

def lambdatag(appkey,value):
    lmbdalist = []
    lmdafunc = []
    lambdarn = filterfunc("",appkey,value,"lambda")
    for i in lambdarn:
        lmdafunc.append(i.split(":")[6])

    for i in lmdafunc:
        lmbdalist.extend(lambda_func(i))

    return lmbdalist

