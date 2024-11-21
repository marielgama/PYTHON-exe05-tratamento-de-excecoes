

#criando exçecoes
class ErroPersonalizado(Exception):
    def __init__(self, mensagem, codigo_erro):
        super().__init__(mensagem)
        self.codigo_erro = codigo_erro

    def __str__(self):
        return f"[Erro {self.codigo_erro}]: {self.args[0]}"

def funcao_que_lanca_excecao(valor):
    if valor < 0:
        raise ErroPersonalizado("O valor nao pode ser negativo!", 400)
    else:
        return f"O valor eh {valor}"

try:
    resultado = funcao_que_lanca_excecao(-10)
    print(resultado)
except ErroPersonalizado as e:
    print(e)



