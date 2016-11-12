from  compresingMarking import CompresingMarking
class Product(object):
    id = 0
    name = ''
    marking = ''

pen = Product()
pen.id = 1
pen.name = "Pen"
pen.marking = "abbbccdddttrrr"

copybook = Product()
copybook.id = 1
copybook.name = "Retro"
copybook.marking = "aaab"

book = Product()
book.id = 1
book.name = "Harry Potter"
book.marking = "abbc"

products = []
products.append(pen.marking)
products.append(copybook.marking)
products.append(book.marking)
for i in range(len(products)):
    print(products[i])
    result = CompresingMarking.compresingMarking(products[i])
    print(result)
    print()






