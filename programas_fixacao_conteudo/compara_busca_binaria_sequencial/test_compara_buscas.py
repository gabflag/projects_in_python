import compara_busca_binaria_e_sequencial, pytest

class Testa_comparacao_de_tipos:

    '''
    Nota geral: Classe para executar testes no arquivo compara_busca_binaria_e_sequencial.
    Para fazer o teste em apenas um dos métodos da classe:

        pytest test_compara_tipos.py -k testa_busca_binaria
        or
        pytest test_compara_tipos.py -k testa_busca_sequencial
    
    Para fazer testes no arquivo todo:
        pytest test_compara_tipos.py

    '''

    @pytest.fixture
    def objeto_test(self):
        
        '''
        Cria um objeto para ser utilizado nos testes. Retorna um objeto da classe Compara_buscas.
        '''

        return compara_busca_binaria_e_sequencial.Compara_buscas()





    @pytest.mark.parametrize("lista, elemento_procurado, valor_esperado", [
        (([1,2,3,4]), 3 , 2),
        ([-3,-1,2,4], -1 , 1),
        ([1,2,3,4], 88 , -1),
    ])

    def testa_busca_binaria(self, objeto_test, lista, elemento_procurado, valor_esperado):
        assert objeto_test.busca_binaria(lista, elemento_procurado) == valor_esperado





    @pytest.mark.parametrize("lista, elemento_procurado, valor_esperado", [
        (([1,2,3,4]), 3 , 2),
        ([-3,-1,2,4], -1 , 1),
        ([1,2,3,4], 99 , -1),
    ])

    def testa_busca_sequencial(self, objeto_test, lista, elemento_procurado, valor_esperado):
        assert objeto_test.busca_sequencial(lista, elemento_procurado) == valor_esperado
        
