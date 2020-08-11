import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sci



d = 0.1
ode = lambda t, y: np.array([y[1], np.sin(y[0]) - d * y[1]])



t_start = 0
t_end = 100
t_range = np.arange(t_start, t_end, 0.01)

yticks = [0, np.pi / 2.0, np.pi, 3 * np.pi / 2.0, 2 * np.pi]
ytickslabels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']



initial_displacement = 0.0872665
initial_velocity = 0
sol_numerical = sci.solve_ivp(ode, y0 = (initial_displacement, initial_velocity), t_span = (t_start, t_end), t_eval = t_range, method = 'Radau').y[0, :]

fig, ax = plt.subplots()
ax.plot(t_range, sol_numerical, label = 'Solution (Radau)')
ax.legend()
ax.set_xlim([t_start, t_end])
ax.set_ylim([min(yticks), max(yticks)])
ax.set_yticks(yticks)
ax.set_yticklabels(ytickslabels)
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$\varphi$')
ax.set_title(r'Solution for $\varphi(0) = 5\degree$, $\dot{\varphi} = 0$')
fig.savefig('generated/damped-pendulum-motion.pdf')
