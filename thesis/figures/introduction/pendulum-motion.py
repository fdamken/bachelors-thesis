import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sci



ode = lambda t, y: np.array([y[1], np.sin(y[0])])

small_angle_solution = lambda x0, xd0, t: 0.5 * np.exp(-t) * (x0 + np.exp(2 * t) * x0 - xd0 + np.exp(2 * t) * xd0)



t_start = 0
t_end = 10
t_range = np.arange(t_start, t_end, 0.01)

yticks = [0, np.pi / 2.0, np.pi, 3 * np.pi / 2.0, 2 * np.pi]
ytickslabels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']



def solve_ivp(initial_displacement, initial_velocity):
	sol_numerical = sci.solve_ivp(ode, y0 = (initial_displacement, initial_velocity), t_span = (t_start, t_end), t_eval = t_range, method = 'Radau').y[0, :]
	sol_approx = small_angle_solution(initial_displacement, initial_velocity, t_range)
	error = (sol_approx - sol_numerical) ** 2
	return sol_numerical, sol_approx, error



initial_displacement = 0.0872665
initial_velocity = 0
tolerance = 1e-3
sol_numerical, sol_approx, error = solve_ivp(initial_displacement, initial_velocity)

tolerance_violation_t = None
tolerance_violation_err = None
for t, err in zip(t_range, error):
	if err > tolerance:
		tolerance_violation_t = t
		tolerance_violation_err = err
		break
if tolerance_violation_t is None or tolerance_violation_err is None:
	raise Exception('Something has to be wrong! The small angle approx. is not so good.')


fig, ax = plt.subplots()
ax.vlines(tolerance_violation_t, min(yticks), max(yticks), ls = 'dashed', color = 'grey', alpha = 0.25, label = 'Distance greater than ' + str(tolerance))
ax.plot(t_range, sol_numerical, label = 'Numerical Solution (Radau)')
ax.plot(t_range, sol_approx, label = 'Small Angle Solution (Analytical)')
ax.legend()
ax.set_xlim([t_start, t_end])
ax.set_ylim([min(yticks), max(yticks)])
ax.set_yticks(yticks)
ax.set_yticklabels(ytickslabels)
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$\varphi$')
ax.set_title(r'Numerical and Approximate Solution for $\varphi(0) = 5\degree$, $\dot{\varphi} = 0$')
fig.savefig('generated/pendulum-motion-solutions.pdf')

fig, ax = plt.subplots()
ax.vlines(tolerance_violation_t, min(error), max(error), ls = 'dashed', color = 'grey', alpha = 0.25, label = 'Distance greater than ' + str(tolerance))
ax.plot(t_range, error, color = 'red', label = 'Squared Difference')
ax.legend()
ax.set_xlim([t_start, t_end])
ax.set_yscale('log')
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$(\hat{\varphi} - \varphi)^2$')
ax.set_title(r'Squared Difference of Solutions for $\varphi(0) = 5\degree$, $\dot{\varphi} = 0$')
fig.savefig('generated/pendulum-motion-difference.pdf')
