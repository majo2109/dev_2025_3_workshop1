class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        """
        texto = texto.lower().replace(" ", "")
        return texto == texto[::-1]
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        """
        invertida = ""
        for c in texto:
            invertida = c + invertida
        return invertida
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        """
        vocales = "aeiouáéíóú"
        contador = 0
        for c in texto.lower():
            if c in vocales:
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        """
        vocales = "aeiouáéíóú"
        contador = 0
        for c in texto.lower():
            if c.isalpha() and c not in vocales:
                contador += 1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        """
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        """
        palabras = texto.split()
        return len(palabras)
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        """
        resultado = ""
        capitalizar = True
        for c in texto:
            if c == " ":
                resultado += c
                capitalizar = True
            else:
                if capitalizar:
                    resultado += c.upper()
                    capitalizar = False
                else:
                    resultado += c
        return resultado
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        """
        resultado = []
        prev_space = False
        for c in texto:
            if c == " ":
                if not prev_space:
                    resultado.append(c)
                prev_space = True
            else:
                resultado.append(c)
                prev_space = False
        return "".join(resultado)
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        """
        if texto.startswith("-"):
            texto = texto[1:]
        return texto.isnumeric()
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        """
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord("A") if c.isupper() else ord("a")
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        """
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        """
        if subcadena == "":
            return []
        posiciones = []
        i = texto.find(subcadena)
        while i != -1:
            posiciones.append(i)
            i = texto.find(subcadena, i + 1)
        return posiciones