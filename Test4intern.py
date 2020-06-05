import numpy as np
## 題目1.-------------------------------------
def flipAllwords(name):
    origin = name
    name = name[::-1]
    print(origin + ' == ' + name)

def flipwords(name):
    name = name[::-1]
    name = name.split(' ')
    name = name[::-1]
    print(name)

name = input('PLz type in some words: ')
flipAllwords(name)
flipwords(name)

# for str_name in name:
#     name_new = name_new + name
# print(name_new)

## 題目2.---------------------------------------
i = 0
array = [0]

num = eval(input('input: '))
for i in range(num):
    flag1 = 0
    flag2 = 0
    array[i] = array[i].insert(i, i)

    if array[i] % 3 == 0 or array[i] % 5 == 0:
        flag1 = 1
    if array[i] % 3 == 0 and array[i] % 5 == 0:
        flag2 = 1    
    if flag1 != 0 and flag2 != 0:
        array = array.pop[i]
    
print(array)

# 3. ---------------------------------------------------
一開始先畫樹狀圖，理解說筆會在那些袋子裡出現。如果想拿"鉛筆"的話，選"原子筆"的袋子可以拿到的機率最高(2/3)
想拿"原子筆"的話，挑"鉛筆"的袋子拿機率最大(2/3)。而挑"混合袋子"，拿到"鉛筆"，"原子筆"的機率分別為(1/2)

# 4. ---------------------------------------------------
服務生已經暗槓60元，所以一開始的900 - 60 = 840，三人實際出的價格應該是840，不能把60元帶入三個人出的錢裡面算。
應該要想的是3個人是各出(750 + 90) / 3 = 280 的價格吃這一份套餐。所以可以想成是這樣(300 - 60/3) * 3 + 60 = 900
3人先受損20元, 每人其實是付了280元*3 + 被暗槓的60元 = 900元 

