
class Stats:
    def promedio(self, numeros):
        """ Calcula la media aritmética de una lista de números. """
        return sum(numeros) / len(numeros) if numeros else 0

    def mediana(self, numeros):
        """ Encuentra el valor mediano de una lista de números. """
        if not numeros:
            return 0
        nums = sorted(numeros)
        n = len(nums)
        mitad = n // 2
        if n % 2 == 0:
            return (nums[mitad - 1] + nums[mitad]) / 2
        else:
            return nums[mitad]

    def moda(self, numeros):
        """ Encuentra el valor más frecuente en la lista. """
        if not numeros:
            return None
        frec = {}
        for num in numeros:
            frec[num] = frec.get(num, 0) + 1
        return max(frec, key=frec.get)

    def desviacion_estandar(self, numeros):
        """ Calcula la desviación estándar poblacional. """
        if not numeros:
            return 0
        media = self.promedio(numeros)
        var = sum((x - media) ** 2 for x in numeros) / len(numeros)
        return var ** 0.5

    def varianza(self, numeros):
        """ Calcula la varianza de la lista. """
        if not numeros:
            return 0
        media = self.promedio(numeros)
        return sum((x - media) ** 2 for x in numeros) / len(numeros)

    def rango(self, numeros):
        """ Calcula el rango (max - min). """
        if not numeros:
            return 0
        return max(numeros) - min(numeros)