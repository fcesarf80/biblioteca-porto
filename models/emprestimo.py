class Emprestimo:

    def __init__(
        self,
        id,
        livro_id,
        utilizador_id,
        data_emprestimo,
        data_prevista,
        data_devolucao="",
        ativo=True
    ):

        self.id = id
        self.livro_id = livro_id
        self.utilizador_id = utilizador_id
        self.data_emprestimo = data_emprestimo
        self.data_prevista = data_prevista
        self.data_devolucao = data_devolucao
        self.ativo = ativo