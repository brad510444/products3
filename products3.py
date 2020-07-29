
#讀取檔案
products = []

with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品名稱,商品價錢' in line:
			continue
		#s = line.strip().split(',')
		#print(s)
		name, price = line.strip().split(',')
		products.append([name, price])

print(products)

while True:
	name = input('商品名稱')
	if name == 'q':
		break
	price = input('商品價錢')
	#products.append(name)
	#products.append(price)
	products.append([name, price])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品名稱,商品價錢\n')
	for line in products:
		f.write(line[0] + ',' + line[1] + '\n')#逗點在excel為區隔鍵
