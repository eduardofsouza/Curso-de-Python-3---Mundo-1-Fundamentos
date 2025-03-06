preço = float(input('qual é o preço do produto? R$'))
desconto = float(input('qual é o desconto do produto?'))
preço_desconto = preço - (preço * desconto / 100)
print ('O preço atual do produto é:{:.2f} , com desconto de:{:.2f} fica:{:.2f}'.format(preço , desconto , preço_desconto))