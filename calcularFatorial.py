import time
from abc import ABC, abstractmethod

class FactorialStrategy(ABC):
    @abstractmethod
    def calculate(self, n: int) -> int:
        pass

class IterativeFactorial(FactorialStrategy):
    def calculate(self, n: int) -> int:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

class RecursiveFactorial(FactorialStrategy):
    def calculate(self, n: int) -> int:
        if n <= 1:
            return 1
        return n * self.calculate(n - 1)


class CalcularFatorial:
    _instance = None  # atributo da instância única

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalcularFatorial, cls).__new__(cls)
        return cls._instance

    def run(self):
        print("=== CALCULADORA DE FATORIAL ===")
        n = int(input("Digite um número inteiro: "))

        print("\nEscolha o método:")
        print("1 - Iterativo")
        print("2 - Recursivo")
        opc = input("Opção: ")

        if opc == '1':
            strategy = IterativeFactorial()
            metodo = "Iterativo"
        elif opc == '2':
            strategy = RecursiveFactorial()
            metodo = "Recursivo"
        else:
            print("Opção inválida!")
            return

        inicio = time.time()
        resultado = strategy.calculate(n)
        fim = time.time()

        print("\n===== RESULTADO =====")
        print(f"{n}! = {resultado}")
        print(f"Método utilizado: {metodo}")
        print(f"Tempo de execução: {fim - inicio:.6f} segundos")
        print("=====================\n")


if __name__ == "__main__":
    calc = CalcularFatorial()
    calc.run()
