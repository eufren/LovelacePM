import os
ordir=os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from utils import *
from wing import *
from body import *
from control import *
from aircraft import *
from xfoil_visc import *
from aerodynamic_output import *
from toolkit import *
os.chdir(ordir)
del ordir
