from inventory_report.inventory.product import Product

mock = [{
    'id': 1,
    'nome_do_produto': 'Queijo do Reino',
    'nome_da_empresa': 'MR. Queijo',
    'data_de_fabricacao': '05/12/2022',
    'data_de_validade': '05/12/2025',
    'numero_de_serie': '7833123',
    'instrucoes_de_armazenamento': 'Guardar na geladeira após aberto'
}]


def test_cria_produto():
    new_product = Product(
        1,
        'Queijo do Reino',
        'MR. Queijo',
        '05/12/2022',
        '05/12/2025',
        '7833123',
        'Guardar na geladeira após aberto'
    )
    assert new_product.id == mock[0]['id']
    assert new_product.nome_do_produto == mock[0]['nome_do_produto']
    assert new_product.nome_da_empresa == mock[0]['nome_da_empresa']
    assert new_product.data_de_fabricacao == (
        mock[0]['data_de_fabricacao']
    )
    assert new_product.data_de_validade == mock[0]['data_de_validade']
    assert new_product.numero_de_serie == mock[0]['numero_de_serie']
    assert new_product.instrucoes_de_armazenamento == (
        mock[0]['instrucoes_de_armazenamento']
    )
