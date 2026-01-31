# Math using Python

Welcome — this repository contains teaching materials, examples, and exercises that use Python to explore and teach mathematics.

## About the instructor
I am ADIL MUKHTAR SHAH, a mathematics teacher with over 17 years of classroom experience. I created these materials to help students (and fellow teachers) learn mathematical concepts through interactive Python examples, clear visualisations, and hands-on exercises.

## Purpose
This repo is designed to:
- Demonstrate mathematical concepts with runnable Python code and Jupyter notebooks.
- Provide classroom-ready exercises and solutions.
- Offer visualisations that make abstract ideas concrete.
- Help teachers adopt Python in their teaching practice.

## Who is this for?
- Secondary and early undergraduate students learning algebra, calculus, linear algebra, probability, and statistics.
- Teachers who want ready-made Python examples and lesson material.
- Self-learners who prefer learning mathematics by doing.

## Repository structure (suggested)
- notebooks/ — interactive Jupyter notebooks for lessons and demos
- examples/ — small, focused Python examples and scripts
- exercises/ — student exercises and worksheets
- solutions/ — solution notebooks and scripts
- slides/ — slide decks and lesson plans
- data/ — example datasets used in lessons
- requirements.txt — Python packages used in the repo

## Requirements
Typical dependencies:
- Python 3.8+
- numpy
- scipy
- sympy
- matplotlib
- pandas
- jupyter (or jupyterlab)

Install with:
```bash
pip install -r requirements.txt
```

## Quick start
Open a notebook from the `notebooks/` folder with Jupyter, or run small examples from `examples/`. Here is a short Python example that solves a quadratic equation and plots the quadratic:

```python name=examples/quick_start.py url=https://github.com/ADIL8590/python-math/blob/main/examples/quick_start.py
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# coefficients for ax^2 + bx + c = 0
a, b, c = 1, -3, 2  # roots: 1 and 2

discriminant = b**2 - 4*a*c
roots = ((-b + np.sqrt(discriminant)) / (2*a), (-b - np.sqrt(discriminant)) / (2*a))
print("Roots:", roots)

# plot
x = np.linspace(-1, 4, 400)
y = a * x**2 + b * x + c
plt.axhline(0, color='black', linewidth=0.8)
plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
plt.scatter(roots, [0, 0], color='red')
plt.legend()
plt.title('Quadratic: roots and curve')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```

## Example lesson topics
- Algebra: solving equations, factorisation, polynomial behaviour
- Calculus: limits, derivatives (symbolic via sympy), numerical differentiation, integrals and area
- Linear Algebra: vectors, matrices, eigenvalues, visual intuition
- Probability & Statistics: distributions, sampling, hypothesis basics
- Geometry: coordinate geometry, transformations, plotting conic sections
- Number Theory & Sequences: modular arithmetic, recurrence relations

## Teaching suggestions
- Use notebooks to present theory, then switch to hands-on exercises.
- Start with numeric examples (numpy) then introduce symbolic reasoning (sympy).
- Encourage students to modify parameters and observe changes in plots.
- Provide short, targeted exercises with immediate automated checks where possible.

## Contributing
Contributions are welcome:
- Add new notebooks or exercises
- Improve explanations and visualisations
- Submit issues for errors or unclear material
Please follow the repository style (clear markdown explanations, working notebooks, and minimal dependencies).

## License
This repository is shared for educational use. If you have a preferred license, add a LICENSE file (e.g., MIT).

## Contact
ADIL MUKHTAR SHAH  
Mathematics Teacher — 17+ years experience  
GitHub: [ADIL8590](https://github.com/ADIL8590)  
Email: (add your email here)

