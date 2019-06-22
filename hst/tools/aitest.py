#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# coding=utf-8

import cv2
import numpy as np  
import matplotlib.pyplot as plt
import imutils
from ctypes import c_uint8
import argparse
import math
import random
import sys
import time
import json
import os   #Python的标准库中的os模块包含普遍的操作系统功能  
import re   #引入正则表达式对象  
#from __future__ import print_function
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data


def func_video_file_test():
    #cap = cv2.VideoCapture('/home/hitpony/EclipseJavaWs/test.avi')
    #cap = cv2.VideoCapture('/dev/v4l/by-id//dev/v4l/by-id/usb-CKF9237G261040003SI0_Laptop_Integrated_Webcam_2M-video-index0')
    #cap = cv2.VideoCapture('/dev/video0')
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture('test.avi')
    #b = cv2.imread('b3.jpg')
    #print(b)
    cnt = 0
    print("Cap=", cap)
    # 获取视频播放界面长宽
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    print("fps/width/height = ", (fps, width, height))
    cv2.namedWindow('input image',cv2.WINDOW_AUTOSIZE)
    #resizeImg = cv2.resize(posCutImg, (StandardCutImg.shape[1], StandardCutImg.shape[0]), interpolation = cv2.INTER_CUBIC)
   
    #循环
    ret, frame = cap.read()
    print("ret = ", ret)
    while(ret == True):
        cnt +=1
        ret, frame = cap.read()
        if (frame == None):
            print("Not exist file!")
            return;
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(cnt)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print("Finished.")
    cap.release()
    cv2.destroyAllWindows()
    pass

def func_video_camera_test():
    cap = cv2.VideoCapture(0)
    # 获取视频播放界面长宽
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    print("width/height = ", (width, height))  
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if (frame == None):
            print("Not exist camera!")
            return;
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()    
    pass


def func_plot_graph_test():
    N = 50 # 点的个数
    x = np.random.rand(N) * 2 # 随机产生50个0~2之间的x坐标
    y = np.random.rand(N) * 2 # 随机产生50个0~2之间的y坐标
    colors = np.random.rand(N) # 随机产生50个0~1之间的颜色值
    area = 3; #np.pi * (15 * np.random.rand(N))**2  # 点的半径范围:0~15 
    # 画散点图
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker=(9, 3, 30))
    plt.show()
    pass


def func_ai_mnist_gdo_algo_for_handwriting_test():
    mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)
    
    x = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784,10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.nn.softmax(tf.matmul(x,W) + b)
    y_ = tf.placeholder("float", [None,10]) 
    
    cross_entropy = -tf.reduce_sum(y_*tf.log(y))
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
    
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    for step in range(5000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        if step % 200 == 0:
            print("")
            print(step, sess.run(W), sess.run(b))        

    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print("")
    print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
    return;

def func_ai_min2_test():
    # Create 100 phony x, y data points in NumPy, y = x * 0.1 + 0.3
    N = 100
    x_data = np.random.rand(N).astype(np.float32)
    y_data = [i for i in range(N)]
    y_output = [i for i in range(N)]
    for i in range(N):
        y_data[i] = x_data[i]*10 + 0.3 + random.random()*2
    #y_data = x_data  + 0.3 + random.random() * 100
    
    # Try to find values for W and b that compute y_data = W * x_data + b
    # (We know that W should be 0.1 and b 0.3, but TensorFlow will
    # figure that out for us.)
    W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    b = tf.Variable(tf.zeros([1]))
    y = W * x_data + b
    
    # Minimize the mean squared errors.
    loss = tf.reduce_mean(tf.square(y - y_data))
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(loss)
    
    # Before starting, initialize the variables.  We will 'run' this first.
    init = tf.global_variables_initializer()
    
    # Launch the graph.
    sess = tf.Session()
    sess.run(init)
    
    # Fit the line.
    for step in range(201):
        sess.run(train)
        if step % 20 == 0:
            print(step, sess.run(W), sess.run(b))
    
    # Learns best fit is W: [0.1], b: [0.3]
    weight = sess.run(W)
    bias = sess.run(b)
    for i in range(N):
        y_output[i] = x_data[i]*weight + bias

    #画图
    colors = np.random.rand(N) # 随机产生50个0~1之间的颜色值
    area = 3; #np.pi * (15 * np.random.rand(N))**2  # 点的半径范围:0~15 
    # 画散点图
    plt.figure(1)                # 第一张图
    plt.xlabel('WGT ADC Read')
    plt.ylabel('Weight Caculate')
    #添加标题
    plt.title('BFDF EVALUATION')
    plt.scatter(x_data, y_data, s=area, c=colors, alpha=0.5, marker=(9, 3, 30))
    plt.plot(x_data, y_output, color='black', linewidth=2)
    plt.grid(False)
    plt.show()
    pass



#ReLU算法
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    
def func_ai_mnist_leru_algo_for_handwriting_test():
    mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)
    sess = tf.InteractiveSession()
    x = tf.placeholder("float", shape=[None, 784])
    y_ = tf.placeholder("float", shape=[None, 10])
    #W = tf.Variable(tf.zeros([784,10]))
    #b = tf.Variable(tf.zeros([10]))

    #第一层卷积
    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])
    x_image = tf.reshape(x, [-1,28,28,1])
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)
    #第二层卷积 
    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)
    #密集连接层 
    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)    
    #Dropout 避免过拟合
    keep_prob = tf.placeholder("float")
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
    #输出层
    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])
    y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
    
    cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
    #ADAM优化器来做梯度最速下降
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
    #梯度下降
    #train_step = tf.train.GradientDescentOptimizer(1e-3).minimize(cross_entropy)
    correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    sess.run(tf.global_variables_initializer())
    for i in range(200):
        batch = mnist.train.next_batch(50)
        if i%100 == 0:
            train_accuracy = accuracy.eval(feed_dict={x:batch[0], y_: batch[1], keep_prob: 1.0})
            print("step %d, training accuracy %f"%(i, train_accuracy))
        train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
    
    print("test accuracy %f"%accuracy.eval(feed_dict={
        x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))  
    return;


#总入口
if __name__ == "__main__":
    #测试视频文件的读取
    #func_video_file_test()
    
    #测试摄像头抓取
    #func_video_camera_test()

    #测试散点图
    #func_plot_graph_test()

    #最小二乘法训练
    #func_ai_min2_test()
        
    #测试MNIST训练集合
    #func_ai_mnist_gdo_algo_for_handwriting_test()
    
    #改进的MNIST训练
    func_ai_mnist_leru_algo_for_handwriting_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    