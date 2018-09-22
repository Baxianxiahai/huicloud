'''
Created on 2017年12月11日

@author: hitpony
'''
import cv2
import numpy as np  
#import matplotlib.pyplot as plt
#import imutils
from ctypes import c_uint8
#import argparse
#import math
import random
import sys
import time
import json
import os   #Python的标准库中的os模块包含普遍的操作系统功能  
import re   #引入正则表达式对象  

class ClassModVisionTest1:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def cmdHandleProcedure(self, input):
        return True


class ClassModVisionTest2(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def cmdHandleProcedure(self, input):
        return True  
    
class ClassModVisionWormClasifySingle(object):
    '''
    classdocs
    '''
    #参数配置
#     lowThreshold = 0
#     max_lowThreshold = 100
#     ratio = 3   
#     kernel_size = 5
    #分类大小的参数确定定义
    HST_VISION_WORM_CLASSIFY_BASE_DEFAULT = 600;
    HST_VISION_WORM_CLASSIFY_SMALL2MID_DEFAULT = 1500;
    HST_VISION_WORM_CLASSIFY_MID2BIG_DEFAULT = 2500;
    HST_VISION_WORM_CLASSIFY_BIG2TOP_DEFAULT = 5000;

    #分类大小的参数定义
    HST_VISION_WORM_CLASSIFY_base = 0;
    HST_VISION_WORM_CLASSIFY_small2mid = 0;
    HST_VISION_WORM_CLASSIFY_mid2big = 0;
    HST_VISION_WORM_CLASSIFY_big2top = 0;
    
    #处理的图片和文档
    HST_VISION_WORM_CLASSIFY_pic_filepath = ""
    HST_VISION_WORM_CLASSIFY_pic_filename = ""
    
    #处理后的结果
    HST_VISION_WORM_CLASSIFY_pic_sta_output = {'totalNbr':0, 'bigAlive':0, 'bigDead':0, 'middleAlive':0, 'middleDead':0, 'smallAlive':0, 'smallDead':0, 'totalAlive':0, 'totalDead':0}

    #初始化
    def __init__(self):
#         lowThreshold = 0
#         max_lowThreshold = 100
#         ratio = 3   
#         kernel_size = 5
        self.HST_VISION_WORM_CLASSIFY_base = self.HST_VISION_WORM_CLASSIFY_BASE_DEFAULT;
        self.HST_VISION_WORM_CLASSIFY_small2mid = self.HST_VISION_WORM_CLASSIFY_SMALL2MID_DEFAULT;
        self.HST_VISION_WORM_CLASSIFY_mid2big = self.HST_VISION_WORM_CLASSIFY_MID2BIG_DEFAULT;
        self.HST_VISION_WORM_CLASSIFY_big2top = self.HST_VISION_WORM_CLASSIFY_BIG2TOP_DEFAULT;
        self.HST_VISION_WORM_CLASSIFY_pic_filepath = "./imgFile/"
        self.HST_VISION_WORM_CLASSIFY_pic_filename = "1.jpg"
        self.HST_VISION_WORM_CLASSIFY_pic_sta_output = {'totalNbr':0, 'bigAlive':0, 'bigDead':0, 'middleAlive':0, 'middleDead':0, 'smallAlive':0, 'smallDead':0, 'totalAlive':0, 'totalDead':0}

    def func_vision_worm_input_processing(self, inputStr):
        try:
            if ((inputStr['cfBase'] < inputStr['cfSmall2MidIndex']) and (inputStr['cfSmall2MidIndex'] < inputStr['cfMid2BigIndex']) and (inputStr['cfMid2BigIndex'] < inputStr['cfBig2TopIndex'])):
                self.HST_VISION_WORM_CLASSIFY_base = inputStr['cfBase'];
                self.HST_VISION_WORM_CLASSIFY_small2mid = inputStr['cfSmall2MidIndex'];
                self.HST_VISION_WORM_CLASSIFY_mid2big = inputStr['cfMid2BigIndex'];
                self.HST_VISION_WORM_CLASSIFY_big2top = inputStr['cfBig2TopIndex'];
                self.HST_VISION_WORM_CLASSIFY_pic_filename = inputStr['fileName'];
            else:
                print("ModVisionGeneral: func_vision_worm_input_processing on input error!")
        except Exception as err:
            text = "ModVisionGeneral: func_vision_worm_input_processing on input error = %s" % str(err)
            print(text);

    def func_vision_worm_binvalue_test(self, img):
        #生成新图像
        #new = res.copy()
        #new = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
        new = np.zeros(img.shape, np.uint8)    
    
        #灰度化
        for i in range(new.shape[0]):  #Axis-y/height/Rows
            for j in range(new.shape[1]):
                (b,g,r) = img[i,j]
                #均值算法
                #new[i,j] = (int(b)+int(g)+int(r))/3
                #最大值法
                #new[i,j] = max(int(b), int(g), int(r))
                #加权平均法
                new[i,j] = int(0.3*float(b) + 0.59*float(g) + 0.11*float(r))&0xFF
    
        #强制8bit转换
        #new = cv2.convertScaleAbs(new)
    
        #中值滤波
        blur= cv2.medianBlur(new, 5)
        midGray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('Middle Blur', midGray)
    
        #固定二值化
        #ret, binNew = cv2.threshold(new, 130, 255, cv2.THRESH_BINARY)
    
        #自适应二值化
        binGray = cv2.adaptiveThreshold(midGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 43, 5)   # ADAPTIVE_THRESH_MEAN_C ADAPTIVE_THRESH_GAUSSIAN_C
        binRes= cv2.GaussianBlur(binGray, (5,5), 1.5) #medianBlur
        #cv2.imshow('Adaptive Bin', binRes)
        return binRes;
    
    def func_vision_worm_remove_noise_test(self, img):
        # 膨胀+腐蚀等形态学变化  
        kerne1 = np.ones((7, 7), np.uint8)  
        img_erosin = cv2.erode(img, kerne1, iterations=1)
        
        #图像相与  
        #img_bit = cv2.bitwise_and(img, img, mask=img_erosin)
        #ret, img_threshold = cv2.threshold(img_erosin, 5, 250, cv2.THRESH_BINARY)  # 二值化   
        #img_bit= cv2.cvtColor(img_threshold, cv2.COLOR_BGR2GRAY)
    
        #再次中值滤波
        midFilter= cv2.medianBlur(img_erosin, 5)
        
        #固定二值化
        ret, binImg = cv2.threshold(midFilter, 130, 255, cv2.THRESH_BINARY)
        #cv2.imshow("img_erosin and Noise removal", binImg)
        
        #其他核的腐蚀膨胀
    #     kerne3 = np.ones((51, 51), np.uint8)  
    #     img_erosin1 = cv2.erode(img, kerne3, iterations=1)  
    #     cv2.imshow("dil", img_erosin1)
    #     kerne2 = np.ones((2, 2), np.uint8)  
    #     img_dilation = cv2.dilate(img, kerne2, iterations=1)
    #     cv2.imshow("ers",img_dilation)
        
        #通过连续腐蚀和膨胀，来降低噪声
    #     kerne3 = np.ones((7, 7), np.uint8)  
    #     img_dilation1 = cv2.dilate(binImg,kerne3,iterations=1)
    #     cv2.imshow("ers",img_dilation1)
        
        return binImg;
    
    
    #https://www.cnblogs.com/llfisher/p/6557611.html
    #https://www.cnblogs.com/nanyangzp/p/3496486.html
    #偏心率：以质心为中心，所有点到X轴的长度综合，相比Y周的长度总和，他们之间的比值。
    #圆形=1，长条就是斜率
    # E = (M20-M02+4M11)/A, Mjk = EE(x-xA)^j * (y-yA)^k, (j+k阶矩)，A为面积
    #http://wenku.baidu.com/link?url=4ZSLxGBKE3LBf2mdxDs0VJ1cjJ3hxqeORu-3mfXO23gGBqf5LyjqZ4AHFCMLeP32xEKkoj5tPsWHdvA2ovmuKiRDKN6YHFO9G7JOzBWWrMC
    
    #http://blog.csdn.net/app_12062011/article/details/51953030
    #E = sqrt(1-I^2)
    #I = (u20+u02-sqrt(4u11*u11(u20-u02)*(u20-u02))/(u20+u02+sqrt(4u11*u11(u20-u02)*(u20-u02))
    def func_vision_worm_find_contours(self, nfImg, orgImg):
        #找到轮廓
        _, contours, hierarchy = cv2.findContours(nfImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #RETR_TREE, RETR_CCOMP
        #contours = contours[0] if imutils.is_cv2() else contours[1]
        
        #绘制轮廓
        #cv2.drawContours(orgImg, contours, -1, (0,0,255), 1)
        #cv2.imshow("contours marked image", orgImg)
    
        #输出图形
        outputImg = cv2.cvtColor(nfImg, cv2.COLOR_GRAY2BGR)
    #     outputImg = np.zeros(orgImg.shape, np.uint8)
    #     outputImg = cv2.cvtColor(outputImg, cv2.COLOR_BGR2GRAY)
    #     ret, outputImg = cv2.threshold(outputImg, 130, 255, cv2.THRESH_BINARY_INV)
    #     outputImg = cv2.cvtColor(outputImg, cv2.COLOR_GRAY2BGR)
        mask = np.zeros((orgImg.shape[0]+2, orgImg.shape[1]+2), np.uint8)
        mask[:] = 1
        #分别分析
        for c in contours:
            #外矩形框
            (x,y,w,h)=cv2.boundingRect(c)
            pointx=x+w/2
            pointy=y+h/2
            # compute the center of the contour
            M = cv2.moments(c)
            cX = int(M["m10"] / (M["m00"]+0.01))
            cY = int(M["m01"] / (M["m00"]+0.01))
            seed_point = (cX, cY)
            #轮廓面积
            cArea = cv2.contourArea(c)
            #轮廓弧长
            cPerimeter = cv2.arcLength(c,True)
            
            #第一种传统计算偏心率：数值无限大，不靠谱
            #E = (M20-M02+4M11)/A
            #cE = float((M["m20"] - M["m02"] + 4.0 * M["m11"]) / (M["m00"]+0.01))
            #I = (u20+u02-sqrt(4u11*u11(u20-u02)*(u20-u02))/(u20+u02+sqrt(4u11*u11(u20-u02)*(u20-u02))
            
            #第二种计算偏心率：使用更复杂的工具，依然不行
    #         u20 = M["m20"]
    #         u02 = M["m02"]
    #         u11 = M["m11"]
    #         up = u20+u02
    #         um = u20-u02
    #         cI = (up- math.sqrt(4*u11*u11 + up*up))/(up + math.sqrt(4*u11*u11 + up*up) + 0.01)
    #         cE = math.sqrt(1-cI*cI)
            
            #第三种近似方式，采用面积和周长的比值：强多了，但依然不能很准确的界定
            #cE = cPerimeter / math.sqrt(cArea+0.01) / (2*math.sqrt(3.14))
            
            #第四种方法：
            rect = cv2.minAreaRect(c)
            # 长宽,总有 width>=height  
            width, height = rect[1]
            if (width > height):
                cE = height / (width+0.001)
            else:
                cE = width / (height+0.001)
            cE = round(cE, 2)
            #判定大小
    #         if cArea < 400: 
    #             pass
    #         else:
    #             # draw the contour and center of the shape on the image
    #             cv2.drawContours(outputImg, [c], -1, (0, 0, 255), 1)
    #             cv2.circle(outputImg, (cX, cY), 2, (0, 255, 0), -1)
    #             #cv2.putText(orgImg, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
            #最终决定不采用flood算法
            #print(self.HST_VISION_WORM_CLASSIFY_base)
            if cArea < self.HST_VISION_WORM_CLASSIFY_base:
                pass
            elif cArea < self.HST_VISION_WORM_CLASSIFY_small2mid:
                self.HST_VISION_WORM_CLASSIFY_pic_sta_output['totalNbr'] +=1
                #cv2.floodFill(outputImg, mask, seed_point,(0,0,255))
                cv2.drawContours(outputImg, c, -1, (0,0,255), 2)  
                if (cE < 0.5):
                    self.HST_VISION_WORM_CLASSIFY_pic_sta_output['smallDead'] +=1
                    self.HST_VISION_WORM_CLASSIFY_pic_sta_output['totalDead'] +=1
                else:
                    self.HST_VISION_WORM_CLASSIFY_pic_sta_output['smallAlive'] +=1
                    self.HST_VISION_WORM_CLASSIFY_pic_sta_output['totalAlive'] +=1               
                cv2.putText(outputImg, str(cE), (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            elif cArea < self.HST_VISION_WORM_CLASSIFY_mid2big:
                self.HST_VISION_WORM_CLASSIFY_pic_sta_output['totalNbr'] +=1
                #cv2.floodFill(outputImg, mask, seed_point,(0,255,0))  
                cv2.drawContours(outputImg, c, -1, (0,255,0), 2)
                if (cE < 0.5):
                    self.HST_VISION_WORM_CLASSIFY_pic_sta_output['middleDead'] +=1
                    self.HST_VISION_WORM_CLASSIFY_pic_sta_output['totalDead'] +=1
                else:
                    self.HST_VISION_WORM_CLASSIFY_pic_sta_output['middleAlive'] +=1
                    self.HST_VISION_WORM_CLASSIFY_pic_sta_output['totalAlive'] +=1            
                cv2.putText(outputImg, str(cE), (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            elif cArea < self.HST_VISION_WORM_CLASSIFY_big2top:
                self.HST_VISION_WORM_CLASSIFY_pic_sta_output['totalNbr'] +=1
                #cv2.floodFill(outputImg, mask, seed_point,(255,0,0))  
                cv2.drawContours(outputImg, c, -1, (255,0,0), 2)
                if (cE < 0.5):
                    self.HST_VISION_WORM_CLASSIFY_pic_sta_output['bigDead'] +=1
                    self.HST_VISION_WORM_CLASSIFY_pic_sta_output['totalDead'] +=1
                else:
                    self.HST_VISION_WORM_CLASSIFY_pic_sta_output['bigAlive'] +=1
                    self.HST_VISION_WORM_CLASSIFY_pic_sta_output['totalAlive'] +=1                        
                cv2.putText(outputImg, str(cE), (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(outputImg, str(self.HST_VISION_WORM_CLASSIFY_pic_sta_output), (10, 30), font, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
        return outputImg;
        pass;

    #分类总处理    
    def func_vision_worm_clasification(self, workMode):
        #读取文件
        try:
            inputImgFn = self.HST_VISION_WORM_CLASSIFY_pic_filepath + self.HST_VISION_WORM_CLASSIFY_pic_filename
            inputImg = cv2.imread(inputImgFn)
        except Exception as err:
            print("ModVisionGeneral: Read file error, errinfo = ", str(err))
            return;

        #处理过程
        binImg = self.func_vision_worm_binvalue_test(inputImg)
        nfImg = self.func_vision_worm_remove_noise_test(binImg)
        outputImg = self.func_vision_worm_find_contours(nfImg, inputImg)
        outputFn = self.HST_VISION_WORM_CLASSIFY_pic_filepath + "result_" + self.HST_VISION_WORM_CLASSIFY_pic_filename
        cv2.imwrite(outputFn, outputImg)
            
        # 存储干活的log记录
        f = open("./vision.log", "a+")
        a = '[%s], vision worm classification ones, save result as [%s].\n' % (time.asctime(), outputFn)
        f.write(a)
        f.close()
        
        #根据指令，是否显示文件
        if ("test" in workMode):
            cv2.imshow("Final output", outputImg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif ("batch" in workMode):
            cv2.destroyAllWindows()
        else:
            pass

    #通用总入口
    def cmdHandleProcedure(self, inputStr):
        self.func_vision_worm_input_processing(inputStr)
        #正式部署时，需要改为"formal"
        self.func_vision_worm_clasification("formal");  #"test", "batch" or "formal"
        return self.HST_VISION_WORM_CLASSIFY_pic_sta_output
        

class ClassModVisionWormClasifyBatch(ClassModVisionWormClasifySingle):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def cmdHandleProcedure(self, input):
        return True  



          