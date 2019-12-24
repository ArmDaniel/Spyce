# -*- coding: utf-8 -*-
"""


@author: motanov
"""

import netlist as ntl
from netsolve import net_solve

"""

Prototype : just solves the circuit using SpicePy library
To do:
Image to netlist converter ( photo of circuit -> netlist of given circuit )

"""

net = ntl.Network('network.net')

net_solve(net)

net.branch_voltage()
net.branch_current()
net.branch_power()


net.print()
