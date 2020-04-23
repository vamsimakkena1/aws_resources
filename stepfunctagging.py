from rsrctag import filterfunc
from stepfunc import step_func

def steptag(appkey,value):
    steplist = []
    steparn = filterfunc("",appkey,value,"states")
    for i in steparn:
        steplist.extend(step_func(i))

    return steplist