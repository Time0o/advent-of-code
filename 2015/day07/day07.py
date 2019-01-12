#!/usr/bin/env python3

import re
import sys
from typing import Union

RESULT_WIRE = 'a'
OVERRIDE_WIRE = 'b'


circuit = {}
outputs = {}
values = {}


def simulate():
    out = [k for k, v in outputs.items() if v]

    for node in out:
        evaluate(node)


def evaluate(node: Union[str, int]):
    if isinstance(node, int):
        return node

    if node in values:
        return values[node]

    op = circuit[node]

    val = {
        'NOP': lambda: evaluate(op[1]),
        'NOT': lambda: ~evaluate(op[1]),
        'AND': lambda: evaluate(op[1]) & evaluate(op[2]),
        'OR': lambda: evaluate(op[1]) | evaluate(op[2]),
        'LSHIFT': lambda: evaluate(op[1]) << op[2],
        'RSHIFT': lambda: evaluate(op[1]) >> op[2]

    }[op[0]]()

    values[node] = val

    return val


if __name__ == '__main__':
    reg_assign = re.compile(r'([a-z]+|\d+) -> ([a-z]+)')
    reg_not = re.compile(r'NOT ([a-z]+) -> ([a-z]+)')
    reg_op = re.compile(r'([a-z]+|\d+) (AND|OR) ([a-z]+|\d+) -> ([a-z]+)')
    reg_shift = re.compile(r'([a-z]+) (LSHIFT|RSHIFT) (\d+) -> ([a-z]+)')

    for line in sys.stdin:
        line = line.rstrip()

        m_assign = reg_assign.match(line)
        m_not = reg_not.match(line)
        m_op = reg_op.match(line)
        m_shift = reg_shift.match(line)

        if m_assign:
            source, target = m_assign.groups()

            if source.isdigit():
                values[target] = int(source)
            else:
                circuit[target] = ('NOP', source)
                if target not in outputs:
                    outputs[target] = True

        elif m_not:
            source, target = m_not.groups()

            circuit[target] = ('NOT', source)

            outputs[source] = False
            if target not in outputs:
                outputs[target] = True

        elif m_op:
            source1, op, source2, target = m_op.groups()

            if source1.isdigit():
                source1 = int(source1)
            elif source2.isdigit():
                source2 = int(source2)

            circuit[target] = (op, source1, source2)

            if not isinstance(source1, int):
                outputs[source1] = False

            if not isinstance(source2, int):
                outputs[source2] = False

            if target not in outputs:
                outputs[target] = True

        elif m_shift:
            source, op, amount, target = m_shift.groups()

            circuit[target] = (op, source, int(amount))

            outputs[source] = False
            if target not in outputs:
                outputs[target] = True
        else:
            raise ValueError("invalid directive: '{}'".format(line))

    values_old = values.copy()

    simulate()
    result1 = values[RESULT_WIRE]

    values = values_old

    values[OVERRIDE_WIRE] = result1

    if OVERRIDE_WIRE in circuit:
        circuit.pop(OVERRIDE_WIRE)

    simulate()
    result2 = values[RESULT_WIRE]

    fmt = "Final value of wire '{}' is {}."
    print(fmt.format(RESULT_WIRE, result1))

    fmt = "After overriding wire '{}' to that value, the final value {}."
    print(fmt.format(OVERRIDE_WIRE, result2))
