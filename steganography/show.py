import cv2
import sys

def merge_byte(r, g, b, a):
    """
    Junta os 2 bits menos significativos de cada canal de um pixel em um byte só
    e o retorna
    """
    return ((r & 3) << 6) | ((g & 3) << 4) | ((b & 3) << 2) | (a & 3)

if __name__ == "__main__":
    """
    Extrai a mensagem da imagem
    """
    image = sys.argv[1]
    nome_saida = sys.argv[2] if len(sys.argv) > 2 else 'saida.txt'

    array = cv2.imread(image, cv2.IMREAD_UNCHANGED)

    height, width, channels = array.shape
    
    # j inicia em 8 para pular o cabeçalho do png
    i, j = 0, 8
    with open(nome_saida, mode="a", encoding='utf-8') as file:
        for i in range(height):
            for j in range(j, width):
                r, g, b, a = array[i][j]
                file.write(chr(merge_byte(r, g, b, a)))
            j = 0
        file.close()
