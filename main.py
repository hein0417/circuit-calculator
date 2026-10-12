"""Simple menu for the circuit calculator."""
from circuit_calc import (
    current,
    parallel_resistance,
    parse_value,
    power,
    rc_charge_voltage,
    rc_time_constant,
    ripple_voltage,
    series_resistance,
    voltage,
    voltage_divider,
)

MENU = """
Circuit Calculator
  1  Current        (I = V / R)
  2  Voltage        (V = I x R)
  3  Power          (P = V x I)
  4  Resistors in series
  5  Resistors in parallel
  6  Voltage divider
  7  RC circuit (time constant and charging voltage)
  8  Rectifier ripple voltage
  0  Quit

You can type values like 4.7k, 100u or 1e3 (p n u m k M G).
"""


def ask(prompt):
    return parse_value(input(prompt))


def ask_list(prompt):
    return [parse_value(x) for x in input(prompt).split()]


def run_choice(choice):
    if choice == "1":
        v = ask("Voltage (V): ")
        r = ask("Resistance (ohm): ")
        print(f"Current = {current(v, r):.4g} A")
    elif choice == "2":
        i = ask("Current (A): ")
        r = ask("Resistance (ohm): ")
        print(f"Voltage = {voltage(i, r):.4g} V")
    elif choice == "3":
        v = ask("Voltage (V): ")
        i = ask("Current (A): ")
        print(f"Power = {power(v, i):.4g} W")
    elif choice == "4":
        values = ask_list("Resistances in ohm, separated by spaces: ")
        print(f"Total resistance = {series_resistance(values):.4g} ohm")
    elif choice == "5":
        values = ask_list("Resistances in ohm, separated by spaces: ")
        print(f"Total resistance = {parallel_resistance(values):.4g} ohm")
    elif choice == "6":
        vin = ask("Input voltage (V): ")
        r1 = ask("R1 (ohm): ")
        r2 = ask("R2 (ohm): ")
        print(f"Output voltage = {voltage_divider(vin, r1, r2):.4g} V")
    elif choice == "7":
        vs = ask("Supply voltage (V): ")
        r = ask("Resistance (ohm): ")
        c = ask("Capacitance (F): ")
        t = ask("Time (s): ")
        print(f"Time constant = {rc_time_constant(r, c):.4g} s")
        print(f"Capacitor voltage after {t:.4g} s = {rc_charge_voltage(vs, r, c, t):.4g} V")
    elif choice == "8":
        i = ask("Load current (A): ")
        f = ask("Mains frequency (Hz, for example 50): ")
        c = ask("Smoothing capacitance (F): ")
        full = input("Full-wave rectifier? (y/n): ").strip().lower() != "n"
        print(f"Ripple voltage = {ripple_voltage(i, f, c, full):.4g} V")
    else:
        print("Please choose a number from the menu.")


def main():
    print(MENU)
    while True:
        try:
            choice = input("Choose: ").strip()
            if choice == "0":
                break
            run_choice(choice)
        except ValueError as error:
            print(f"Invalid input: {error}")
        except (EOFError, KeyboardInterrupt):
            print()
            break


if __name__ == "__main__":
    main()
