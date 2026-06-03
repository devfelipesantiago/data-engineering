# %% [markdown]
# ## 1. Introdução à Programação Orientada a Objetos (POO)
# 
# A POO é um paradigma de programação que organiza o código em torno de "objetos", que podem conter tanto dados (atributos) quanto ações (métodos). Pense em um objeto como uma representação de algo do mundo real, como um carro, uma pessoa ou uma conta bancária. Isso ajuda a estruturar programas complexos de forma mais lógica e reutilizável.
# 
# Praticamente todos os algoritmos de Machine Learning e IA são criados com POO. Quase todas as bibliotecas usadas em tarefas de Ciência de Dados (Análise de Dados, Análise Estatística, Engenharia de Dados) são criadas usando POO.

# %% [markdown]
# ## 2. Classes e Objetos - Abstraindo Entidades do Mundo Real
# 
# Uma Classe é como um "molde" para criar objetos. Ela define um conjunto de atributos (características) e métodos (comportamentos) que os objetos desse tipo terão.
# 
# Um Objeto é uma instância de uma classe. É a entidade real, criada a partir do molde (classe), com a qual você interage em seu programa.

# %%
# Definindo a Classe (o molde)
class Carro:
    
    # O método __init__ é um "construtor". Ele é chamado quando um novo objeto é criado.
    # 'self' se refere à instância do objeto que está sendo criado.
    def __init__(self, marca, modelo, ano):
        
        # Atributos (dados) do objeto
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False # Um carro começa desligado por padrão

    # Métodos (comportamentos) do objeto
    def ligar(self):
        
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} está ligado.")
        else:
            print(f"O {self.modelo} já estava ligado.")

    def desligar(self):
        
        if self.ligado:
            self.ligado = False
            print(f"O {self.modelo} foi desligado.")
        else:
            print(f"O {self.modelo} já estava desligado.")

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

# %%
# Criando objeto (instância da classe Carro)
carro_1 = Carro("Volkswagen", "Fusca", 1967)

# %%
# Usando os objetos
carro_1.exibir_informacoes()

# %%
carro_1.ligar()

# %%
carro_1.desligar()

# %%
# Criando objeto (instância da classe Carro)
carro_2 = Carro("Tesla", "Model S", 2025)

# %%
carro_2.exibir_informacoes()

# %%
carro_2.ligar()

# %% [markdown]
# ## 3. Fundamentos de POO - Encapsulamento
# 
# O encapsulamento é a ideia de agrupar os dados (atributos) e os métodos que operam nesses dados dentro de uma única unidade (a classe). Ele também envolve restringir o acesso direto aos atributos, geralmente usando um _ (protegido) ou __ (privado) no início do nome do atributo. O acesso é feito através de métodos (getters e setters), o que dá mais controle sobre como os dados são modificados.
# 
# Vamos modificar a classe Carro para encapsular velocidade e horsepower.

# %%
# Define a classe
class Carro:

    # Método construtor
    def __init__(self, marca, modelo, ano):

        # Inicializa os atributos
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self._velocidade = 0      # Atributo protegido, não deve ser acessado diretamente
        self.__horsepower = 300   # Atributo privado (name mangling), não deve ser acessado diretamente

    # Método "getter" para obter o valor da velocidade
    def get_velocidade(self):
        return self._velocidade

    # Método "setter" para alterar o valor da velocidade com lógica de controle
    def acelerar(self, valor):
        if valor > 0:
            self._velocidade += valor
            print(f"O {self.modelo} acelerou para {self._velocidade} km/h.")
        else:
            print("O valor de aceleração deve ser positivo.")

    # Método geral
    def frear(self, valor):
        if valor > 0:
            self._velocidade -= valor
            if self._velocidade < 0:
                self._velocidade = 0
            print(f"O {self.modelo} freou para {self._velocidade} km/h.")
        else:
            print("O valor de frenagem deve ser positivo.")

# %%
# Cria a instância da classe
carro_encapsulado = Carro("Hyundai", "HB20", 2026)

# %%
# Observe que o atributo _velocidade não aparece na lista
carro_encapsulado.ano

# %%
# Interagindo com o objeto através de métodos
carro_encapsulado.acelerar(50)
print(f"Velocidade atual: {carro_encapsulado.get_velocidade()} km/h")
carro_encapsulado.frear(20)
print(f"Velocidade atual: {carro_encapsulado.get_velocidade()} km/h")

# %%
# Conseguimos acessar diretamente o atributo protegido
print(carro_encapsulado._velocidade)

# %%
# Acesso direto (não recomendado)
carro_encapsulado._velocidade = 200 # Isso quebra o encapsulamento!
print(f"Velocidade alterada diretamente: {carro_encapsulado._velocidade} km/h")

# %% [markdown]
# **ATENÇÃO**: A célula acima funciona porque, em Python, o uso de um único sublinhado no início de um atributo (como _velocidade) é apenas uma convenção de programação, não uma regra imposta pela linguagem. Ou seja, o sublinhado indica para outros desenvolvedores que aquele atributo é considerado "protegido" e não deve ser acessado diretamente fora da classe, mas o interpretador Python não impede que você o modifique. Python aceita normalmente, sobrescrevendo o valor interno do atributo, mesmo que isso quebre a lógica de encapsulamento. Diferente de linguagens como Java ou C++, onde o modificador private de fato impede o acesso externo, em Python a proteção é baseada em boas práticas e disciplina do programador.
# 
# Se a intenção fosse dificultar ainda mais o acesso direto, poderia ser usado duplo sublinhado (__horsepower), que aciona um processo chamado name mangling. Isso não torna o atributo verdadeiramente privado, mas altera o nome interno e dificulta acessá-lo acidentalmente, embora ainda seja possível com alguma insistência.

# %%
# Tentativa de acesso direto falha
try:
    print(carro_encapsulado.__horsepower)
except AttributeError as e:
    print("Erro ao acessar diretamente:", e)

# %%
# Mas o atributo existe, só que com nome interno modificado
print("Acessando pelo nome real interno:", carro_encapsulado._Carro__horsepower)

# %%
# Acesso direto (não recomendado)
carro_encapsulado.__horsepower = 350   # Isso quebra o encapsulamento!
print(f"Horsepower alterado diretamente: {carro_encapsulado.__horsepower}")

# %% [markdown]
# Resumindo
# 
# - _atributo → apenas convenção, acesso é permitido.
# 
# - __atributo → Python aplica name mangling, mudando o nome interno do atributo para _NomeDaClasse__atributo. Isso dificulta o acesso, mas ainda é possível se você souber o nome interno.
# 
# Ou seja, em Python o encapsulamento é mais cultural do que técnico.

# %% [markdown]
# ## 4. Fundamentos de POO - Herança
# <!-- Trabalho Desenvolvido no Curso da Data Science Academy - www.datascienceacademy.com.br -->
# A herança permite que uma nova classe (chamada de classe filha ou subclasse) herde atributos e métodos de uma classe existente (chamada de classe pai ou superclasse). Isso promove a reutilização de código.
# 
# Vamos criar uma classe Veiculo genérica e fazer Carro e Moto herdarem dela.

# %%
# Classe Pai (Superclasse)
class Veiculo:

    # Método construtor da classe pai
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O {self.modelo} foi ligado.")

    def desligar(self):
        self.ligado = False
        print(f"O {self.modelo} foi desligado.")

# Classe Filha (Subclasse) que herda de Veiculo
class Carro(Veiculo):

    # Método construtor da classe filha
    def __init__(self, marca, modelo, portas):
        # super().__init__() chama o construtor da classe pai
        super().__init__(marca, modelo)
        self.portas = portas

    def exibir_info_carro(self):
        print(f"Carro: {self.marca} {self.modelo}, Portas: {self.portas}")

# Outra Classe Filha
class Moto(Veiculo):

    # Método construtor da classe filha
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    # Este método é específico da classe Moto
    def empinar(self):
        print(f"A moto {self.modelo} está empinando! Cuidado!")

# %%
meu_carro = Carro("Volkswagen", "Golf", 4)

# %%
minha_moto = Moto("Honda", "CB 500", 500)

# %%
meu_carro.exibir_info_carro()

# %%
meu_carro.ligar() # Método herdado de Veiculo

# %%
minha_moto.ligar() # Método herdado de Veiculo
minha_moto.empinar() # Método específico de Moto

# %% [markdown]
# ## 5. Fundamentos de POO - Polimorfismo
# 
# Polimorfismo significa "muitas formas". Em POO, refere-se à capacidade de um método se comportar de maneiras diferentes para diferentes objetos. Um exemplo clássico é quando classes filhas sobrescrevem (redefinem) um método da classe pai.
# <!-- Trabalho Desenvolvido no Curso da Data Science Academy - www.datascienceacademy.com.br -->
# Vamos criar um método exibir_detalhes na classe Veiculo e sobrescrevê-lo nas classes filhas.

# %%
# Cria a Superclasse
class Veiculo:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_detalhes(self):
        print(f"Veículo genérico: {self.marca} {self.modelo}")

# Cria a Subclasse
class Carro(Veiculo):
    
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    # Sobrescrevendo o método da classe pai
    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo} | Portas: {self.portas}")

# Cria a Subclasse
class Moto(Veiculo):
    
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    # Sobrescrevendo o método da classe pai
    def exibir_detalhes(self):
        print(f"Moto: {self.marca} {self.modelo} | Cilindradas: {self.cilindradas}cc")

# %%
# Lista de veículos de diferentes tipos
veiculos = [
    Carro("Toyota", "Corolla", 4),
    Moto("Yamaha", "MT-07", 700),
    Veiculo("Caloi", "Ceci")        # Usando a classe pai diretamente
]

# %%
# O mesmo método se comporta de forma diferente para cada objeto
for v in veiculos:
    v.exibir_detalhes() # Polimorfismo em ação!

# %% [markdown]
# ## 6. Métodos Especiais (ou "Mágicos")
# 
# São métodos com nomes que começam e terminam com duplo sublinhado. Eles permitem que seus objetos se comportem como tipos nativos em Python. Os mais comuns são __init__ (construtor) e __str__ (representação em string do objeto).

# %%
# Cria a classe
class Livro:

    # Construtor
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Chamado quando usamos print() ou str() no objeto
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

    # Chamado quando usamos len() no objeto
    def __len__(self):
        return self.paginas

# %%
# Cria o objeto
livro = Livro("Deep Learning Book", "Data Camp", 100)

# %%
type(livro)

# %%
# O método __str__ é chamado aqui
print(livro)

# %%
# O método __len__ é chamado aqui
print(f"O livro tem {len(livro)} páginas.")


