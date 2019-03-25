from datetime import datetime  
year = int(input("輸入年分："))  
  
#判斷是不是閏年 能被4整除但是不能被100整除的年份  或者   能直接被400整除的。  
  
if((year %4 == 0 and year %100 != 0) or (year % 400 == 0)):   
    leap_year = True  
else:  
    leap_year = False   
      
i = 1900   #因為1900年的1月1號在禮拜一
sum = 0  
while i < year - 1:  
    i += 1  
    if((i % 4 == 0 and i % 100 != 0) or (i % 400 == 0)):  
        sum += 366 # 是閏年就加366  
    else:   
        sum += 365 # 不是閏年加365  
print("目前總年的天數",sum)     
  
# ------------------------------------------  
          
month = int(input("輸入月份："))  
  
j=1  
while j < month:  
    # 判斷大月跟小月  
    if((j == 1) or (j == 3) or (j == 5) or (j == 7) or (j == 8) or (j == 10) or (j == 12)):  
        sum += 31  
    elif j == 2: # 判斷是否為閏年的2月  
        if leap_year:  
            sum += 29  
        else:   
            sum += 28  
    else: sum += 30  
    j += 1  
print("目前總天數",sum)       
  
# ------------------------------------------  
#通常每過一年 同一日期的星期幾會往後推一天  
week = (sum + 1) % 7   #求出該月份1日星期幾(因為從星期日計算故+1) 空幾格 [一,二,三,四,五,六,日]>[1,2,3,4,5,6,7]
if ((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)):  
    day = 31  
elif month == 2:  
    #閏年的2月 29天 平年就28天  
    if leap_year:  
        day = 29  
    else:  
        day = 28  
else:  
    day = 30  
  
print("求出該月份1日星期幾[日,一,二,三,四,五,六]>[0,1,2,3,4,5,6]",week)    
      
# ------------------------------------------  
  
print("日\t一\t二\t三\t四\t五\t六")  
print("==================================================") 
count = 0   # 打空格  
k = 0   
while k <= week:   #每個月開始前面的空格數  
    k += 1  
    print("\t",end="") # end=' '意思是末尾不換行，加空格。  
    count += 1  
    if (count % 7 == 0):print("\n")  
   # 7格就換行  
p = 1  
while p <= day:    #顯示天數  
    print(p,"\t",end="")       
    p += 1  
    count += 1  
    if(count % 7 == 0):print("\n")        #逢7換行  