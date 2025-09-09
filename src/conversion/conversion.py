class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte temperatura de Celsius a Fahrenheit.
        """
        return (celsius * 9/5) + 32

    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte temperatura de Fahrenheit a Celsius.
        """
        return (fahrenheit - 32) * 5/9

    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.
        """
        return (metros * 3.28084)

    def pies_a_metros(self, pies):
        """
        Convierte distancia de pies a metros.
        """
        return (pies / 3.28084)

    def decimal_a_binario(self, decimal):
        """
        Convierte un número decimal a su representación binaria.
        """
        return bin(decimal)[2:]  # quitamos el prefijo '0b'

    def binario_a_decimal(self, binario):
        """
        Convierte un número binario a decimal.
        """
        return int(binario, 2)

    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.
        """
        valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        resultado = ""
        i = 0
        while numero > 0:
            if numero >= valores[i]:
                resultado += simbolos[i]
                numero -= valores[i]
            else:
                i += 1
        return resultado

    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        """
        valores = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = 0
        i = 0
        while i < len(romano):
            if i+1 < len(romano) and valores[romano[i]] < valores[romano[i+1]]:
                total += valores[romano[i+1]] - valores[romano[i]]
                i += 2
            else:
                total += valores[romano[i]]
                i += 1
        return total

    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        """
        morse_dict = {
        "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....",
        "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.",
        "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-",
        "Y":"-.--", "Z":"--..",
        "0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....",
        "6":"-....", "7":"--...", "8":"---..", "9":"----."
        }
        texto = texto.upper()
        resultado = []
        for letra in texto:
            if letra in morse_dict:
                resultado.append(morse_dict[letra])
        return " ".join(resultado)

    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        """
        morse_dict = {
        "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....",
        "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.",
        "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-",
        "Y":"-.--", "Z":"--..",
        "0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....",
        "6":"-....", "7":"--...", "8":"---..", "9":"----."
        }
        inv_morse = {v: k for k, v in morse_dict.items()}
        palabras = morse.strip().split(" ")
        resultado = ""
        for simbolo in palabras:
            if simbolo in inv_morse:
                resultado += inv_morse[simbolo]
        return resultado