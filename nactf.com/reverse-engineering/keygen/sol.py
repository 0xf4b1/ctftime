import angr
import claripy
import logging


logging.getLogger('angr.sim_manager').setLevel(logging.DEBUG)

proj = angr.Project("./keygen-1")

argv1 = claripy.BVS('argv1', 0xf*8)

state = proj.factory.entry_state(args=["./keygen-1", argv1])

state.solver.add(argv1.get_byte(0) == 0x6e)
state.solver.add(argv1.get_byte(1) == 0x61)
state.solver.add(argv1.get_byte(2) == 0x63)
state.solver.add(argv1.get_byte(3) == 0x74)
state.solver.add(argv1.get_byte(4) == 0x66)
state.solver.add(argv1.get_byte(5) == 0x7b)
state.solver.add(argv1.get_byte(14) == 0x7d)

for i in range(6,14):
    digit = state.solver.And(argv1.get_byte(i) >= 0x30, argv1.get_byte(i) <= 0x39)
    lower = state.solver.And(argv1.get_byte(i) >= 0x41, argv1.get_byte(i) <= 0x5a)
    upper = state.solver.And(argv1.get_byte(i) >= 0x61, argv1.get_byte(i) <= 0x7a)
    state.solver.add(state.solver.Or(digit, lower, upper))

sm = proj.factory.simulation_manager(state)
sm.explore(find=(0x0804936f), avoid=(0x0804938, 0x080492d8, 0x080492c4, 0x080492a5))

found = sm.found[0]
solution = found.solver.eval(argv1, cast_to=bytes)
print(repr(solution))