frase = str(input('digite uma fase:')).upper().strip()
print ('a letra a aparece {} vezes na frase.'.format(frase.count('A')))
print ('a peimeira letra (A) aparceu na posição {}:'.format(frase.find('A')+1))
print ('a ultima letra (A) aparceu na Posição {}:'.format(frase.rfind('A')+1))