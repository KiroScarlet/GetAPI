import jieba
import jieba.posseg as pseg
import jieba.analyse

with open('data/电子商务.txt', 'r',encoding="gbk") as f:
    lines=f.readlines()
    writeLine=[]
    for line in lines:
        line=line.split(' ')
        # print(line)
        # print(line[2])
        line[2]=jieba.cut(line[2])
        # print(' '.join(line[2]))
        line[2]=' '.join(line[2])
        print(line[2])
        writeLine.append(line[0]+';;'+line[1]+';;'+line[2]+'\n')

    print(writeLine)
    with open('data/电子商务2.txt', 'a',encoding="gbk") as f2:
        for i in writeLine:
            f2.write(i)