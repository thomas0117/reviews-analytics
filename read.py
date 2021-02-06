data = []
sum_len = 0 
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		sum_len += len(line)

# avg = sum_len/len(data)

print('檔案讀取完了,總共有', len(data),'筆資料')
# print('平均每筆留言長度為:', avg)

# print(data[0])

wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

# print(wc)

while True:
	word = input('請問你想查什麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過哦!')	

print('感謝使用本查詢功能')