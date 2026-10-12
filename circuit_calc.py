"""Basic electrical engineering formulas.

All values are in base units: volts (V), amperes (A), ohms (ohm),
farads (F), hertz (Hz) and seconds (s).
"""
import math

# SI prefixes that can be typed after a number, for example 4.7k or 100u
PREFIXES = {
    "p": 1e-12,
    "n": 1e-9,
    "u": 1e-6,
    "m": 1e-3,
    "k": 1e3,
    "M": 1e6,
    "G": 1e9,
}


def parse_value(text):
    """Convert text such as '4.7k', '100u' or '1e3' to a float."""
    text = text.strip()
    if not text:
        raise ValueError("empty value")
    if text[-1] in PREFIXES:
        return float(text[:-1]) * PREFIXES[text[-1]]
    return float(text)


def _positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero")


def _check_resistors(values):
    if not values:
        raise ValueError("at least one resistor is needed")
    for r in values:
        _positive(r, "resistance")


def current(voltage_v, resistance):
    """Ohm's law: I = V / R."""
    _positive(resistance, "resistance")
    return voltage_v / resistance


def voltage(current_a, resistance):
    """Ohm's law: V = I x R."""
    return current_a * resistance


def power(voltage_v, current_a):
    """Electrical power: P = V x I."""
    return voltage_v * current_a


def series_resistance(values):
    """Total resistance of resistors in series."""
    _check_resistors(values)
    return sum(values)


def parallel_resistance(values):
    """Total resistance of resistors in parallel."""
    _check_resistors(values)
    return 1 / sum(1 / r for r in values)


def voltage_divider(vin, r1, r2):
    """Output voltage across R2 of a divider: Vout = Vin x R2 / (R1 + R2)."""
    _positive(r1, "R1")
    _positive(r2, "R2")
    return vin * r2 / (r1 + r2)


def rc_time_constant(resistance, capacitance):
    """Time constant of an RC circuit: tau = R x C."""
    _positive(resistance, "resistance")
    _positive(capacitance, "capacitance")
    return resistance * capacitance


def rc_charge_voltage(vs, resistance, capacitance, t):
    """Capacitor voltage after t seconds of charging: Vs x (1 - e^(-t / tau))."""
    if t < 0:
        raise ValueError("time cannot be negative")
    tau = rc_time_constant(resistance, capacitance)
    return vs * (1 - math.exp(-t / tau))


def ripple_voltage(load_current, mains_frequency, capacitance, full_wave=True):
    """Approximate ripple voltage of a rectifier with a smoothing capacitor.

    Full wave: Vripple = I / (2 x f x C). Half wave: Vripple = I / (f x C).
    """
    _positive(mains_frequency, "frequency")
    _positive(capacitance, "capacitance")
    factor = 2 if full_wave else 1
    return load_current / (factor * mains_frequency * capacitance)
