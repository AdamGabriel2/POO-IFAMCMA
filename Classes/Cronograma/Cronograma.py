class Cronograma:
    def __init__(self,lista,horarios,datas,dias,semanas,meses,bimestre):
        self.lista=lista
        lista=["Escola"]
        self.horarios=horarios
        horarios=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        self.datas=datas
        datas=[]
        self.dias=dias
        dias=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.semanas=semanas
        semanas=[1,2,3,4]
        self.meses=meses
        meses=[1,2,3,4,5,6]
        self.bimestre=bimestre
        bimestre=[1,2,3,4]

    def add_lista(self):
        m_lista=input("Insira o que você quer adicionar a lista: ")
        i=0
        while(self.lista[i]!=""):
            i=+1
        else:
            print(i)

    def rm_lista(self):
        return 0

    def m_lista(self):
        return 0
