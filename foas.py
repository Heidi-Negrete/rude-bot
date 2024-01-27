import random


class Foas:
    '''All the random fucks you'll never need.'''

    def __init__(self, fucks=[]):
        self.fucks = ["Fuckity bye!",
                      "I can't fuckin' even.",
                      "I don't give a flying fuck.",
                      "Fuck that, fuck you.",
                      "Fuck that shit.",
                      "You disingenuous dense motherfucker!",
                      "Fuck me gently with a chainsaw.",
                      "Everyone can go and fuck off.",
                      "Kindly fuck off.",
                      ] + fucks

    def give_fuck(self):
        return random.choice(self.fucks)
