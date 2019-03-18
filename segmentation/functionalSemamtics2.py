import re
import copy
SDrule="conj"

with open('data/电子商务2parser.txt', 'r',encoding="utf-8") as f:
    lines=f.readlines()
    num=0
    for line in lines:
        item=line.split(" ")
        # print(item)
        item[2]=item[2][1:-2]
        # print(item[2])
        tmp1=re.split(r'\(|,|\),|\)',item[2])
        # print(tmp1)

        SDstructure=[]#构建数据结构来存储SD关系
        for i in range(int(len(tmp1)/3)):
            SDstructure.append([tmp1[i*3],tmp1[i*3+1],tmp1[i*3+2]])

        # print(SDstructure)

        CSG=[]#初始目标

        for sd in SDstructure:
            if sd[0]=='dobj':
                CSG.append([sd[1],sd[2],''])

        # print(CSG)



        #对conj关系进行扩展，但没有发现扩展后未重复的关系
        # CSGtmp=[]
        # CSGtmp=copy.deepcopy(CSG)
        # for ig in CSGtmp:
        #     for sd in SDstructure:
        #         if sd[0]=='conj':
        #             if sd[1]==ig[0]:
        #                 CSG.append([sd[1],ig[1],''])
        #             if sd[2]==ig[0]:
        #                 CSG.append([sd[2],ig[1],''])
        #             if sd[2]==ig[1]:
        #                 CSG.append([ig[0],sd[2],''])
        #             if sd[1]==ig[1]:
        #                 CSG.append([ig[0],sd[1],''])

        # 对nn关系进行扩展
        for sd in SDstructure:
            if sd[0] == 'nn':
                for ig in CSG:
                    if sd[1]==ig[1]:
                        ig.append(sd[2])
        for ig in CSG:
            ig.append('')

        for sd in SDstructure:
            if sd[0] == 'amod':
                for ig in CSG:
                    if sd[1]==ig[1]:
                        ig.append(sd[2])
        for ig in CSG:
            ig.append('')




        print(CSG)
        num=num+1

    print(num)




        # CSG=re.findall(r'nsubjpass\(.*?\)|dobj\(.*?\)',item[2])#正则匹配
        # print(CSG)
        # for ig in CSG:
        #     sgv=re.findall(r'服务,',ig)
            # print(sgv)
            # print(sgv[1][1:-1])


        # item.append(findSD)
        # print(item[3])
        # with open('data/电子商务初始目标2.txt', 'a',encoding="utf-8") as f2:
        #     f2.write(str(item[3])+'\n')


