from collections import Counter
from datetime import datetime


class SimpleReport:
    @staticmethod
    def oldest(inventory: list):
        return min(product['data_de_fabricacao'] for product in inventory)

    @staticmethod
    def validation_date(inventory: list):
        return min(
            product["data_de_validade"]
            for product in inventory
            if product["data_de_validade"]
            > datetime.now().strftime("%Y-%m-%d")
        )

    @staticmethod
    def company(inventory: list):
        return Counter(
            product["nome_da_empresa"] for product in inventory
        ).most_common()[0]

    @classmethod
    def generate(cls, inventory: list):
        oldest = cls.oldest(inventory)
        validation_date = cls.validation_date(inventory)
        company, _ = cls.company(inventory)
        return (
            f'Data de fabricação mais antiga: {oldest}\n'
            f'Data de validade mais próxima: {validation_date}\n'
            f'Empresa com mais produtos: {company}'
        )
