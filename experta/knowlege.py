from experta import *


class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="greet")


    @Rule(
        NOT(Fact(continua=W())),
        salience=100
        )
    def ask_quer(self):
        self.declare(Fact(continua=input("Deseja classificar um animal? ")))

    @Rule(
        Fact(continua='n'),
        salience=9
        )
    def fim(self):
        print('tchau')
        exit(0)

    @Rule(
        Fact(continua='s'),
        Fact(fim='s'),
        salience=10,
        )
    def loopa(self):
        self.reset()
        self.declare(Fact(continua=input("Deseja classificar outro animal? ")))
        self.run()


    @Rule(
        NOT(Fact(fim=W())),
        salience=5,
        )
    def ask_name(self):
        self.declare(Fact(mamifero=input("Seu animal é um mamifero? ")))

    ##MAMMALIA IDENTIFIER##
    @Rule(Fact(action='greet'),
        Fact(mamifero='s'),
        NOT(Fact(fim=W())))
    def ask_location(self):
        self.declare(Fact(aquatico=input("Seu animal vive na água? ")))

    @Rule(
        Fact(aquatico='s'),
        Fact(mamifero='s'),
        NOT(Fact(fim=W()))
        )
    def eh_peixe(self):
        print("Seu animal é uma baleia!")
        self.declare(Fact(fim='s'))

    @Rule(
        Fact(mamifero='s'),
        NOT(Fact(fim=W())),
        )
    def ask_hiberna(self):
        self.declare(Fact(hiberna=input("Seu animal hiberna? ")))

    @Rule(
        Fact(mamifero='s'),
        Fact(hiberna='s'),
        NOT(Fact(fim=W())),
        )
    def is_urso(self):
        print("Seu animal é um urso!")
        self.declare(Fact(fim='s'))

    @Rule(
        Fact(mamifero='s'),
        Fact(hiberna='n'),
        Fact(aquatico='n'),
        NOT(Fact(fim=W())),
        )
    def ask_voa(self):
        self.declare(Fact(voa=input("Seu animal voa? ")))


    @Rule(
        Fact(mamifero='s'),
        Fact(hiberna='n'),
        Fact(aquatico='n'),
        NOT(Fact(fim=W())),
        Fact(voa='s')
        )
    def is_batNotMan(self):
        print("Seu animal é um Morcego!")
        self.declare(Fact(fim='s'))

    @Rule(
        Fact(mamifero='s'),
        Fact(hiberna='n'),
        Fact(aquatico='n'),
        NOT(Fact(fim=W())),
        Fact(voa='n'),
        )
    def ask_late(self):
        self.declare(Fact(late=input("Seu animal late? ")))

    @Rule(
        Fact(late='s')
        )
    def is_cachorro(self):
        print("Seu animal é um cachorro!")
        self.declare(Fact(fim='s'))

    @Rule(
        Fact(mamifero='s'),
        NOT(Fact(fim=W())),
        salience=-1,
        )
    def is_hooman(self):
        print("Seu animal é um humano!")
        self.declare(Fact(fim='s'))


    ##END OF MAMMALIA IDDENTIFIER##

    @Rule(
        NOT(Fact(fim=W())),
        )
    def is_ave(self):
        self.declare(Fact(ave=input("Seu animal é uma ave? ")))

    @Rule(
        Fact(ave='s'),
        NOT(Fact(fim=W())),
        )
    def ask_polar(self):
        self.declare(Fact(polar=input("Seu animal vive em regiões polares? ")))

    @Rule(
        Fact(ave='s'),
        Fact(polar='s'),
        NOT(Fact(fim=W())),
        )
    def is_penguim(self):
        print("Seu animal é um penguim!")
        self.declare(Fact(fim='s'))

    @Rule(
        Fact(ave='s'),
        NOT(Fact(fim=W()))
        )
    def ask_ave_rapina(self):
        self.declare(Fact(rapina=input("Seu animal é uma ave de rapina? ")))

    @Rule(
        Fact(ave='s'),
        Fact(rapina='s'),
        NOT(Fact(fim=W())),
        )
    def is_gaviao(self):
        print("Seu animal é um gavião!")
        self.declare(Fact(fim='s'))

    @Rule(
        Fact(ave='s'),
        NOT(Fact(fim=W())),
        )
    def ask_prey_fish(self):
        self.declare(Fact(come_peixe=input("Seu animal tipicamente se alimenta de peixes? ")))
    @Rule(
        Fact(ave='s'),
        Fact(come_peixe='s'),
        NOT(Fact(fim=W())),
        )
    def eh_gaiovota(self):
        print("Seu animal é uma gaiovota!")
        self.declare(Fact(fim='s'))

    @Rule(
        Fact(ave='s'),
        NOT(Fact(fim=W())),
        salience=-1
        )
    def eh_beijaflor(self):
        print("Seu animal é um beija-flor!")
        self.declare(Fact(fim='s'))

    ###fim of ave###

    @Rule(
        NOT(Fact(fim=W()))
        )
    def ask_reptil(self):
        self.declare(Fact(reptil=input("Seu animal é um reptil? ")))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(reptil='s'),
        )
    def ask_pele(self):
        self.declare(Fact(trocapele=input("Seu animal troca de pele? ")))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(reptil='s'),
        Fact(trocapele='s'),
        )
    def is_cobrah(self):
        print("Seu animal é uma cobra!")
        self.declare(Fact(fim='s'))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(reptil='s'),
        )
    def ask_cor(self):
        self.declare(Fact(muda_cor=input("Seu animal muda drasticamente de cor? ")))


    @Rule(
        NOT(Fact(fim=W())),
        Fact(reptil='s'),
        Fact(muda_cor='s'),
        )
    def is_camaleao(self):
        print("Seu animal é um camaleão!")
        self.declare(Fact(fim='s'))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(reptil='s'),
        )
    def ask_casco(self):
        self.declare(Fact(casco=input("Seu animal tem casco? ")))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(reptil='s'),
        Fact(casco='s'),
        )
    def is_tartaruga(self):
        print("Seu animal é uma tartaruga!")
        self.declare(Fact(fim='s'))

    @Rule(
        Fact(reptil='s'),
        Fact(casco='n'),
        Fact(muda_cor='n'),
        Fact(trocapele='n'),
        NOT(Fact(fim=W())),
        )
    def is_jacare(self):
        print("Seu animal é um jacaré!")
        self.declare(Fact(fim='s'))
    ###FIM REPTEIS###

    @Rule(
        NOT(Fact(fim=W())),
        Fact(mamifero='n'),
        )
    def ask_peixe(self):
        self.declare(Fact(peixe=input("Seu animal é marinho? ")))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(mamifero='n'),
        Fact(peixe='s'),
        )
    def ask_cartilaginoso(self):
        self.declare(Fact(cartilaginoso=input("Seu animal é cartilaginoso? ")))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(mamifero='n'),
        Fact(peixe='s'),
        Fact(cartilaginoso='s'),
        )
    def ask_achatado(self):
        self.declare(Fact(achatado=input("Seu animal tem o corpo achatado? ")))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(mamifero='n'),
        Fact(peixe='s'),
        Fact(cartilaginoso='s'),
        Fact(achatado='s')
        )
    def is_arraia(self):
        print("Seu animal é uma arraia!")
        self.declare(Fact(fim='s'))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(mamifero='n'),
        Fact(peixe='s'),
        Fact(cartilaginoso='s'),
        Fact(achatado='n')
        )
    def is_tutubarao(self):
        print("Seu animal é o tutubarão!")
        self.declare(Fact(fim='s'))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(mamifero='n'),
        Fact(peixe='s'),
        Fact(cartilaginoso='n'),
        )
    def ask_infla(self):
        self.declare(Fact(infla=input("Seu animal infla? ")))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(mamifero='n'),
        Fact(peixe='s'),
        Fact(cartilaginoso='n'),
        Fact(infla='s'),
        )
    def is_baiacu(self):
        print("Seu animal é o baiacu!")
        self.declare(Fact(fim='s'))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(mamifero='n'),
        Fact(peixe='s'),
        Fact(cartilaginoso='n'),
        Fact(infla='n'),
        )
    def is_atum(self):
        print("Seu animal é o Atum")
        self.declare(Fact(fim='s'))

    ### fim of peixe ###

    @Rule(NOT(Fact(fim=W())))
    def ask_anfibio(self):
        self.declare(Fact(anfibio=input("Seu animal é um anfibio? ")))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(anfibio='s'),
        )
    def ask_rabo(self):
        self.declare(Fact(rabo=input("Seu animal tem uma cauda longa? ")))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(anfibio='s'),
        Fact(rabo='s')
        )
    def eh_salamandra(self):
        print("Seu animal é uma salamandra!")
        self.declare(Fact(fim='s'))

    @Rule(
        NOT(Fact(fim=W())),
        Fact(anfibio='s'),
        Fact(rabo='n')
        )
    def eh_salamandra(self):
        print("Seu animal é um sapo!")
        self.declare(Fact(fim='s'))
engine = Greetings()
engine.reset() # Prepare the engine for the execution.
engine.run() # Run it!
