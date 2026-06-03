
# Importa o módulo inteiro
import modulo

# Usa a função e a variável do módulo
mensagem = modulo.saudacao("Mundo")
print(mensagem)
print(f"O valor de PI do nosso módulo é: {modulo.PI}")

# Outra forma: importando itens específicos
from modulo import saudacao, PI

mensagem_direta = saudacao("Felipe")
print(mensagem_direta)
print(f"Valor de PI importado diretamente: {PI}")
