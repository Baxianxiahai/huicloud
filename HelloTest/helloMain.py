'''
Created on 2018/4/17

@author: WY
'''

#!/opt/bin/python3.6
# -*- coding: UTF-8 -*-

import datetime
import string
import sys
import time
import json
import os
import re
import socket
import ctypes 
import re
import random


#1)       Create a class named “A”, it have an function “convert” , it can transfer “A”-“Z” to 1-26, for example “B” to 2, ignore lower case and upper case(“b” also to 2)   
class A(object):
    def convert(self, c):
        if (len(c)!=1):
            return -1;
        b = c.lower()
        return (ord(b) - ord("a") + 1);

#2 Check - is the file “input.txt” in “D:\”, if not print error info on screen and exit program.
def func2_judge_file_exist(path, fileName):
    if (os.path.exists(path) == False):
        print("File path %s not exist!" %(path))
        return False;
    if (os.path.isfile(path + fileName) == False):
        print("File name %s not exist!" %(fileName))
        return False;
    return True;


#3)       
#If file is exist, read file.
# File content format will like this:
# 
# AAB,90
# 
# Gexingmi0n, 8
# 
# Xiaomin,80
# 
# Junjun,100
# 
# ……

def func3_read_file(path, fileName):
    if (func2_judge_file_exist(path, fileName) == True):
        with open(path + fileName, mode='r+', encoding='utf-8') as f:
            print("==>Starting to output content:")
            for line in f:
                print(line.strip()) #去掉换行
            print("==>File print finished!")


#TEST 4
#4)       Use regular expression  check if “AAB” or “Xiaomin” or “Junjun” only have include 26 letters, if not convert to 0
def func4_check_string_regular(myStr):
    #content = re.match('.*\d.*', myStr)
    #content = re.search(r'\d*', myStr)
    totalCount = re.sub("\D", "", myStr)
    if (totalCount != ''):
        return totalCount;
    else:
        return 0; 


#5)       Use class “A” function , convert AAB to 4 (1+1+2)
def func5_caculate_result(myStr):
    length = len(myStr);
    if (length <=0):
        return -1;
    obj = A();
    res = 0;
    for i in range(length):
        ch = myStr[i]
        res += obj.convert(ch);
    return res;

# 6)       Print result on screen like this:
# 
# AAB,90,4
# 
# Gexingmin0n,8,0
# 
# Xiaomin,80,85
# 
# Junjun,100,90
# 
# ….
def func6_print_screen_file_content(path, fileName):
    if (func2_judge_file_exist(path, fileName) == True):
        with open(path + fileName, mode='r+', encoding='utf-8') as f:
            for line in f:
                strOrigin = line.strip() #去掉换行
                if len(strOrigin) <= 3:
                    continue;
                if (strOrigin.find(',') < 0):
                    continue;
                strTmp = strOrigin.split(',');
                if (len(strTmp) != 2):
                    continue;
                nbr = func5_caculate_result(strTmp[0])
                print("%s,%d" % (strOrigin, nbr))
    return True;



# Case 6
# 1)       Create a class named “A”, it have an function “convert” , it can transfer “6” to 6 （int）。 it have an error expect function when input like “a”， cannot convert to int type，then output 0\
# 
# 2)       Create a class named “B”, it have a function “convert” , it can convert  “90” like this: get several random int  numbers range is (1-52), the sum of these number is equal to 90, convert these numbers to string.
# 
# 3)       Check - is the file “input.txt” in “D:\”, if not print error info on screen and exit program.
# 
# 4)       If file is exist, read file.
# 
# File content format will like this:
# 
# AAB,90
# 
# 87689, 8
# 
# Xiaomin9,8a
# 
# Junjun,100
# 
# ……
# 
# 5)       Use class “A” function  , convert AAB to 0 (0+0+0)，convert 87689 to 38
# 
# 6)       use try… except convert “90” to int, if error is catched output 0, else use class “B” function   “convert”, convert “90” to “52+38”  -------- “52+1+37 “ also ok
# 
# 7)       Print result on screen like this:
# 
# AAB,90,0,52+1+37
# 
# 87689,8,38,1+2+3+3
# 
# Xiaomin,8a,0,0
# 
# Junjun,10b,0,0

class AA(object):
    def convert(self, c):
        if (len(c)!=1):
            return -1;
        print(ord(c))
        tmp = ord(c);
        if ((tmp < ord('0')) or (tmp > ord('9'))):
            return 0;
        tmp = int(c, 10)
        if tmp != '':
            return tmp;
        else:
            return 0;

class BB(object):
    def convert(self, nbrStr):
        if (len(nbrStr) <=0):
            return ''
        target = int(nbrStr, 10)
        if target <=0:
            return ''
        accu = 0;
        res = {}
        index = 0;
        #print(accu, target)
        while (accu < target):
            tmp = int((random.random() * 10000)) % 53
            while (accu + tmp) > target:
                tmp = int((random.random() * 10000)) % 53
            #print(tmp)
            res[index] = tmp;
            index += 1;
            accu += tmp;
            if (accu == target):
                break;
        strResult = str(res[0])
        for i in range (1, index):
            strResult += '+'
            strResult += str(res[i])
        #print(strResult)
        return strResult

def case6_func5_caculate_result(myStr):
    length = len(myStr);
    if (length <=0):
        return -1;
    obj = AA();
    res = 0;
    for i in range(length):
        ch = myStr[i]
        res += obj.convert(ch);
    return res;

def case6_func6_try_except(myStr):
    flag = 1;
    try:
        res = int(myStr, 10)
    except Exception as err:
        flag = -1;
    finally:
        if (flag == -1):
            return 0;
    #Continue procssing
    obj = BB();
    return obj.convert(str(res))


def case6_func7_print_screen_file_content(path, fileName):
    if (func2_judge_file_exist(path, fileName) == True):
        with open(path + fileName, mode='r+', encoding='utf-8') as f:
            for line in f:
                strOrigin = line.strip() #去掉换行
                if len(strOrigin) <= 3:
                    continue;
                if (strOrigin.find(',') < 0):
                    continue;
                strTmp = strOrigin.split(',');
                if (len(strTmp) != 2):
                    continue;
                nbr = func5_caculate_result(strTmp[0])
                myString = case6_func6_try_except(str(nbr))
                print("%s,%d,%s" % (strOrigin, nbr, myString))
    return True;











#SYSTEM ENTRY
if __name__ == '__main__':
    print("[MY EXAM] ", time.asctime(), ", Starting...\n" );

    #===========================
    #BASIC CASE
    #===========================
    #Test 1
    obj = A();
    print("BASIC-CASE TEST1:", obj.convert("Z"))

    #Test 2
    print("\nBASIC-CASE TEST2:", func2_judge_file_exist("D:\\", "Input.txt"));

    #Test 3
    print("\nBASIC-CASE TEST3:")
    func3_read_file("/home/hitpony/", "ros_readme.txt")

    #Test 4
    print("\nBASIC-CASE TEST4:", func4_check_string_regular("Thi3sada"))

    #Test 5
    print("\nBASIC-CASE TEST5:", func5_caculate_result("ADDDDZ"))
    
    #Test 6
    print("\nBASIC-CASE TEST6:");
    func6_print_screen_file_content("/home/hitpony/", "a.txt")
    
    #===========================
    #CASE6
    #===========================
    #Test 1
    obj = AA();
    print("CASE6 TEST1:", obj.convert("A"))

    #Test 2
    print("\nCASE6 TEST2:")
    obj = BB();
    obj.convert("40")
    
    #Test 3: Same as Basic Case Test2
    #Test 4: Same as Basic Case Test3

    #Test 5
    print("\nCASE6 TEST5:", case6_func5_caculate_result("AA"))

    #Test 6
    print("\nCASE6 TEST6:", case6_func6_try_except("90"))
    
    #Test 7
    print("\nCASE6 TEST7:")
    case6_func7_print_screen_file_content("/home/hitpony/", "a.txt")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
