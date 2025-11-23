import sys
import io
from contextlib import redirect_stdout

from student_code_m13_ex3 import Circulo, Rectangulo, Triangulo

checks = []

# Circulo
buf = io.StringIO()
with redirect_stdout(buf):
    Circulo(5).dibujar()
out = buf.getvalue().strip()
checks.append((out, "Dibujando un círculo de radio 5."))

# Rectangulo
buf = io.StringIO()
with redirect_stdout(buf):
    Rectangulo(10, 20).dibujar()
out = buf.getvalue().strip()
checks.append((out, "Dibujando un rectángulo de 10x20."))

# Triangulo
buf = io.StringIO()
with redirect_stdout(buf):
    Triangulo(8, 12).dibujar()
out = buf.getvalue().strip()
checks.append((out, "Dibujando un triángulo de base 8 y altura 12."))

# Polymorphic loop
buf = io.StringIO()
with redirect_stdout(buf):
    formas = [Circulo(7), Rectangulo(5, 10), Triangulo(3, 6)]
    for f in formas:
        f.dibujar()
out_lines = [l.strip() for l in buf.getvalue().strip().splitlines()]
expected_lines = [
    "Dibujando un círculo de radio 7.",
    "Dibujando un rectángulo de 5x10.",
    "Dibujando un triángulo de base 3 y altura 6."
]

# Aggregate checks
all_ok = True
for i, (got, exp) in enumerate(checks, 1):
    if got != exp:
        print(f"Check {i} FAILED:\n  got: '{got}'\n  exp: '{exp}'")
        all_ok = False

if out_lines != expected_lines:
    print("Polymorphic loop FAILED:")
    print("  got:")
    for l in out_lines:
        print(f"    {l}")
    print("  expected:")
    for l in expected_lines:
        print(f"    {l}")
    all_ok = False

if all_ok:
    print("✅ Quick checks passed for example3.")
    sys.exit(0)
else:
    print("❌ Quick checks failed. See details above.")
    sys.exit(1)
