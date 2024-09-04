import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('fios.png')

# Converter para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplicar um filtro para reduzir o ruído
imagem_suavizada = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)

# Detectar bordas usando o algoritmo de Canny
bordas = cv2.Canny(imagem_suavizada, 50, 150)

# Encontrar os contornos na imagem de bordas
contornos, _ = cv2.findContours(bordas, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Função para calcular a distância de um ponto a um contorno
def distancia_ponto_contorno(ponto, contorno):
    distancias = np.sqrt((contorno[:, 0, 0] - ponto[0])**2 + (contorno[:, 0, 1] - ponto[1])**2)
    return np.min(distancias)

# Polilinha indicada pelo usuário (uma lista de pontos (x, y))
polilinha_usuario = [(128, 871), (128, 768), (130, 746), (146, 690), (162, 638), (187, 553)]
# Tolerância para a distância (ajuste conforme necessário)
tolerancia = 1.1

# Filtrar contornos com base na polilinha do usuário
contornos_filtrados = []
for contorno in contornos:
    for ponto in polilinha_usuario:
        if distancia_ponto_contorno(ponto, contorno) < tolerancia:
            contornos_filtrados.append(contorno)
            break

# Desenhar os contornos filtrados na imagem original
imagem_com_contornos = imagem.copy()
imagem_com_contornos2 = imagem.copy()
cv2.drawContours(imagem_com_contornos, contornos_filtrados, -1, (255, 0, 0), 1)
cv2.drawContours(imagem_com_contornos2, contornos, -1, (0, 255, 0), 1)
cv2.drawContours(imagem_com_contornos2, pl, -1, (0, 255, 255), 3)

# Mostrar a imagem com os contornos marcados
cv2.imshow('Contornos do Cabo', imagem_com_contornos)
cv2.imshow('Contornos do Cabo2', imagem_com_contornos2)
cv2.waitKey(0)
cv2.destroyAllWindows()