class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """
    
    def area_rectangulo(self, base, altura):
        """
        Calcula el área de un rectángulo.
        
        """
        return base*altura
    
    def perimetro_rectangulo(self, base, altura):
        """
        Calcula el perímetro de un rectángulo.
        
        """
        return (base+altura)*2
    
    def area_circulo(self, radio):
        """
        Calcula el área de un círculo.
        
        """
        return 3.1416 * (radio ** 2)
    
    def perimetro_circulo(self, radio):
        """
        Calcula el perímetro (circunferencia) de un círculo.
        """
        return 3.1416*(2*radio)
    
    def area_triangulo(self, base, altura):
        """
        Calcula el área de un triángulo.
        
        """
        return (base*altura)/2
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
        """
        Calcula el perímetro de un triángulo.
        
        """
        return lado1+lado2+lado3
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        """
        Verifica si tres longitudes pueden formar un triángulo válido.
        
        """
        if (lado1 + lado2 > lado3 and
        lado1 + lado3 > lado2 and
        lado2 + lado3 > lado1):
            return True
        else:
            return False
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        """
        Calcula el área de un trapecio.
        
        """
        return ((base_mayor + base_menor) * altura) / 2
        
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        """
        Calcula el área de un rombo usando sus diagonales.
        
        """
        return (diagonal_mayor*diagonal_menor)/2
        
    
    def area_pentagono_regular(self, lado, apotema):
        """
        Calcula el área de un pentágono regular.
        
        """
        return ((lado*5)*apotema)/2
    
    def perimetro_pentagono_regular(self, lado):
        """
        Calcula el perímetro de un pentágono regular.
        
        """
        return lado*5
    
    def area_hexagono_regular(self, lado, apotema):
        """
        Calcula el área de un hexágono regular.
        
        """
        return ((lado*6) * apotema) / 2
    
    def perimetro_hexagono_regular(self, lado):
        """
        Calcula el perímetro de un hexágono regular.
        
        """
        return lado*6
    
    def volumen_cubo(self, lado):
        """
        Calcula el volumen de un cubo.
        
        """
        return lado*lado*lado
    
    def area_superficie_cubo(self, lado):
        """
        Calcula el área de la superficie de un cubo.
        
        """
        return (lado*lado)*6
    
    def volumen_esfera(self, radio):
        """
        Calcula el volumen de una esfera.
        
        """
        return (4/3)*3.1416*(radio**3)
    
    def area_superficie_esfera(self, radio):
        """
        Calcula el área de la superficie de una esfera.
        
        """
        return 4*(radio**2)*3.1416
    
    def volumen_cilindro(self, radio, altura):
        """
        Calcula el volumen de un cilindro.
        
        """
        return 3.1416*(radio**2)*altura
    
    def area_superficie_cilindro(self, radio, altura):
        """
        Calcula el área de la superficie de un cilindro.
        
        """
        return 2*3.1416*radio*(altura+radio)
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        """
        Calcula la distancia euclidiana entre dos puntos en un plano 2D.
        
        """
        return ((x2 - x1)*2 + (y2 - y1)*2) ** 0.5
    
    def punto_medio(self, x1, y1, x2, y2):
        """
        Calcula el punto medio entre dos puntos en un plano 2D.
        
        """
        return ((x1 + x2) / 2, (y1 + y2) / 2)
    
    def pendiente_recta(self, x1, y1, x2, y2):
        """
        Calcula la pendiente de una recta que pasa por dos puntos.
       
        """
        return (y2 - y1) / (x2 - x1)
    
    

    

    def ecuacion_recta(self, x1, y1, x2, y2):
        import math 

        A = y1 - y2
        B = x2 - x1
        C = x1 * y2 - x2 * y1

        common_divisor = abs(math.gcd(A, B, C))
        A //= common_divisor
        B //= common_divisor
        C //= common_divisor

      
        if A < 0 or (A == 0 and B < 0):
            A, B, C = -A, -B, -C

        return (A, B, C)

    def area_poligono_regular(self, n, lado, apotema):
        """
      
        """
        return (n * lado * apotema) / 2

        
    def perimetro_poligono_regular(self, num_lados, lado):
        """
        Calcula el perímetro de un polígono regular.
        
        """
        return num_lados * lado