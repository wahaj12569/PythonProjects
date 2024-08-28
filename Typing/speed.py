from time import *
import random as r

def mistake(para_test,user_test):
    error =0 
    for i in range(len(para_test)):
        try:
            if para_test[i]!= user_test[i]:
                error += 1
        except:
            error+=1
    return error

def speed_time(time_s,time_e,userinput):
    time_dely = time_e - time_s 
    time_R = round(time_dely,2)
    speed =len(userinput)/time_R
    return round(speed)    

while True:
    ck = input("Ready to test! (Yes/No)")
    if ck == 'yes' or ck=='Yes':
        test =["The quick brown fox jumps over the lazy dog","my name is wahaj","It is testing !"]
        test1= r.choice(test)
        print("        ****Typing speed****")
        print()
        print(test1)
        print()
        print()
        time_1 = time()
        test_input = input("Enter:")
        time_2 =time()

        print("Your Speed :",speed_time(time_1,time_2,test_input),"w/sec")
        print("Your Mistakes:",mistake(test1,test_input))
    elif ck == 'no' or ck =='No':
        print('Thanks You !')
        break
    else:
        print('InValid Input!!')