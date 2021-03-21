class Retângulo: #classe que representa retângulos

    def __init__ (self, x=0, y=0):#sem essa função não é possível preencher as coordenadas
        self.x = x
        self.y = y

    def setTamanho(self, coordx, coordy): #construtor
        self.x = coordx
        self.y = coordy

    def perímetro(self): #retorna perímetro do retângulo
        return 2 * (self.x + self.y)

    def área(self): #retorna área do retângulo
        return self.x * self.y

 # >>> retângulo = Retângulo(3,4)
        # >>> retângulo.perímetro()
        # 14
        # >>> retângulo.área()
        # 12
