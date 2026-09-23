class Conteudo:
    def __init__(self, titulo):
        self.titulo = titulo

    def exibir_info(self):
        print(f"Título: {self.titulo}")

class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo)
        self.genero = genero
        self.duracao = duracao

    def exibir_info(self):
        print(f"Filme: {self.titulo} - Gênero: {self.genero} - Duração: {self.duracao}")

class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo)
        self.genero = genero
        self.temporadas = temporadas

    def exibir_info(self):
        print(f"Série: {self.titulo} - Gênero: {self.genero} - Temporadas: {self.temporadas}")

class Documentario(Conteudo):
    def __init__(self, titulo, tema, assunto):
        super().__init__(titulo)
        self.tema = tema
        self.assunto = assunto

    def exibir_info(self):
        print(f"Documentário: {self.titulo} - Tema: {self.tema} - Assunto: {self.assunto}")

catalogo = [
    Filme("Interestelar", "Ficção", 169),
    Filme("Shrek", "Animação", 90),
    Serie("Stranger Things", "Ficção", 4),
    Serie("Round 6", "Suspense", 2),
    Documentario("Nosso Planeta", "Natureza", "Vida selvagem")
]

class Podcast(Conteudo):
    def __init__(self, titulo, episodios):
        super().__init__(titulo)
        self.episodios = episodios

    def exibir_info(self):
        print(f"Podcast: {self.titulo} - Episódios: {self.episodios}")

catalogo.append(Podcast("PodPah", 100))

for item in catalogo:
    item.exibir_info()