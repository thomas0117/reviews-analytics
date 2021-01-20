data = []
sum_len = 0 
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		sum_len += len(line)

avg = sum_len/len(data)

print('檔案讀取完了,總共有', len(data),'筆資料')
print('平均每筆留言長度為:', avg)
