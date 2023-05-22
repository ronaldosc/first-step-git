# -*- coding: utf-8 -*-
"""
Created on Sun May 21 20:08:55 2023

@author: Ronaldo
"""


def realizar_divisao():
    """
    INFO
    ----
    Divide o numerador '1' pelo valor de entrada do usuário e mostra o 
    resultado a seguir.

    Returns
    -------
    None.

    """
    try:
        entrada = input("\n\t -> Digite um valor para a dividir '1' por: ")
        print()
        resultado = 1 / float(entrada)
        print('\t' * 3, "Resultado da divisão:", format(resultado).replace(".", ","), '\n')
    except ZeroDivisionError:
        print("Erro: Divisão por zero!")
    except (ValueError, TypeError):
        print("Erro: Valor inválido!")
        print("\t Tipagem do valor recebido:", type(entrada))
    except Exception as e:
        print("Erro genérico:", str(e))
    finally:
        program = "Nome do programa: Tratamento de Erros e Exceções em Python"
        print()
        print("–" * len(program))
        print(program)
        print('Desenvolvido por: Ronaldo Sc')

realizar_divisao()

