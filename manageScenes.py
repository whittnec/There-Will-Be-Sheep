import pygame
import levelPage
from mainPlay import mainPlay
from oilPlay import oilPlay
from oilPlayExplanation import oilPlayExplanation
from dogPlay import dogPlay
from dogPlayExplanation import dogPlayExplanation
from PISSPLAY import pissPlay
from pissPlayExplanation import pissPlayExplanation
from finaleTransition import finalTransition
from finale import final
from deathPage import death
from instructionsMain import instructionsM
from instructionsFinal import instructions
from ending import theEnd
from endingKill import endingOde
from returnHome import returning
from couponsInstructions import instructing
from coupons import couponPlay
from woodchip import woodChipper
from instructionsExtra import wInstructions

"""decided to change my main framework because this one made more sense to me;
link: https://stackoverflow.com/questions/14700889/pygame-level-menu-states"""
class SceneManager(object):
    def __init__(self):
        self.go_to(oilPlay())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self