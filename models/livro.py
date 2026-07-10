class Livro:

    def __init__(
        self,
        id,
        titulo,
        autor,
        categoria,
        ano,
        isbn,
        disponivel=True
    ):

        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ano = ano
        self.isbn = isbn
        self.disponivel = disponivel