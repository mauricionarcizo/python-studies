from datetime import date

def gera_nome_convite(nome):
    tamanho = len(nome)
    parte1 = nome[0:4]
    parte2 = nome[tamanho - 4: tamanho]
    return parte1 + ' ' + parte2


def envia_convite(nome_formatado):
    print 'Enviando convite para %s ' % (nome_formatado)


def processa_convite(nome):
    nome_formatado = gera_nome_convite(nome)
    envia_convite(nome_formatado)


def calcular_idade():
    ano_nascimento = raw_input()
    idade = date.today().year - int(ano_nascimento)
    print idade


def cadastrar(nomes):
    nome = raw_input()
    nomes.append(nome)


def remover(nomes):
    print 'Qual nome devera ser removido'
    nome = raw_input()
    nomes.remove(nome)