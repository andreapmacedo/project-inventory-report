from inventory_report.reports.simple_report import SimpleReport
from collections import Counter
from functools import reduce


class CompleteReport(SimpleReport):

    @staticmethod
    def get_oldest_date(inventory: list):
        oldest_date = reduce(
            lambda x, y: x if x["data_de_fabricacao"]
            < y["data_de_fabricacao"] else y, inventory)
        return oldest_date["data_de_fabricacao"]

    @staticmethod
    def get_validity_date(inventory: list):
        validity_date = reduce(
            lambda x, y: x if x["data_de_validade"]
            < y["data_de_validade"] else y, inventory)
        return validity_date["data_de_validade"]

    @classmethod
    def generate(cls, inventory: list):

        oldest_date = cls.get_oldest_date(inventory)
        validity_date = cls.get_validity_date(inventory)
        componies_list = []

        for item in inventory:
            componies_list.append(item["nome_da_empresa"])

        companies_counter = Counter(componies_list)
        company_with_more_items = companies_counter.most_common()[0][0]

        products_by_companies = ""
        for empresa in Counter(componies_list).most_common():
            products_by_companies += f"- {empresa[0]}: {empresa[1]}\n"

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {validity_date}\n"
            f"Empresa com mais produtos: {company_with_more_items}\n"
            f"Produtos estocados por empresa:\n"
            f"{products_by_companies}"
        )

# https://pt.stackoverflow.com/questions/407400/calcular-quantas-vezes-se-repetem-os-valores-dentro-de-uma-key-em-dicion%C3%A1rio-p
    # data = [{
    #     "id": 1,
    #     "nome_do_produto": "MESA",
    #     "nome_da_empresa": "Forces of Nature",
    #     "data_de_fabricacao": "1999-05-04",
    #     "data_de_validade": "2023-02-10",
    #     "numero_de_serie": "FR48",
    #     "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
    #     },
    #     {
    #     "id": 2,
    #     "nome_do_produto": "MESA",
    #     "nome_da_empresa": "Newton Laboratories, Inc.",
    #     "data_de_fabricacao": "2010-04-03",
    #     "data_de_validade": "2023-02-08",
    #     "numero_de_serie": "FR48",
    #     "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
    #     },
    #     {
    #     "id": 3,
    #     "nome_do_produto": "MESA",
    #     "nome_da_empresa": "Physicians Total Care, Inc.",
    #     "data_de_fabricacao": "2019-05-04",
    #     "data_de_validade": "2023-02-09",
    #     "numero_de_serie": "FR48",
    #     "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
    #     },
    #     {
    #     "id": 3,
    #     "nome_do_produto": "MESA",
    #     "nome_da_empresa": "Physicians Total Care, Inc.",
    #     "data_de_fabricacao": "2019-05-04",
    #     "data_de_validade": "2023-02-09",
    #     "numero_de_serie": "FR48",
    #     "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
    #     },
    # ]
