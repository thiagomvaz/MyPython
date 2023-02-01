class Filme ():
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor
    def __str__(self):
        return self.titulo + ' - ' + self.diretor

    def __eq__(self, outro_filme):
        return self.titulo == outro_filme.titulo

a = Filme("A teoria de tudo", "James Marsh")
b = Filme("A teoria de tudo", "James Marsh")

print(a)
print(id(a))
print(id(b))

print(a == b)


# def pega_todos_os_filmes():
#
# meus_filmes = pega_todos_os_filmes()
# for filme in meus_filmes:
#     print(filme)