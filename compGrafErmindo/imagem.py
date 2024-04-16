import cv2 #importa a biblioteca
img = cv2.imread('lena.png') #abrir a imagem
print(img) #Mostra os pixels
#Mostra a imagem a com a função imshow
cv2.imshow("Nome da janela", img)
#Dimensoes
height = img.shape[0] #altura
width = img.shape[1] #largura
channels = img.shape[2] #numero de canais
print('Largura em pixels: {}'.format(width))
print('Altura em pixels: {}'.format(height))
print('Qtde de canais: {}'.format(channels))
px = img[0, 0] #acessando valor de pixel posicao 0 e 0 (h,w)
print('O pixel (0, 0) tem as seguintes cores:')
print(px)
(b, g, r) = img[0,0]
#Imprimindo separadamente
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)
#Acessando posição h e w e muda pra azul.
img[51, 99] = (255,0,0)
for y in range(0, height): #percorrer todos os pixels de largura
    for x in range(0, width): #percorrer todos os pixels de comprimento
        img[y, x] = (255,0,0) # mudar todos os pixels para azul
#Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", img)