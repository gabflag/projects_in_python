import my_card
import pytest

# NOTA GERAL, VOCÊ PODE ESCOLHER QUAL TESTE EXECUTAR COM O COMANDO pytest test_my_card.py -k 'método_a_ser_testado'

class Test_mycard:

    @pytest.fixture
    def b(self):
        return my_card.Meu_cartão_vazou

    @pytest.mark.parametrize("entrada, valor_esperado", [
        ('1548.,56', 154856),
        ('2.28368', 228368),      
        ('+3+56-9.', 3569),
        ('-356-9.', 3569),])

    def test_trata_numero(self, entrada, valor_esperado, b):
        assert b.trata_numero(self, entrada) == valor_esperado


    @pytest.mark.parametrize("entrada_digitos, valor_digitos_esperado", [
    (4, 4),
    (16, 16),      
    (36, 36),
    ])

    def test_cria_num_cartões(self, entrada_digitos, valor_digitos_esperado, b):
        assert len(str(b.cria_num_cartões(self, entrada_digitos))) == valor_digitos_esperado
    
    @pytest.mark.parametrize('entrada_qnt, qnt_esperada', [
        (3, 3),
        (5, 5),
        (7, 7)
        ])
    def test_cria_lista_int(self, entrada_qnt, qnt_esperada, b):
        assert len(b.cria_lista_int(b, entrada_qnt)) == qnt_esperada
