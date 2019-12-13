from imagem import Imagem
import abc
class Personagem(Imagem,abc.ABC):
    __x = 0
    __y = 0
    __velocidade = 0
    __vida = True
    

    def __init__(self, src, posx, posy, vel):
        super().__init__(src, posx, posy,)
        self.velocidade = vel
        self.vida = True

    def movimentoDireita(self):
        self.rect.right += self.velocidade
        self.movimento()
    def movimentoEsquerda(self):
        self.rect.left -= self.velocidade
        self.movimento()

    @abc.abstractmethod
    def movimento(self):
        pass

    def setVida(self, vida):
        self.vida = vida



