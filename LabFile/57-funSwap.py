# 57-WAP to swap the values of two variable that are defined as global variables
fn,sn=5,18
def swap():
    global fn,sn
    temp=fn
    fn=sn
    sn=temp
    print("After Swapping:\n First Num={} and Second Num={}".format(fn,sn))

swap()