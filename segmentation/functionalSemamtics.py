import re
SDrule="conj"

with open('data/电子商务parser.txt', 'r',encoding="utf-8") as f:
    lines=f.readlines()
    for line in lines:
        item=line.split(" ")
        # print(item)
        # item[2]=item[2][1:-2]
        # print(item[2])
        findSD=re.findall(r'nsubjpass\(.*?\)|dobj\(.*?\)',item[2])
        item.append(findSD)
        print(item[3])
        with open('data/电子商务初始目标.txt', 'a',encoding="utf-8") as f2:
            f2.write(str(item[3])+'\n')



# str="det(接口-2,本-1),nsubj(提供-3,接口-2),root(ROOT-0,提供-3),conj(图形验证码-11,英文-4),conj(图形验证码-11,数字-6),
#           conj(图形验证码-11,中文-8),cc(图形验证码-11,或-9),nn(图形验证码-11,混合型-10),assmod(识别-13,图形验证码-11),assm(图形验证码-11,的-12),dobj(提供-3,识别-13)";
# pattern=re.compile("conj")
# print(re.findall(r'dobj\(.*?\)|conj\(.*?\)',str))
