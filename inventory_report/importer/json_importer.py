from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if 'json' in path:
            with open(path, mode='r') as json_file:
                return json.load(json_file)
        else:
            raise ValueError('Arquivo inválido')
