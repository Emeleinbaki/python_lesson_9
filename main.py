# a = 1000
# years = 5
# for i in range(1, years+1):
#     q = a * 0.1 + a
#     a = q
#     print(f'{int(a)} сом')

# input('Введите вашу сумму:')
# input('На какое время выложить сумму(лет,год):')
# a = 1000
# years = 5
#
# while  (1, years+1):
#     years += a
#     q = a * 0.1 + a
#     a = q
#     print(f'{int(a)} сом')
#
print("Сумма")
a = float(input())

print("Время ?")
years = int(input())

def bank(i, years):
    a = 0
    while a <= years:
        i = i + 1
        return i

    print(bank(i, years))
    print(f'{int(i)}сом')
