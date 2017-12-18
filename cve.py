#coding:utf8

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}

cveDetaillist=[]

def getdetail(url):
    print url
    req = requests.get(url,headers=headers)
    soup = BeautifulSoup(req.text,'lxml')
    cveNum = soup.select('#GeneratedTable > table > tr:nth-of-type(2) > td:nth-of-type(1) > h2')[0].text
    description = soup.select('#GeneratedTable > table > tr:nth-of-type(4) > td')[0].text
    cna = soup.select('#GeneratedTable > table > tr:nth-of-type(9) > td')[0].text
    dateCreated = soup.select('#GeneratedTable > table > tr:nth-of-type(11) > td:nth-of-type(1) > b')[0].text
    print [cveNum, description, cna, dateCreated]
    #cveDetaillist.append()


def main():
    url='https://cassandra.cerias.purdue.edu/CVE_changes/today.html'
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text,'lxml')
    hreflist = soup.select('body > a')
    for cvenumber in hreflist:
        getdetail(cvenumber.get('href'))
    for l in  cveDetaillist:
        print cveDetaillist

#GeneratedTable > table > tbody > tr:nth-child(2) > td:nth-child(1) > h2


if __name__ == '__main__':
    main()

