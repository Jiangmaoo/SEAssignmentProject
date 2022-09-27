import math
import matplotlib.pyplot as plt
import csv
import numpy
'''隔行提取飞机路径点'''
with open('FlightPath.csv',encoding='utf-8-sig') as f:
    with open('LIDARPoints.csv', encoding='utf-8') as file:
        reader=csv.reader(f)
        header=next(reader)
        readerP = csv.reader(file)
        next(readerP)
        pointA=[] #pointA[1:2] 第二行的数据
        pointB=[]
        pointa = []#转化为直角坐标的X轴
        pointb = []
        k=0
        #通过k来控制隔行输出
        for i in reader:
            if(k%2==0):#导入偶数行数据
                r1 = float(i[0])*1000   #换算单位
                pointA.append(r1)
                r2 = float(i[1])*1000
                pointB.append(r2)
                print(r1,r2)
                # angle = []
                # x = []
                '''无人机扫描到的数据，没533or534数据为一组，当一组数据导入完毕，
                跳出循环，使用无人机下一个位置
                扫描到的数据'''
                for j in readerP:
                    if(j[1]=='533'):
                        break
                    if(j[1]=='534'):
                        break
                    p1 = float(j[0])
                    p2 = float(j[1])
                    # angle.append(p1)
                    # x.append(p2)
                    #将极坐标转化为直角坐标
                    pointa1 = r1 + numpy.cos(p1/180*math.pi) * p2
                    pointa.append(pointa1)
                    pointb1 = r2 - numpy.sin(p1/180*math.pi) * p2
                    pointb.append(pointb1)
                    #print(r1, r2)
            k=k+1
        #生成散点图和折线图
        fig = plt.figure(dpi=128, figsize=(10, 6))
        # plt.scatter(pointA, pointB, c='red')
        plt.scatter(pointa, pointb, c='red')
        plt.plot(pointA, pointB, 'ro-', color='blue', alpha=1, label='路线图')
        plt.show()









