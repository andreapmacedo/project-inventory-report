from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if 'csv' in path:
            with open(path, encoding='utf-8') as csv_file:
                return list(
                    csv.DictReader(csv_file, delimiter=',', quotechar='"')
                )
        else:
            raise ValueError('Arquivo inválido')
