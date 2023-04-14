from datetime import date  #Consegui fazer sozinha!
cont1 = 0
cont2 = 0
atual = date.today().year
for c in range(1,8):
    i = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - i
    if idade >= 18:
        cont1 += 1
    else:
        cont2 += 1
print ('No total, {} pessoas atingiram a maioridade\n{} pessoas ainda são menores de idade'.format(cont1,cont2))
    