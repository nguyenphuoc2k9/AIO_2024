import math
import random
#1
def F1_Score_calculate(tp,fp,fn):
    if(tp != 0 and fp !=0 and fn !=0):
        if(type(tp) != type(0)):
            print("tp must be int")
        elif(type(fn) != type(0)):
            print("fn must be int")
        elif (type(fp) != type(0)):
            print("fp must be int")
        else:
            pre = tp/(tp+fp)
            recall = tp/(tp+fn)
            f1_score = 2*((pre*recall)/(pre+recall))
            print(f'precision is {pre} \n recall is {recall} \n f1-score is {f1_score}')
    else:
        print("tp and fp and fn must be greater than zero")
F1_Score_calculate(2,0,4)
#2
def is_number ( n ) :
 try :
    float ( n )
 except ValueError :
    return False
 return True
def elu(x):
    if x<=0:
        return 0.01*(math.exp(x)-1)
    else:
        return x
def relu(x):
    if x <= 0:
        return 0
    else:
        return x
def sigmoid(x):
    return 1/(1+math.exp(-x))
def activation_function(mode,x):
    x = float(x)
    if is_number(x):
        if mode == "relu":
            print(f"relu: f({x})={relu(x)}")
        elif mode == "elu":
            print(f"elu: f({x})={elu(x)}")
        elif mode == "sigmoid" : 
            print(f"sigmoid: f({x})={sigmoid(x)}")
        else:
            print(f'{mode} is not supported')
    else:
        print(f"{x} must be a number")
activation_function("relu",1.5)
#3
def MAE(num):
    sum = 0
    for i in range(0,num):
        target = random.uniform(0,10)
        predict = random.uniform(0,10)
        loss = abs(target - predict)
        print(f"loss name : MAE , sample : {i} , pred : {predict} , target : {target} ,loss : {loss}")
        sum += loss
    final_MAE = (1/num)*sum
    print(f"Final MAE : {final_MAE}")
def MSE(num):
    sum = 0
    for i in range(0,num):
        target = random.uniform(0,10)
        predict = random.uniform(0,10)
        loss = math.pow(target-predict,2)
        print(f"loss name : MAE , sample : {i} , pred : {predict} , target : {target} ,loss : {loss}")
        sum+=loss
    final_MSE = (1/num)*sum 
    print(f"Final MAE : {final_MSE}")
def regression_loss(num,loss):
    if num.isnumeric():
        num = int(num)
        if loss == "MAE":
            MAE(num)
        elif loss =="MSE":
            MSE(num)
        elif loss == "RMSE":
            math.sqrt(MSE(num))
    else:
        print("number of samples must be an integer number")
regression_loss("5","MSE")
#4
def giai_thua(x):
    result = 1
    for i in range(2,x+1):
        result *= i
    return float(result)
def sin(x,n):
    sum = 0
    for i in range(0,n):
        sum += ((-1)**i)*(x**(2*i +1)/giai_thua(2*i +1))
    print(sum)
def cos(x,n):
    sum = 0
    for i in range(0,n):
        sum+=((-1)**i)*(x**(2*i)/giai_thua(2*i))
    print(sum)
def sinh(x,n):
    sum = 0
    for i in range(0,n):
        sum+= (x**(2*i +1)/giai_thua(2*i +1))
    print(sum)
def cosh(x,n):
    sum = 0
    for i in range(0,n):
        sum += (x**(2*i)/giai_thua(2*i))
    print(sum)
cos(3.14,10)
#5
def MD_nRE(y,y_hat,n,p):
    print((y**(1/n)-y_hat**(1/n))**p)
MD_nRE(100,99.5,2,1)