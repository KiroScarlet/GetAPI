# -*- coding: utf-8 -*-
# filename:GoogleTranslation1.2.py

import urllib.parse
import urllib.request
from tkinter import *
import xlrd

def translate(text, f='zh-cn', t='en'):
    url_google = 'http://translate.google.cn/translate_t'
    reg_text = re.compile(r'(?<=TRANSLATED_TEXT=).*?;')
    user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 r'Chrome/44.0.2403.157 Safari/537.36'
    '''user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)'''''
    values = {'hl': 'zh-cn', 'ie': 'utf-8', 'text': text, 'langpair': '%s|%s' % (t, f)}
    value = urllib.parse.urlencode(values)

    req = urllib.request.Request(url_google + '?' + value)

    req.add_header('User-Agent', user_agent)
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')
    data = reg_text.search(content)
    result = data.group(0).strip(';').strip('\'')
    return result


def save():
    data = xlrd.open_workbook('webAPI.xls')  # 打开xls文件
    #print(data.sheet_names())
    table = data.sheet_by_index(0)  # 打开第一张表
    nrows = table.nrows  # 获取表的行数
    with open('API.txt','w',encoding='utf-8') as f:
        for i in range(nrows):
            f.write(str(translate(table.row_values(i)[0])))
            f.write('类别：')
            f.write(str(translate(table.row_values(i)[1])))
            f.write('\n')
            print(i+1)



if __name__ == "__main__":
    save()