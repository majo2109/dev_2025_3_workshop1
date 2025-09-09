class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    """
    #Ejemplo

    def fibonacci(self, n):
        """Calcula el n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
    
    def secuencia_fibonacci(self, n):
        """Genera los primeros n números de Fibonacci."""
        secuencia = []
        a, b = 0, 1
        for _ in range(n):
            secuencia.append(a)
            a, b = b, a + b
        return secuencia
    
    def es_primo(self, n):
        """Verifica si un número es primo."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        """Genera una lista de números primos hasta n."""
        return [i for i in range(2, n+1) if self.es_primo(i)]
    
    def es_numero_perfecto(self, n):
        """Verifica si un número es perfecto."""
        if n < 2:
            return False
        suma = sum(i for i in range(1, n) if n % i == 0)
        return suma == n
    
    def triangulo_pascal(self, filas):
        """Genera las primeras n filas del triángulo de Pascal."""
        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
            triangulo.append(fila)
        return triangulo
    
    def factorial(self, n):
        """Calcula el factorial de un número."""
        if n < 0:
            return None
        resultado = 1
        for i in range(1, n+1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        """Calcula el máximo común divisor de dos números."""
        while b:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        """Calcula el mínimo común múltiplo de dos números."""
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        """Calcula la suma de los dígitos de un número."""
        return sum(int(d) for d in str(n))
    
    def es_numero_armstrong(self, n):
        """Verifica si un número es de Armstrong."""
        digitos = str(n)
        potencia = len(digitos)
        suma = sum(int(d)**potencia for d in digitos)
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        """Verifica si una matriz es un cuadrado mágico."""
        n = len(matriz)
        suma_objetivo = sum(matriz[0])
        
        # Filas
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        
        # Columnas
        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_objetivo:
                return False
        
        # Diagonal principal
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
        
        # Diagonal inversa
        if sum(matriz[i][n-1-i] for i in range(n)) != suma_objetivo:
            return False
        
        return True