import random
#
# #Запись в файл рандомных нулей и единиц
# with open('1.txt', "w") as f1:
#     for i in range(10000):
#         f1.write(str(random.choice([0,1])))

# #Запись в файл определенной картинки
# with open('1.txt', "w") as f1:
#     for i in range(100):
#         for j in range(100):
#             if j in range(45,56):
#                 f1.write(str(1))
#             else:
#                 f1.write(str(0))

with open('Klyuchnikov_D_S_BVT-191/Crypto/LR2/1.txt', "w") as f1:
    st = 0
    for i in range(100):
        if st == 0:
            st = 1
        else:
            st = 0
        for j in range(100):
            if j % 10 == 0:
                if st == 0:
                    st = 1
                else:
                    st = 0
            f1.write(str(st))