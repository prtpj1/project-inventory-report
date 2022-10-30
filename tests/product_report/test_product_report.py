from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product_mock = Product(
        1,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "CR25 1551 4467 2549 4402 1",
        "ao abrigo de luz",
    )

    assert product_mock.__repr__() == (
        f"O produto {product_mock.nome_do_produto}"
        f" fabricado em {product_mock.data_de_fabricacao}"
        f" por {product_mock.nome_da_empresa} com validade"
        f" até {product_mock.data_de_validade}"
        f" precisa ser armazenado {product_mock.instrucoes_de_armazenamento}."
    )
