from datetime import datetime
from collections import Counter


class SimpleReport:
    # @classmethod
    def oldest_date(list):
        date = min(product["data_de_fabricacao"] for product in list)
        return date

    # @classmethod
    def closest_date(list):
        TODAY = datetime.today().isoformat()
        date = min(
            product["data_de_validade"]
            for product in list
            if product["data_de_validade"] >= TODAY
        )
        return date

    # @classmethod
    def company_with_bigger_stock(list):
        company = Counter(
            [company_name["nome_da_empresa"] for company_name in list]
        ).most_common()[0][0]
        return company

    @classmethod
    def generate(cls, list):
        oldest_date = cls.oldest_date(list)
        closest_date = cls.closest_date(list)
        company = cls.company_with_bigger_stock(list)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company}"
        )
