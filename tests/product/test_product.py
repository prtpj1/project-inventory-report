from inventory_report.inventory.product import Product


def test_cria_produto():
    product_mock = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1",
    )

    assert type(product_mock.id) is int and product_mock.id == 1
    assert (
        type(product_mock.nome_do_produto) is str
        and product_mock.nome_do_produto == "Nicotine Polacrilex"
    )
    assert (
        type(product_mock.nome_da_empresa) is str
        and product_mock.nome_da_empresa == "Target Corporation"
    )
    assert (
        type(product_mock.data_de_fabricacao) is str
        and product_mock.data_de_fabricacao == "2021-02-18"
    )
    assert (
        type(product_mock.data_de_validade) is str
        and product_mock.data_de_validade == "2023-09-17"
    )
    assert (
        type(product_mock.numero_de_serie) is str
        and product_mock.numero_de_serie == "CR25 1551 4467 2549 4402 1"
    )
    assert (
        type(product_mock.instrucoes_de_armazenamento) is str
        and product_mock.instrucoes_de_armazenamento == "instrucao 1"
    )
