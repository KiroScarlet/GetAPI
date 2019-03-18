import requests
import json

#DOWNLOAD_URL= 'https://market.aliyun.com/api/ajax/product/queryProducts.json?pageSize=10&pageIndex=12&categoryId=56956004'

def download_page(url):
    headers={
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
        'DNT': '1',
        'Cookle':'aliyun_choice=CN; UM_distinctid=16252e0a2044a4-0ad80b3f8f6232-3a614108-144000-16252e0a205e39; _ga=GA1.2.1810734562.1521808876; cna=c/VxE7bBgBYCAd5CdRTvbbtP; _gid=GA1.2.82934157.1533358592; mplace_session_id=0N566AA1-TB9XB4RPUY1WN0QED6LX3-AVDB4JKJ-QWM7; spmSource=9PKJFA4P3yZ%2BlTe0t3G2p%2BBJx82N1HxWvSdv7mIo%2FJJXbVk94mOweZQdK6dw0o9eVB5edvuGw8lOMUGmicaAvK0hSHbIdaU1; mplace0=%2FZLTRHNsQmjZe31eOO0OsUZB3XOBJIYa6468yNWZriGl5%2BklUBZxDAELiToQ0BA1wsGZQ%2B44HKuiRMb2G2wuHY1EpbZvM3v03RuEfR8zlMa3aLpc51L%2Bw3kc1c9OSfX3t995VJyvR9E6lQKiF%2B29lIkdyIsZ1jqa4%2Fg5%2FPDHZN8%3D; isg=BNjYDIp9N9IlcBqLN1Jt9qF6qQaqaT3feAoKzRLSeJdOrTmXq9Az2lLL4aU4vfQj',
        'Referer': 'https://market.aliyun.com/products/56956004?spm=5176.730005-56956004-56928004.0.0.wG7C9O',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data=requests.get(url,headers=headers)
    return data.text

def get_API_url(data,API_url_list):
    data=(json.loads(data))
    print(data)
    data=(data.get('result').get('products'))
    #print(data)
    for i in data:
        API_url_list.append([i['url'],
                             i['name'],
                             i['short_description'].replace("\n","").replace(" ...","。"),
                             ])


#分类对应关系：名称，页数，categoryId
APIclass=[["电子商务",24,'56928004'],
          ["金融理财",21,'57000002'],
          ["交通地理",10,'57002002'],
          ["企业管理",5,'56928005'],
          ["公共事务",4,'57002003'],
          ["气象水利",3,'57096001'],
          ["人工智能",18,'57124001'],
          ["生活服务",16,'57126001']
          ]

import xlwt

def save_class(className,pageSize,categoryId):
    API_url_list=[]
    for i in range(1):#为了避免遗漏，可以多做几次
        for j in range(pageSize):
            DOWNLOAD_URL='https://market.aliyun.com/api/ajax/product/queryProducts.json?pageSize=10&pageIndex='+str(j+1)+'&categoryId='+categoryId
            data=download_page(DOWNLOAD_URL)
            get_API_url(data,API_url_list)


    with open('data/'+className+'.txt','w') as f:
        for i in range(len(API_url_list)):
            for j in range(len(API_url_list[i])):
                f.write(API_url_list[i][j]+' ')
            f.write("\n")


'''
    #创建workbook（其实就是excel，后来保存一下就行）
    workbook = xlwt.Workbook(encoding='utf-8')
    #创建表
    worksheet = workbook.add_sheet('My Worksheet')
    #往单元格内写入内容

    for i in range(len(API_url_list)):
        for j in range(len(API_url_list[i])):
            worksheet.write(i, j, label=API_url_list[i][j])

    #保存
    # workbook.save(className+'.xls')
'''


if __name__=='__main__':
    for className,pageSize,categoryId in APIclass:
        save_class(className,pageSize,categoryId)