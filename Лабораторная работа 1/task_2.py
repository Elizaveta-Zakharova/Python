# TODO Найдите количество книг, которое можно разместить на дискете
Size = 1.44 #Мб
Pages = 100
Lines = 50
Signs = 25
Storage = 4 #байт
Size_one_book = Storage * Signs * Lines * Pages/1024/1024 #Объем в МБ одной книги
Number = round(Size//Size_one_book) #Количество одинаковых книг, помещающихся на дискете
print("Количество книг, помещающихся на дискету:", Number)
