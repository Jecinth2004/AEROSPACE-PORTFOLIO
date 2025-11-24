"""
Starter script: very small dynamics example (projectile) to verify environment.
Run:
    python scripts/6dof_sim.py
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def deriv(t, y):
    # y = [x, vx, z, vz] simple 2D projectile with gravity, no drag
    x, vx, z, vz = y
    ax = 0.0
    az = -9.81
    return [vx, ax, vz, az]

def run():
    y0 = [0.0, 50.0*np.cos(np.deg2rad(45)), 0.0, 50.0*np.sin(np.deg2rad(45))]
    t_span = (0, 10)
    t_eval = np.linspace(t_span[0], t_span[1], 300)
    sol = solve_ivp(deriv, t_span, y0, t_eval=t_eval, rtol=1e-8)
    x = sol.y[0]
    z = sol.y[2]

    plt.figure(figsize=(6,4))
    plt.plot(x, z)
    plt.xlabel('x (m)')
    plt.ylabel('z (m)')
    plt.title('Projectile (starter) — simple 2D trajectory')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run()
