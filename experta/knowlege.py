from experta import *


class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="greet")

    @Rule(Fact(action='greet'),
        NOT(Fact(mamifero=W())))
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
        Fact(hiberna='n'),
        Fact(aquatico='n'),
        NOT(Fact(fim=W())),
        Fact(voa='n'),
        Fact(late='n')
        )
    def is_hooman(self):
        print("Seu animal é um humano!")
        self.declare(Fact(fim='s'))


    ##END OF MAMMALIA IDDENTIFIER##
    @Rule(Fact(action='greet'),
        Fact(name=MATCH.name),
        Fact(location=MATCH.location))
    def greet(self, name, location):
        print("Hi %s! How is the weather in %s?" % (name, location))


engine = Greetings()
engine.reset() # Prepare the engine for the execution.
engine.run() # Run it!
