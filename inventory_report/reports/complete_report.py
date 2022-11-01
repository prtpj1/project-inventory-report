from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def companies_names(list):
        companies = [company_name["nome_da_empresa"] for company_name in list]
        return companies

    @classmethod
    def products_in_stock_counter(cls, list):
        companies = cls.companies_names(list)
        products_in_stock = "Produtos estocados por empresa:\n"
        stock = Counter(companies).most_common()

        for product in stock:
            products_in_stock += f"- {product[0]}: {product[1]}\n"
        return products_in_stock

    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)
        products_in_stock = cls.products_in_stock_counter(list)

        return f"{simple_report}\n" f"{products_in_stock}"
