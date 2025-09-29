# Flujo de trabajo con ASE

ASE (Atomic Simulation Environment) permite crear, manipular y simular estructuras atómicas.

Ejemplo mínimo:
```python
from ase.build import bulk
atoms = bulk('Ti', 'hcp', a=2.95, c=4.68)
```
