# -*- coding: gb2312 -*-
import requests,os
from bs4 import BeautifulSoup
'''
    ��ȡ��Ȥ��С˵վС˵
'''
__author__ = "����"

# requests ����
def request_tool(url):
    response = requests.get(url)
    # ת������
    response.encoding = 'gbk'
    return response.text

# ��ȡ�����½�
def section_fun():
    # �½��б�
    section_list = []
    soup = BeautifulSoup(request_tool("http://www.cangqionglongqi.com/hunwushuangxiu/"),"html.parser")
    divList = soup.find_all(id="list")
    base_url = "http://www.cangqionglongqi.com/hunwushuangxiu/"
    for div in divList:
        for a in div.find_all("a"):
            section_list.append({"title":a.text,"src":base_url + a.get("href")})
    return section_list

# ��ȡ�½�����
def crawl_text(path):
    soup = BeautifulSoup(request_tool(path),"html.parser")
    return soup.find(attrs={"id":"content"}).text

# ������
if __name__ == "__main__":
    for section in section_fun():
        # ����һ��Ŀ¼���С˵
        if os.path.exists("xs") == False:
            os.mkdir("xs")
        print("�������� =====> %s" % (section.get("title")))
        # Ϊÿһ�´���һ���ı�
        try:
            # print(crawl_text(section.get("src")))
            with open("xs/"+section.get("title") +".txt","w",encoding="utf-8") as f:
                f.write(crawl_text(section.get("src")))
        except Exception as e:
            print("�����ļ��쳣��%s " % e)
