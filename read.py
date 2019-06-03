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

