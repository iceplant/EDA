import itertools
from PyLTSpice.LTSpiceBatch import SimCommander

steps = 10  # number of increments for all values
starting_vals = [18, 1, 100, 10]  # initial values for L1, L2, C1, C2


def processing_data(raw_file, log_file):
    print("Handling the simulation data of %s, log file %s" % (raw_file, log_file))

# select spice model
LTC = SimCommander("./Draft1.asc")
# # define simulation
# LTC.add_instructions(
#     "; Simulation settings",
#     ".param run = 0",
#     ".tran 100m"
# )

# for setting in itertools.product(range(steps), repeat=4):
#     LTC.set_component_value('L1', str(starting_vals[0] + setting[0]*10) + "m")
#     LTC.set_component_value('L2', str(starting_vals[1] + setting[1]) + "m")
#     LTC.set_component_value('C1', str(starting_vals[2] + setting[2]*10) + "n")
#     LTC.set_component_value('C2', str(starting_vals[3] + setting[3]) + "n")
#     # overriding he automatic netlist naming
#     run_netlist_file = "{}_{}_{}_{}_{}.net".format(LTC.circuit_radic,  str(setting[0]) + "m",  str(setting[1]) + "m",  str(setting[2]) + "n",  str(setting[3]) + "n")
#     LTC.run(run_filename=run_netlist_file, callback=processing_data)

# # Sim Statistics
# print('Successful/Total Simulations: ' + str(LTC.okSim) + '/' + str(LTC.runno))