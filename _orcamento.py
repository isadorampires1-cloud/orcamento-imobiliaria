import csv

class Imovel:
    def __init__(self, tipo, quartos, garagem, crianca):
        self.tipo = tipo
        self.quartos = quartos
        self.garagem = garagem
        self.crianca = crianca
        self.valor = 0

    def calcular_valor(self):
        # Valor base
        if self.tipo == 1:
            self.valor = 700
        elif self.tipo == 2:
            self.valor = 900
        elif self.tipo == 3:
            self.valor = 1200

        # Acréscimo quartos
        if self.tipo == 1 and self.quartos == 2:
            self.valor += 200
        elif self.tipo == 2 and self.quartos == 2:
            self.valor += 250

        # Garagem
        if self.tipo in [1, 2] and self.garagem.lower() == "s":
            self.valor += 300

        # Desconto apartamento sem criança
        if self.tipo == 1 and self.crianca.lower() == "n":
            self.valor *= 0.95

        return self.valor


class Contrato:
    def __init__(self, parcelas):
        self.valor_total = 2000
        self.parcelas = parcelas

    def calcular_parcela(self):
        return self.valor_total / self.parcelas


def gerar_csv(valor_mensal):
    with open('parcelas.csv', mode='w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(['Parcela', 'Valor'])

        for i in range(1, 13):
            writer.writerow([i, valor_mensal])

    print("Arquivo parcelas.csv gerado com sucesso!")


# Execução principal
print("1 Apartamento | 2 Casa | 3 Estudio")
tipo = int(input("Escolha o tipo: "))
quartos = int(input("Quantos quartos? "))
garagem = input("Garagem s/n: ")
crianca = input("Tem criança s/n: ")
parcelas_contrato = int(input("Contrato em até 5x: "))

imovel = Imovel(tipo, quartos, garagem, crianca)
valor_mensal = imovel.calcular_valor()

contrato = Contrato(parcelas_contrato)
valor_parcela_contrato = contrato.calcular_parcela()

print("\nValor mensal do aluguel: R$", round(valor_mensal, 2))
print("Contrato total: R$", contrato.valor_total)
print("Parcelas do contrato:", parcelas_contrato, "x de R$", round(valor_parcela_contrato, 2))

gerar_csv(valor_mensal)

input("\nPressione Enter para sair...")