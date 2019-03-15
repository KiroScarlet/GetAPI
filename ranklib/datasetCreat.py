import random

QoSData=[]
for i in range(10):#随机建立10个Web服务，
    QoSData.append({"ID":i,
                     "Availability":random.randint(0,100),
                     "Reliability":random.randint(0,100),
                     "Throughput":random.randint(0,100),
                     "ResponseTime":random.randint(0,100),
                     "Successability":random.randint(0,100),
                     "Compliance":random.randint(0,100),
                     "Cost":random.randint(0,100)})


# print(QoSData)


#用户1：按照加权求和的方法，权值为1
QoSData1=QoSData[:]
for i in QoSData1:
    i["sum"]=(i["Availability"]+i["Reliability"]+i["Throughput"]+i["ResponseTime"]+i["Successability"]+i["Compliance"]+i["Cost"])


def WADD_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i]["sum"] > lists[j]["sum"]:
                lists[i], lists[j] = lists[j], lists[i]

def LEX_sort(lists):#词典策略
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i]["Availability"] > lists[j]["Availability"]:
                lists[i], lists[j] = lists[j], lists[i]
            elif lists[i]["Availability"] == lists[j]["Availability"]:
                if lists[i]["Reliability"] > lists[j]["Reliability"]:
                    lists[i], lists[j] = lists[j], lists[i]
                elif lists[i]["Reliability"] == lists[j]["Reliability"]:
                    if lists[i]["Throughput"] > lists[j]["Throughput"]:
                        lists[i], lists[j] = lists[j], lists[i]

def label_data(QoSdata):
    for i in range(len(QoSdata)):
        if i>8:
            QoSdata[i]["label"]=1
        else:
            QoSdata[i]["label"] = 0


if __name__ == '__main__':
    with open('8020.txt','w',encoding="utf-8") as f:
        for times in range(100):
            if random.randint(0,100)>80:
                LEX_sort(QoSData1)
                label_data(QoSData1)
                for i in range(len(QoSData1)):
                    f.write(str(QoSData1[i]["label"])+" "+"qid:"+str(times+1)+
                            " 1:" +str(QoSData1[i]["Availability"]/100)+" "+
                            " 2:" +str(QoSData1[i]["Reliability"]/100)+" "+
                            " 3:" +str(QoSData1[i]["Throughput"]/100)+" "+
                            " 4:" +str(QoSData1[i]["ResponseTime"]/100)+" "+
                            " 5:" +str(QoSData1[i]["Successability"] / 100) +" "+
                            " 6:" +str(QoSData1[i]["Compliance"] / 100) +" "+
                            " 7:" +str(QoSData1[i]["Cost"] / 100)
                            +" #"+str(QoSData1[i]["ID"])+'\n')
            else:
                WADD_sort(QoSData1)
                label_data(QoSData1)
                for i in range(len(QoSData1)):
                    f.write(str(QoSData1[i]["label"])+" "+"qid:"+str(times+1)+
                            " 1:" +str(QoSData1[i]["Availability"]/100)+" "+
                            " 2:" +str(QoSData1[i]["Reliability"]/100)+" "+
                            " 3:" +str(QoSData1[i]["Throughput"]/100)+" "+
                            " 4:" +str(QoSData1[i]["ResponseTime"]/100)+" "+
                            " 5:" +str(QoSData1[i]["Successability"] / 100) +" "+
                            " 6:" +str(QoSData1[i]["Compliance"] / 100) +" "+
                            " 7:" +str(QoSData1[i]["Cost"] / 100)
                            +" #"+str(QoSData1[i]["ID"])+'\n')





# QoSData1.sort(key=lambda x: x["sum"])

WADD_sort(QoSData1)
label_data(QoSData1)

for i in QoSData1:
    print(i)


def sort(list):
    count=len(list)
    for i in range(0,count):
        for j in range(i+1,count):
            if list[i][8]>list[j][8]:
                list[i],list[j]=list[j],list[i]





def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists