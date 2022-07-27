n1 =float(input('Digite a primeira nota:'))
n2 =float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2
if media < 5.0:
    print(f'Sua média é {media}, você está \033[31mREPROVADO')
elif (media == 5) or (media < 7):
    print(f'Sua média é {media}, você está de \033[33mRECUPERAÇÃO')
else:
    print(f'Sua média é {media}, você está \033[32mAPROVADO')