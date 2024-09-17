# Classes Normais
from Classes import Ave, Cachorro # Animais
from Classes import Calendario, Cronograma # Datas/Gerenciamento
from Classes import Cliente, Barraquinha, Produto, Loja # Estabelecimentos
from Classes import Caneca, Copo, Taca, Jarra # Recipientes
from Classes import Celular, Relogio, Relogioatt # Objetos
from Classes import Aviao, Carro, Moto, Motoatt # Veiculos

# Classes Abstratas
from Classes import VIP # Ex 1
from Classes import Retangulo, Triangulo # Ex 2
from Classes import TriAtleta # Ex 3
from Classes import ContaCorrente, Poupanca, ContaImposto # Ex4

# Interfaces
from Classes import Menu # Ex 1
from Classes import InfoClientePessoaFisica, InfoClientePessoaJuridica, ClienteFidelizacao # Ex 2

# Relacionamentos
from Classes import Farol, MotoR, Pedido # Ex 1
from Classes import ItemPedido # Ex 2
# Lista de Exercícios/Ex 3
from Classes import DVDPLAYER, DVDMIDIA # Ex 1
from Classes import Pessoa, Musico, Engenheiro # Ex 2
from Classes import Baterista, Saxofonista, Musico2, Orquestra # Ex 3
from Classes import Baterista2, Saxofonista2, Musico3, Orquestra2 # Ex 4
from Classes import Aluno, Curso # Ex 5
from Classes import Casa, TabuleiroDeXadrez # Ex 6
from Classes import C1, C2, PropriedadesDaRelacao # Ex 7
from Classes import School, Department, Student, Course, Instructor # Ex 8
from Classes import Carro2 # Ex 4 
from Classes import Mestre, Sensor, Conexao, Astromech # Ex 5

def verificar_classes():
    print("|=========================|")
    print("|         Classes         |")
    print("|1. Classes Normais       |")
    print("|2. Classes Abstratas     |")
    print("|3. Interfaces            |")
    print("|4. Relacionamentos       |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o tipo de Exercícios de Classes que voce quer usar: ")
    print(f"O tipo de Exercícios de Classes que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            print("Fim do Programa.")
            exit

        case "1":
            cn()

        case "2":
            ca()
            
        case "3":
            inter()
            
        case "4":
            rela()

        case _:
            print("Tipo de Exercícios de Classes errado tente novamente:")
            verificar_classes()

def cn():
    print("|=========================|")
    print("|         Metodos         |")
    print("|1. Animais               |")
    print("|2. Datas/Gerenciamento   |")
    print("|3. Estabelecimentos      |")
    print("|4. Recipientes           |")
    print("|5. Objetos               |")
    print("|6. Veiculos              |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            verificar_classes()

        case "1":
            animais()

        case "2":
            datas_gerenciamento()

        case "3":
            estabelecimentos()

        case "4":
            recipientes()
            
        case "5":
            objetos()

        case "6":
            veiculos()

        case _:
            print("Metodo errado tente novamente:")
            cn()

def animais():
    print("|=========================|")
    print("|         Animais         |")
    print("|1. Ave                   |")
    print("|2. Cachorro              |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            cn()

        case "1":
            galinha=Ave("Galinha","Sim","5 kg")
            bemteve=Ave("Bem-te-vi","Não","2 kg")

            galinha.voar()
            bemteve.voar()
                
        case "2":
            Doberman=Cachorro("Dob","Doberman",15,"Preto e Branco",20,16,"Macho","Nome")

            print(f"Nome: {Doberman.nome}")
            print(f"Raça: {Doberman.raca}")
            print(f"Idade: {Doberman.idade}")
            print(f"Cor: {Doberman.cor}")
            print(f"Altura: {Doberman.altura}cm")
            print(f"Peso: {Doberman.peso}kg")
            print(f"Gênero: {Doberman.genero}")
            print(f"Nome do Dono: {Doberman.dono}")

            Doberman.latir()
            Doberman.andar()
            Doberman.comer()
            Doberman.brincar()
            Doberman.fazer_truques()
            Doberman.receber_carinho()
            Doberman.definir_dono("Novo Nome")
            print(f"Nome do Dono: {Doberman.dono}")

        case _:
            print("Metodo errado tente novamente:")
            animais()

def datas_gerenciamento():
    print("|=========================|")
    print("|  Datas e Gerenciamento  |")
    print("|1. Calendario            |")
    print("|2. Cronograma            |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            cn()

        case "1":
            cal = Calendario(2024,None,None,1)

            cal.add_evento(1,"Teste1")
            cal.add_evento(2,"Teste2")
            cal.rm_evento(1, "Teste1")

            cal.visu_eventos(2)
            cal.visu_mes("Janeiro")
            cal.visu_ano()

            cal.verif_feriado(2)

            cal.proximo_dia(2024, "Fevereiro", 28)

            cal.mostrar_meses_por_periodo("bimestre")
            cal.mostrar_meses_por_periodo("trimestre")
            cal.mostrar_meses_por_periodo("semestre")

            cal.mostrar_calendario_xml()
                
        case "2":
            c=Cronograma()
            c.opcs()

        case _:
            print("Metodo errado tente novamente:")
            datas_gerenciamento()

def estabelecimentos():
    print("|=========================|")
    print("|     Estabelecimentos    |")
    print("|1. Cliente               |")
    print("|2. Barraquinha           |")
    print("|3. Loja                  |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            cn()

        case "1":
            joao=Cliente("Joao da Silva",23632,"06/06/1995","Rua A, Bairro B, Maues-AM")

            print(joao.nome)

            maria=Cliente("Maria Alburquerque", "65456", "11/11/2000", "Rua B, 2, Bairro A, Maues-AM")
            print(maria.endereco)

            print(joao.endereco)
            joao.mudar_endereco("Rua C, 3, Bairro X, Maues-AM")
            print(joao.endereco)

            maria.fazer_emprestimo('2000')
            joao.fazer_emprestimo('30')

        case "2":
            Barraquinha1=Barraquinha("Barraquinha de Maués", "Bairro: A, Rua: A, Número: A", "123456789", "barraquinha@email.com", 1.2356, 0.243657,
                                     "Carne: Temos\n"
                                     "Frango: Temos\n"
                                     "Suco: Temos\n"
                                     "Lanche: Não Temos", True, True, 40)
            Barraquinha1.info()
            Barraquinha1.funcionamento=False
            Barraquinha1.delivery=False
            Barraquinha1.taxa_delivery=0
            Barraquinha1.info()

        case "3":
            l1 = Loja("Loja de Maués", "Bairro: A, Rua: A, Número: A", "123456789", "loja@email.com", 6, 18)
            l1.info()

            produto1 = Produto("Camiseta", 20, 100)
            produto2 = Produto("Calça Jeans", 50, 50)
            l1.adicionar_produto(produto1)
            l1.adicionar_produto(produto2)

            l1.esta_aberta(10)

            l1.atualizar_estoque("Camiseta", 80)

            l1.listar_produtos()

            l1.buscar_produto("Calça Jeans")

        case _:
            print("Metodo errado tente novamente:")
            estabelecimentos()
            
def recipientes():
    print("|=========================|")
    print("|       Recipientes       |")
    print("|1. Ex da Aula            |")
    print("|2. Caneca                |")
    print("|3. Copo                  |")
    print("|4. Taça                  |")
    print("|5. Jarra                 |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            cn()

        case "1":
            print("Aqui serao testadas as classes...")
            
            copoAmericano=Copo(0.25,0.2,0.3,"vidro","americano")

            copoAmericano.Calcular_volume()

            print(copoAmericano.altura)
            copoAmericano.altura=0.4
            print("Novo valor da altura...")
            print(copoAmericano.altura)
            
        case "2":
            
            caneca = Caneca(5, 5, 10, "cerâmica", "moderno", "redonda")
            caneca.Calcular_volume()
            caneca.Encher()
            caneca.Esvaziar()
            
        case "3":

            copo = Copo(4, 4, 8, "vidro", "clássico")
            copo.Calcular_volume()
            copo.Encher()
            copo.Esvaziar()
            
        case "4":

            taca = Taca(6, 4, 12, "vidro", "elegante", "vinho")
            taca.Calcular_volume()
            taca.Encher()
            taca.Esvaziar()
            
        case "5":

            jarra = Jarra(8, 6, 15, "vidro", "moderno", "2 litros")
            jarra.Calcular_volume()
            jarra.Encher()
            jarra.Esvaziar()
            
        case _:
            print("Metodo errado tente novamente:")
            recipientes()

def objetos():
    print("|=========================|")
    print("|         Objetos         |")
    print("|1. Celular               |")
    print("|2. Relogio               |")
    print("|3. Relogioatt            |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            cn()

        case "1":
            c1=Celular()
            c1.especificacoes()

        case "2":
            r=Relogio(60,60,24,30,"Janeiro",2024)

            r.all_f()


        case "3":
            r=Relogioatt(60,60,24,30,"Janeiro",2024)

            r.all_f()

        case _:
            print("Metodo errado tente novamente:")
            objetos()

def veiculos():
    print("|=========================|")
    print("|         Veiculos        |")
    print("|1. Avião                 |")
    print("|2. Carro                 |")
    print("|3. Moto                  |")
    print("|4. Motoatt               |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            cn()

        case "1":
            aviao1 = Aviao("Emirates", "Boeing 777", 2015, "Branco", "Turbofan", "Automática", 900, 10000000, True, 100000)
            aviao1.ligar_motor()
            aviao1.decolar()
            aviao1.voar(500)
            aviao1.atualizar_quilometragem(500)
            aviao1.verificar_manutencao()
            aviao1.info()

        case "2":
            fiat_uno = Carro("Fiat", "Uno", 1984, "Preto", "Fire 1.0 Evo 8V Flex", "5 marchas, manual", "152 km/h", "R$ 9.553", "1ª geração 1984-2013", 0)
            fuscao_preto = Carro("Volkswagen", "Fusca Type 1", 1938, "Preto", "1.2L F4", "4 marchas, manual", "112 km/h", "R$ 20.000,00 a 150.000,00", "1938–2003 (total)", 0)

            fiat_uno.ligar_motor()
            fiat_uno.acelerar()
            fiat_uno.velocidade = 40
            fiat_uno.mudar_marcha()

            print(f"\nInformações do carro {fiat_uno.marca} {fiat_uno.modelo}:")
            fiat_uno.info()

            fiat_uno.distancia = 100
            fiat_uno.tempo = 2
            fiat_uno.calcular_velocidade_media()

            fiat_uno.frear()
            fiat_uno.desligar_motor()

            print(f"\nInformações do carro {fiat_uno.marca} {fiat_uno.modelo} após desligar:")
            fiat_uno.info()

            fiat_uno.pintar("Cinza")

            print("\n")
            fuscao_preto.ligar_motor()
            fuscao_preto.acelerar()
            fuscao_preto.velocidade = 70
            fuscao_preto.mudar_marcha()

            print(f"\nInformações do carro {fuscao_preto.marca} {fuscao_preto.modelo}:")
            fuscao_preto.info()

            fuscao_preto.distancia = 400
            fuscao_preto.tempo = 5
            fuscao_preto.calcular_velocidade_media()

            fuscao_preto.frear()
            fuscao_preto.desligar_motor()

            print(f"\nInformações do carro {fuscao_preto.marca} {fuscao_preto.modelo} após desligar:")
            fuscao_preto.info()

            fuscao_preto.att_preco("R$ 50.000,00 a 150.000,00")

        case "3":
            moto1 = Moto("Suzuki", "V-Strom 650", "Preto")
            moto2 = Moto("Honda", "CBR 1000RR", "Vermelho")

            moto1.acelerar(20)
            moto2.acelerar(30)

        case "4":
            moto1 = Motoatt("Suzuki", "Vermelha")
            moto2 = Motoatt("Honda", "Azul")

            moto1.ligar_motor()
            moto1.acelerar()
            moto1.velocidade = 40
            moto1.mudar_marcha()

            print("\nInformações da Moto 1:")
            moto1.info()

            moto1.distancia = 100
            moto1.tempo = 2
            moto1.calcular_velocidade_media()

            moto1.frear()
            moto1.desligar_motor()

            print("\nInformações da Moto 1 após desligar:")
            moto1.info()

            print("\n")
            moto2.ligar_motor()
            moto2.acelerar()
            moto2.velocidade = 70
            moto2.mudar_marcha()

            print("\nInformações da Moto 2:")
            moto2.info()

            moto2.distancia = 400
            moto2.tempo = 5
            moto2.calcular_velocidade_media()

            moto2.frear()
            moto2.desligar_motor()

            print("\nInformações da Moto 2 após desligar:")
            moto2.info()

        case _:
            print("Metodo errado tente novamente:")
            veiculos()

def ca():
    print("|=========================|")
    print("|  Exs Classes Abstratas  |")
    print("|1. Exercício 1           |")
    print("|2. Exercício 2           |")
    print("|3. Exercício 3           |")
    print("|4. Exercício 4           |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            verificar_classes()
            
        case "1":
            # Exercício 1
            vip1=VIP(5,10)
            vip1.imprimeValor()
    
        case "2":
            # Exercício 2
            r1=Retangulo(0, 0)
            print(r1.calculaArea(5, 10))
            print(r1.calculaPerimetro(5, 10))

            t1=Triangulo(0, 0)
            print(t1.calculaArea(2, 5))
            print(t1.calculaPerimetro(1, 2, 3))

        case "3":
            # Exercício 3
            tr1=TriAtleta(False, 40)
            tr1.aquecer()
            tr1.correr()
            tr1.nadar()
            tr1.pedalar()

        case "4":
            # Exercício 4
            c1=ContaCorrente(1)
            p1=Poupanca(2, 0.1)
            ci1=ContaImposto(3, 0.05)

            print(c1.numero)
            print(c1.saldo)
            c1.creditar(2000.0)
            print(c1.saldo)
            c1.debitar(500.0)
            print(c1.saldo)

            print(p1.numero)
            print(p1.saldo)
            p1.creditar(2000.0)
            print(p1.saldo)
            p1.debitar(500.0)
            print(p1.saldo)
            p1.renderJuros()
            print(p1.saldo)

            print(ci1.numero)
            print(ci1.saldo)
            ci1.creditar(2000.0)
            print(ci1.saldo)
            ci1.debitar(500.0)
            print(ci1.saldo)
            ci1.calculaImposto()
            print(ci1.saldo)

        case _:
            print("Metodo errado tente novamente:")
            ca()
            
def inter():
    print("|=========================|")
    print("|  Exercícios Interfaces  |")
    print("|1. Exercício 1           |")
    print("|2. Exercício 2           |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            verificar_classes()
            
        case "1":
            menu1=Menu()
            menu1.menu()
            
        case "2":
            icpf=InfoClientePessoaFisica("123456789")
            icpj=InfoClientePessoaJuridica("123456789-0000")
            cf=ClienteFidelizacao("José","Rua: A, Bairro: A, Cidade: ABCD",1000.0,"10/10/2010")

            icpf.info()
            print(" ")
            icpj.info()
            print(" ")
            cf.info()

        case _:
            print("Metodo errado tente novamente:")
            inter()
            
def rela():
    print("|================================|")
    print("|   Exercícios Relacionamentos   |")
    print("|1. Exercício 1                  |")
    print("|2. Exercício 2                  |")
    print("|3. Exercício 3                  |")
    print("|4. Exercício 4                  |")
    print("|0. Sair                         |")
    print("|================================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            verificar_classes()
            
        case "1":
            moto1=MotoR("Yamaha","Fazer")
            farolDaFrente=Farol("Xenon",40)
            farolDeTras=Farol("Xenon",40)

            #agregando
            moto1.instalaFarol(farolDaFrente)
            moto1.instalaFarol(farolDeTras)

            #associando
            moto1.farois[0].acender()
            moto1.farois[0].apagar()
            moto1.farois[1].acender()
            moto1.farois[1].apagar()
        
        case "2":
            pedido1 = Pedido()

            itempedido1 = ItemPedido(codigo=1, valor=100, descricao="Produto 1", quantidade=2)
            itempedido2 = ItemPedido(codigo=2, valor=200, descricao="Produto 2", quantidade=1)

            pedido1.add_item(itempedido1)
            pedido1.add_item(itempedido2)

            total = pedido1.obter_total()
            print(f"Total do pedido: R${total:.2f}")
        
        case "3":
            print("Lista de Exercícios: ")
            print("Exercício 1:\nNão tem saída")
            player=DVDPLAYER()
            midia=DVDMIDIA()

            player.play(midia)
            
            print("\n\nExercício 2:\nNão tem Implementação")
            
            print("\n\nExercício 3:")
            baterista=Baterista()
            saxofonista=Saxofonista()
            musico=Musico2()
            orquestra=Orquestra()

            baterista.toca_com("Saxofonista")
            saxofonista.toca_com("Baterista")

            musico.toca_em("Orquestra")
            orquestra.toca_em("Musico")
            
            print("\n\nExercício 4:")
            baterista=Baterista2()
            saxofonista1=Saxofonista2()
            saxofonista2=Saxofonista2()
            saxofonista3=Saxofonista2()
            saxofonista4=Saxofonista2()
            musico1=Musico3()
            musico2=Musico3()
            orquestra=Orquestra2()

            saxofonista1.toca_com(baterista)

            baterista.add_saxofonista(saxofonista1)
            baterista.add_saxofonista(saxofonista2)
            baterista.add_saxofonista(saxofonista3)
            baterista.add_saxofonista(saxofonista4)
            baterista.toca_com()

            musico1.toca_em(orquestra)

            orquestra.add_musico(musico1)
            orquestra.add_musico(musico2)
            orquestra.toca_em()
            
            print("\n\nExercício 5:\nNão tem saída")
            aluno=Aluno()
            curso=Curso(aluno)
            
            print("\n\nExercício 6:")
            casa=Casa()
            tabuleiro=TabuleiroDeXadrez()

            casa.contem(tabuleiro)
            tabuleiro.contem(casa)
            
            print("\n\nExercício 7:\nNão tem implementação")
            
            print("\n\nExercício 8:")
            school=School()
            department=Department()
            student=Student()
            course=Course()
            instructor=Instructor()

            department.has(school)

            student.attends(course)
            student.member(school)

            instructor.teaches(course)
            instructor.assignedTo(department)
        
        case "4":
            meuCarro=Carro2(1945,"Fiat uno","ABC1234","Branco")

            meuCarro.acelerar()
            meuCarro.frear()
            meuCarro.businar()
            
        case "5":
            novoMestre=Mestre("Luke Skywalker",100,"Alianca para Restauracao da Republica","Jedi")
            print(novoMestre.getIdade(5))
            print(novoMestre.possuiForca())
            print(novoMestre.getAnoNascimentoString())
            print(novoMestre.getDescricao())

            novoSensor=Sensor("Azul",512.0,240)
            print(novoSensor.getMPixelsPorSegundo())
            print(novoSensor.getDescricao())

            novaConexao=Conexao("SCOMP Link",1,4096000)
            print(novaConexao.getProtocoloString())
            print(novaConexao.getTaxaMBps())
            print(novaConexao.getDescricao())

            astromech1=Astromech("R2-D2",novoMestre,novoSensor,novaConexao)
            print(astromech1.getDescricao())
        
        case _:
            print("Metodo errado tente novamente:")
            rela()
            
verificar_classes()

