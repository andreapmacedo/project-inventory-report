from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if "csv" in path:
            return Inventory.open_csv(path, type)
        elif "json" in path:
            return Inventory.open_json(path, type)
        elif "xml" in path:
            return Inventory.open_xml(path, type)
        else:
            raise ValueError("Arquivo inválido")

    @classmethod
    def open_csv(cls, path, type):
        with open(path, encoding="utf-8") as file:
            file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            if type == "simples":
                return SimpleReport.generate(list(file_reader))
            elif type == "completo":
                return CompleteReport.generate(list(file_reader))
            else:
                raise ValueError("Tipo inválido")

    @classmethod
    def open_json(cls, path, type):
        with open(path) as file:
            file_reader = json.load(file)
            if type == "simples":
                return SimpleReport.generate(file_reader)
            elif type == "completo":
                return CompleteReport.generate(file_reader)
            else:
                raise ValueError("Tipo inválido")

    @classmethod
    def open_xml(cls, path, type):
        with open(path) as file:
            doc = xmltodict.parse(file.read())['dataset']['record']
            if type == "simples":
                return SimpleReport.generate(doc)
            elif type == "completo":
                return CompleteReport.generate(doc)
            else:
                raise ValueError("Tipo inválido")
