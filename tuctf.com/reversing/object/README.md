# object

## Reversing - Points: 500

> We've recovered this file but can't make much of it.
>
> [run.o](run.o)
>

Find the password by using the following `angr` script:

```python
import angr
import claripy
import logging


logging.getLogger('angr.sim_manager').setLevel(logging.DEBUG)

proj = angr.Project("./run", auto_load_libs=False)

password = claripy.BVS('password', 44*8)

state = proj.factory.blank_state(addr=0x4011f6, add_options={angr.options.LAZY_SOLVES})

buf     = 0x806000
state.memory.store(buf, password, endness='Iend_BE')
state.regs.rdi = buf

for i in range(44):
    state.solver.add(state.solver.And(password.get_byte(i) >= 0x30, password.get_byte(i) <= 0x7E))

sm = proj.factory.simulation_manager(state)

sm.explore(find=(0x4012ad), avoid=(0x401227))

s = sm.found[0]

print("Pass: ", s.solver.eval(password, cast_to=bytes))
```

flag: `TUCTF{c0n6r47ul4710n5_0n_br34k1n6_7h15_fl46}`