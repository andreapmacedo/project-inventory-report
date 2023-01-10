from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if 'xml' in path:
            with open(path) as xml_file:
                return xmltodict.parse(xml_file.read())['dataset']['record']
        else:
            raise ValueError('Arquivo inválido')
