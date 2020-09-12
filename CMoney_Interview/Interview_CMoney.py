#!/usr/bin/env python
# coding: utf-8

# In[26]:


import csv
import time 
import pandas as pd
from selenium import webdriver 

# 下載台灣銀行當日匯率CSV檔，利用Chrome當webdriver
driverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path = driverPath)
browser.get('https://rate.bot.com.tw/xrt/flcsv/0/day')

# 台灣銀行當日匯率CSV檔(檔名)
csv_raw = 'ExchangeRate@202009111602.csv'

# 讀取檔案，開啟檔案，將CSV_raw的資料存入csvReader中
with open(csv_raw) as csvFile:
    csvReader = csv.reader(csvFile)
    listReport = list(csvReader)

# 創建資料存處位置
newlistReport = list() 
tmplist = []

# 存入所有的(幣別、匯率、現金匯率、即期匯率)資料 in newlistReport
for row in listReport:
    tmplist = [row[0], row[1], row[2], row[3]]
    newlistReport.append(tmplist)
    
# 幣別、匯率、現金匯率、即期匯率
JPY_data = dict()
for row in newlistReport:
# 當幣別 = 日幣(JPY)時，存入字典中
    if row[0] == 'JPY':
        JPY_data['幣別'] = row[0]
        JPY_data['匯率'] = row[1]
        JPY_data['現金匯率'] = row[2]
        JPY_data['即期匯率'] = row[3]
# 列印出資料做確認        
#         print('幣別: %4s\t\n匯率: %3s\t\n現金匯率: %3s\t\n即期匯率: %s ' \
#               %(row[0], row[1], row[2], row[3]))
        
# 命名輸出 txt檔案
timestr = time.strftime('%Y%m%d')
nametxt = timestr + '_日幣匯率.txt'

# 打開 nametxt 的檔案，寫入'utf-8'資料方法
f1 = open(nametxt, 'w', encoding = 'utf-8')
# 將字典JPY_data的 key(名稱) & value(值)寫入 txt 檔案內 
for key, value in JPY_data.items():
    f1.write(key + ':' + value + '\n')
f1.close()

# 列印出txt做驗證        
check_text = open(nametxt, encoding = 'utf-8')
print(check_text.read())


# In[ ]:




