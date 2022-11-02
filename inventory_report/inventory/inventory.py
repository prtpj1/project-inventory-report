from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory(CompleteReport):
    @classmethod
    def open_file(cls, path):
        if path.endswith(".csv"):
            with open(path) as file:
                data = list(csv.DictReader(file))
                return data
        elif path.endswith(".json"):
            with open(path) as file:
                data = list(json.load(file))
                return data
        elif path.endswith(".xml"):
            with open(path) as file:
                data = xmltodict.parse(file.read())["dataset"]["record"]
                return data
        else:
            raise ValueError(
                "Invalid file type. Try: 'CSV', 'JSON' or 'XML' types"
            )

    @classmethod
    def import_data(cls, path, type="simples" or "completo"):
        data = cls.open_file(path)

        if type == "simples":
            simple_report = super(CompleteReport, cls).generate(data)
            return simple_report

        if type == "completo":
            complete_report = super(Inventory, cls).generate(data)
            return complete_report
