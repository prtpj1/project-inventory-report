from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, list):
        TODAY = datetime.today().isoformat()
        oldest_date = min(product["data_de_fabricacao"] for product in list)

        closest_date = min(
            product["data_de_validade"]
            for product in list if product["data_de_validade"] >= TODAY
        )

        company = Counter(
            [company_name["nome_da_empresa"] for company_name in list]
        ).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company}"
        )
