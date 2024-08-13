
import os
from pickle import TRUE

print('ADVINHE A PALAVRA SECRETA')
print('#' * 20 )

palavra_secreta = 'corinthians'
palavra_acertada = ''
tentativa = 0

while TRUE:
    letra_digita = input ('DIGITE APENAS UMA LETRA:')
    tentativa += 1

    if len(letra_digita) > 1:
        print('DIGITE APENAS 1 LETRA')
        continue

    if letra_digita in palavra_secreta:
        palavra_acertada += letra_digita

        palavra_formada = ''
        
        for letra_secreta in palavra_secreta:
            if letra_acertada in letra_secreta:
              palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            print("palavra formada", palavra_formada)

            if palavra_formada == palavra_secreta:
                os.system('cls')
                print('PARABENS,VOCÊ ACERTOU!!!')
                print(f'A palavra secreta era (palavra_secreta)')
                print(f'voce teve {tentativa} tentativa')
                letra_acertada = ''
                tentativa = 0
           
             


