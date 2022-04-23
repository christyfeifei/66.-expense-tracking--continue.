# 讀取、分割資料
products = []
with open('64. products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入商品價格:')
    price = int(price)
    products.append([name, price])
print(products)

for p in products:
    print(p)
    print(p[0], '的價格是', p[1])

with open('64. products.csv', 'w', encoding='utf-8') as f:
    f.write('商品名稱,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
