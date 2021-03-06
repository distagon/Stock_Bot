# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:22:32 2015

@author: tim
"""
# 請先安裝 sudo apt-get install sendemail

import os
from datetime import datetime
from grs import BestFourPoint
from grs import Stock
from grs import TWSENo
from grs import OTCNo


Stock_no_name = TWSENo().all_stock  # 所有上市股票名稱與代碼字典 type: dict

OTC_no_name = OTCNo().all_stock     # 所有上櫃股票名稱與代碼字典 type: dict

stock_no_list = TWSENo().all_stock_no # 所有上市股票代碼

#stock_name_list = TWSENo().all_stock_name

OTC_no_list = OTCNo().all_stock_no # 所有上櫃股票代碼

#OTC_name_list = OTCNo().all_stock_name


content = "贏要衝,輸要縮."   #沒有辦法換行

time_now = datetime.now().strftime("%Y-%m%d") #今天的日期 ex:2015-0411
title = str(time_now+"-小小兵盤後機器人") #Email郵件的標題 ex:2015-0411-選股機器人

attachment = str(time_now)+'.txt' #附件名稱使用當日時間 ex:2015-0411.txt

fileopen = open(attachment, 'w') #開啟檔案,w沒有該檔案就新增

f = open('/home/tim/GMAIL.txt','r') #於前一個相對目錄中放置登入GMAIL帳號密碼,目的為了不再GitHub顯示出來.
ID = f.readline().strip('\n') #不包含換行符號\n
PW = f.readline().strip('\n')


fileopen.write('上市公司股票篩選\n\n\n')


fileopen.write("\n""+暴量長紅2天"+"\n\n")

#=====================
index = 1 
for i in stock_no_list:
    try:
        if BestFourPoint(Stock(i)).red_3():
           print i,'123'         #暴量長紅2天
           fileopen.write(str(index)+" "+"暴量長紅2天"+"-"+Stock_no_name[i].encode("UTF-8")+"-"+i+"-"+"成交張數"+"-"+str(int(Stock(i).raw[-1][1]/1000))+"\n")
           index = index + 1 
    except:     # 回傳為None 或 資料不足導致ValueError
        pass


for i in stock_no_list:
    try:
        if BestFourPoint(Stock(i)).black_3():
           print i,'123'         #暴量收黑3天
           fileopen.write(str(index)+" "+"暴量收黑3天"+"-"+Stock_no_name[i].encode("UTF-8")+"-"+i+"-"+"成交張數"+"-"+str(int(Stock(i).raw[-1][1]/1000))+"\n")
           index = index + 1
    except:     # 回傳為None 或 資料不足導致ValueError
        pass

for i in stock_no_list:
    try:
        if BestFourPoint(Stock(i)).black_4():
           print i,'123'         #暴量收黑4天
           fileopen.write(str(index)+" "+"暴量收黑4天"+"-"+Stock_no_name[i].encode("UTF-8")+"-"+i+"-"+"成交張數"+"-"+str(int(Stock(i).raw[-1][1]/1000))+"\n")
           index = index + 1
    except:     # 回傳為None 或 資料不足導致ValueError
        pass

for i in stock_no_list:
    try:
        if BestFourPoint(Stock(i)).black_5():
           print i,'123'         #暴量收黑5天
           fileopen.write(str(index)+" "+"暴量收黑5天"+"-"+Stock_no_name[i].encode("UTF-8")+"-"+i+"-"+"成交張數"+"-"+str(int(Stock(i).raw[-1][1]/1000))+"\n")
           index = index + 1
    except:     # 回傳為None 或 資料不足導致ValueError
        pass






fileopen.write('\n\n\n上櫃公司股票篩選\n\n\n')

for i in OTC_no_list:
    try:
        if BestFourPoint(Stock(i)).black_3():
           print i,'123'         #暴量收黑3天
           fileopen.write(str(index)+" "+"暴量收黑3天"+"-"+OTC_no_name[i].encode("UTF-8")+"-"+i+"-"+"成交張數"+"-"+str(int(Stock(i).raw[-1][1]/1000))+"\n")
           index = index + 1
    except:     # 回傳為None 或 資料不足導致ValueError
        pass



"""
j = 1
for i in stock_no_list:
    #print i, '上市', Stock_no_name[i]
    try:
        best_point, info = BestFourPoint(Stock(i)).best_four_point()
        if best_point:           # 買點
           ## fileopen.write(str(j)+' '+'Buy'+' '+i+' ('+Stock_no_name[i].encode("UTF-8")+')'\
           ### +'  成交張數(含零股)  '+ str(Stock(i).raw[-1][1]/1000) +                 '\n')

           ## txt = "%-2d Buy%6s%10s 成交張數(包含零股):%9.1f \n"%(j,i,Stock_no_name[i].encode("UTF-8"),Stock(i).raw[-1][1]/1000)
           ## fileopen.write(txt)
            fileopen.write(str(j)+' '+'Buy'+' '+i+' ('+Stock_no_name[i].encode("UTF-8")+')'+'\n')
            fileopen.write('  成交張數:'+str(int(Stock(i).raw[-1][1]/1000))+'\n')
            fileopen.write('  '+info.encode("UTF-8"))
            fileopen.write('\n\n')
            fileopen.write('----------------------------------\n')
            j+=1
    except:     # 不作為或資料不足
        pass
"""
        
"""
j = 1
for i in stock_no_list:
    try:
        best_point, info = BestFourPoint(Stock(i)).best_four_point()
        # 要執行這段程式 best_buy_or_sell.py下的best_four_point 要改成 return None ,None
    except ValueError: #印出三個月內有資料不足的股票,可能當日都沒交易傳回 - 字串
        print 'ValueError',i 
        # 顯示ValueError表示該各股兩個月內有其中一天沒交易量,所以抓到字串" - "
    else:
	pass
"""



"""
fileopen.write("\n"+"傳統黃金交叉定義:昨天短均線低於長均線,今天短均線高於長均線"+"\n\n")

#傳統黃金交叉(5日均線向上穿越20日均線)
index = 1
for i in stock_no_list:
    try: 
        if BestFourPoint(Stock(i)).golden_cross_no_back_test(m=5,n=20):
           fileopen.write(str(index)+" "+"傳統黃金交叉(5日均線向上穿越20日均線)"+"-"+Stock_no_name[i].encode("UTF-8")+"-"+i+"-"+"成交張數"+"-"+str(int(Stock(i).raw[-1][1]/1000))+"\n")
           index = index + 1
    except:     # 回傳為None 或 資料不足導致ValueError
        pass
"""




"""
j =1
for i in stock_no_list:
        try:
                golden_cross_true_or_false = BestFourPoint(Stock(i)).golden_cross() #判斷黃金交叉
                # 今天以前的五天內五日均線小於20日均線,但是今天5日均線高於20日均線,故今天為黃金交叉
                if golden_cross_true_or_false:
                        print i
                        fileopen.write(str(j)+' '+'黃金交叉-Buy'+' '+i+' ('+Stock_no_name[i].encode("UTF-8")+')'+'\n')
        except:
                pass
"""



 
fileopen.write('\n\n\n上櫃公司股票篩選\n\n\n')

"""
j = 1
for i in OTC_no_list:
    #print i,'上櫃', OTC_no_name[i]
    try:
        best_point, info = BestFourPoint(Stock(i)).best_four_point()

        if best_point:           # 買點
            #fileopen.write(str(j)+' '+'Buy'+' '+i+' ('+OTC_no_name[i].encode("UTF-8")+')'\
            #+'  成交張數  '+ str(Stock(i).raw[-1][1]) +                 '\n')


            txt = "%-2d Buy%6s%10s 成交張數:%-9d \n"%(j,i,OTC_no_name[i].encode("UTF-8"),Stock(i).raw[-1][1])
            fileopen.write(txt)


            fileopen.write(info.encode("UTF-8"))
            fileopen.write('\n\n')
            fileopen.write('----------------------------------\n')
            j+=1
    except:     # 不作為或資料不足
        pass
"""   
fileopen.close()                #關閉檔案


"""
os.system('sendEmail -o \
 -f u160895@taipower.com.tw \
 -t "WEI <weihautin@gmail.com>" u160895@taipower.com.tw \
 -s smtp.gmail.com:587 \
 -xu %s \
 -xp %s \
 -u %s \
 -m %s \
 -a %s \
 '%(ID, PW, title, content, attachment))
"""

 
 
 

 
