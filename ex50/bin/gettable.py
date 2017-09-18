
from selenium import webdriver
from urllib.parse import urljoin
import time
import csv
import codecs

#Phanttomjs Driverを入手
browser = webdriver.PhantomJS()

#取得したいURLを入力

url = "http://area-info.jpn.org/CrimPerPop.html"

#urlにアクセス

browser.get(url)
browser.implicitly_wait(5)
print("指定されたページにログインしました")

#urlからテーブルデータを取得し数える
trs = browser.find_elements_by_xpath("/html/body/div/div[3]/table[1]/tbody/tr") #列をすべて取得
numberOfTR = len(trs) #列の数を調べる
print("取得した列の数")
print(numberOfTR)


#csvファイルの設定
with open('data1.csv', 'wt', encoding='utf-16') as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')

    #すべての列から一つずつ列を取り出し、その中身を一つずつ挿入していく
    for i in range (numberOfTR): #すべての列のうち、i列目を抽出
        csvRow = []
        tr = trs[i]#i列目のtdを取得
        print("現在の列：")
        print(i + 1)
        tds = tr.find_elements_by_tag_name("td") #その列のtdを取得
        numberOfTD = len(tds)
        print("tdの数：")
        print(numberOfTD)
        for j in range (numberOfTD): #cellをひとつひとつ取り出す
            td = tds[j]
            if td.text:
                print("tds[j]:")
                print(td.text)
                utd = str(td.text)
                csvRow.append(utd)
        writer.writerow(csvRow)
    csvfile.close()