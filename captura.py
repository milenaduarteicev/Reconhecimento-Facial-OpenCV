import cv2

haarcascade_path = 'haarcascade_frontalface_default.xml'

classificador = cv2.CascadeClassifier(haarcascade_path)
camera = cv2.VideoCapture(0)
amostra = 1 #controla quantas fotos ele vai tirar
numeroAmostras = 25 #número de fotos que o algoritmo vai tirar por pessoa, diversas posições
id = input("Digite seu identificador: ") #identifica a pessoa
largura, altura = 220, 220 #padronização do tamanho das imagens
print("Diga X!!!")

while (True):
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) #converter imagens em escalas de cinza
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(100,100)) #
    
    for(x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255, 2))
        if cv2.waitKey(1) & 0xFF == ord("q"): #salvar imagem
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + 1], (largura, altura))
            cv2.imwrite("fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
            print("foto" + str(amostra)+ "capturada com sucesso")
            
    cv2.imshow("Face", imagem)
    #cv2.waitKey(1)
    if(amostra >= numeroAmostras + 1):
        break
    
print("Faces capturadas com sucesso")    
    
camera.realese ()
cv2.destroyAllWindows()

