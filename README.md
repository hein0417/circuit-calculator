# Circuit Calculator

A small Python program for basic electrical engineering calculations. It runs in the
terminal, needs no extra packages, and accepts values with engineering prefixes such as
`4.7k` or `100u`.

## Try it online

https://hein0417.github.io/circuit-calculator/

The web page runs the same Python code (`circuit_calc.py`) in your browser using [Pyodide](https://pyodide.org). No installation is needed.

## What it can calculate

- Ohm's law: current, voltage and power
- Resistors in series and in parallel
- Voltage divider output
- RC circuit: time constant and capacitor charging voltage
- Rectifier ripple voltage with a smoothing capacitor (half-wave and full-wave)

## Requirements

- Python 3.8 or newer

## Usage

```bash
python main.py
```

Choose an item from the menu and type the values when asked. You can use these prefixes
after a number: `p` (pico), `n` (nano), `u` (micro), `m` (milli), `k` (kilo), `M` (mega)
and `G` (giga). Scientific notation such as `1e3` also works.

Example (voltage divider with 12 V, 1 kohm and 2 kohm):

```
Choose: 6
Input voltage (V): 12
R1 (ohm): 1k
R2 (ohm): 2k
Output voltage = 8 V
```

## Project files

- `circuit_calc.py` - the formulas, written as small functions
- `main.py` - the menu in the terminal
- `index.html` - the web page that runs `circuit_calc.py` in the browser
- `test_circuit_calc.py` - automatic tests for the formulas

## Run the tests

```bash
python -m unittest
```

## Formulas used

| Calculation | Formula |
|---|---|
| Ohm's law | I = V / R, V = I x R |
| Power | P = V x I |
| Series resistors | R = R1 + R2 + ... |
| Parallel resistors | 1/R = 1/R1 + 1/R2 + ... |
| Voltage divider | Vout = Vin x R2 / (R1 + R2) |
| RC time constant | tau = R x C |
| RC charging | V(t) = Vs x (1 - e^(-t / tau)) |
| Ripple (full-wave) | Vripple = I / (2 x f x C) |
| Ripple (half-wave) | Vripple = I / (f x C) |

The ripple formulas are approximations. Here f is the mains frequency (for example 50 Hz).

## Ideas for improvement

- Plot the RC charging curve with matplotlib
- Add inductor and RL circuit calculations
- Add a command-line version with `argparse`
