data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完畢，總共有', len(data),'筆資料')

# 算留言的平均長度
#留言總長度/一百萬筆

sum_len = 0
for d in data:
    sum_len += len(d)
print('平均留言長度', sum_len / len(data)) 

#篩選出留言長度小於一百
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new),'筆留言長度小於一百')

#篩選出留言中有提到good的
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good),'筆留言提及good')
print(good[0])

#文字計數
wc = {} # word_count
for d in data:
    words = d.split(' ') #可以不輸入,因為split預設值就是空字串
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

while True:
    word = input('你想要查什麼字呢:')
    if word == 'q':
        break
    if word in wc:
        print(word, '總共出現', wc[word], '次')
    else:
        print('這個字沒有出現過唷')

print('感謝使用此查詢功能')
