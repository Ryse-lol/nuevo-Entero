class GCDCalculator:
    def MCD(self, a, b):
        x = abs(a)
        y = abs(b)

        while y != 0:
            remainder = x % y
            x = y
            y = remainder

        return x


if __name__ == '__main__':
    operacion = numeroEntero()
    print(f"MCD de {5} {10} es {operacion.MDC(5, 10)}")