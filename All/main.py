from Classes import Cliente, Ave, Caneca, Copo, Barraquinha, Moto, Motoatt, Relogio, Relogioatt, Cronograma, Celular

def verificar_metodo():
    tabela()
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
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
            galinha=Ave("Galinha","Sim","5 kg")
            bemteve=Ave("Bem-te-vi","Não","2 kg")

            galinha.voar()
            bemteve.voar()

        case "3":
            Caneca.Calcular_volume()
            canecaAmericana=Caneca(0.25,0.2,0.3,"vrido","americano")

            print(canecaAmericana.altura)
            canecaAmericana.altura=0.4
            print("Novo valor da altura...")
            print(canecaAmericana.altura)

        case "4":
            Copo.Calcular_volume()

            copoAmericano=Copo(0.25,0.2,0.3,"vidro","americano")

            print(copoAmericano.altura)
            copoAmericano.altura=0.4
            print("Novo valor da altura...")
            print(copoAmericano.altura)

        case "5":
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

        case "6":
            moto1 = Moto("Suzuki", "V-Strom 650", "Preto")
            moto2 = Moto("Honda", "CBR 1000RR", "Vermelho")

            moto1.acelerar(20)
            moto2.acelerar(30)

        case "7":
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

        case "8":
            r=Relogio(60,60,24,30,"Janeiro",2024)

            r.verificar_metodo_relogio()

        case "9":
            r=Relogioatt(60,60,24,30,"Janeiro",2024)

            r.all_f()

        case "10":
            c=Cronograma()
            c.opcs()

        case "11":
            c1=Celular()
            c1.especificacoes()

        case _:
            print("Metodo errado tente novamente:")
            verificar_metodo()

def tabela():
    print("|=========================|")
    print("|         Metodos         |")
    print("|1. Cliente               |")
    print("|2. Ave                   |")
    print("|3. Caneca                |")
    print("|4. Copo                  |")
    print("|5. Barraquinha           |")
    print("|6. Moto                  |")
    print("|7. Motoatt               |")
    print("|8. Relogio               |")
    print("|9. Relogioatt            |")
    print("|10. Cronograma           |")
    print("|11. Celular              |")
    print("|=========================|")

verificar_metodo()
