from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()


circuit = Circuit('Test')

circuit.raw_spice = '''
V1 +5V 0 5
L1 Vc1 Vin 18m
C1 Vc1 N006 100n
C2 Vc2 N006 10n
R1 Vc2 Vc1 1.5k
R4 N002 Vc2 10k
R5 N002 N004 10k
R6 N004 N006 3.3k
XU1 Vc2 N004 +5V -5V N002 LM741/NS
V3 -5V 0 -5
R2 N003 Vc2 100k
R3 N003 N005 100k
R7 N005 N006 2.2k
XU2 Vc2 N005 +5V -5V N003 LM741/NS
XU3 Vc2 N001 +5V -5V Vout LM741/NS
L2 Vout N001 10m
V4 Vin N006 SINE(0 1 1k 0 0 0 500)
.tran 100m
.include 74hc.lib
.include dview.lib
.include LM741.MOD
.backanno
.end
'''

circuit.V('input', 1, circuit.gnd, 10@u_V)

simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.operating_point()

for node in analysis.nodes.values():
    print('Node {}: {:4.1f} V'.format(str(node), float(node))) # Fixme: format value + unit
#o#