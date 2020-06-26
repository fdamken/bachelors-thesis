import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sci



ode = lambda t, y: np.array([y[1], -np.sin(y[0])])

small_angle_solution = lambda x0, xd0, t: x0 * np.cos(t) + xd0 * np.sin(t)



t_start = 0
t_end = 100
t_range = np.arange(t_start, t_end, 0.01)

yticks = [-np.pi / 2.0, 0, np.pi / 2.0]
ytickslabels = [r'$-\frac{\pi}{4}$', r'$0$', r'$\frac{\pi}{4}$']



def solve_ivp(initial_displacement, initial_velocity):
	sol_numerical = sci.solve_ivp(ode, y0 = (initial_displacement, initial_velocity), t_span = (t_start, t_end), t_eval = t_range).y[0, :]
	sol_approx = small_angle_solution(initial_displacement, initial_velocity, t_range)
	error = sol_numerical - sol_approx
	return sol_numerical, sol_approx, error



def plot_solution(initial_displacement, initial_velocity, initial_displacement_latex = None, initial_velocity_latex = None):
	sol_numerical, sol_approx, error = solve_ivp(initial_displacement, initial_velocity)

	fig, (ax1, ax2) = plt.subplots(2, 1, sharex = True, figsize = (10, 8))
	ax1.plot(t_range, sol_numerical, label = 'Numerical Solution (RK45)')
	ax1.plot(t_range, sol_approx, label = 'Small Angle Solution (Analytical)')
	ax2.plot(t_range, error, color = 'red', label = 'Error')
	ax1.legend()
	ax2.legend()
	#ax1.set_yticks(yticks)
	#ax2.set_yticks(yticks)
	#ax1.set_yticklabels(ytickslabels)
	#ax2.set_yticklabels(ytickslabels)
	ax1.set_ylabel(r'$\varphi$')
	ax2.set_ylabel(r'$\varphi$')
	ax2.set_xlabel(r'$t$')
	initial_displacement_latex = str(initial_displacement) if initial_displacement_latex is None else initial_displacement_latex
	initial_velocity_latex = str(initial_velocity) if initial_velocity_latex is None else initial_velocity_latex
	fig.suptitle(r'Comparison of Solutions for $\varphi(0) = ' + initial_displacement_latex + r'$ and $\dot{\varphi}(0) = ' + initial_velocity_latex + '$')
	fig.savefig('generated/pendulum-motion-%s-%s.pdf' % (str(int(initial_displacement * 100)), str(int(initial_velocity * 100))))
	fig.show()



plot_solution(0.0, 0.1)
plt.show()



#initial_velocity = 0.0
#for initial_displacement in [0.01, 0.05, 0.1]:
#	plot_solution(initial_displacement, 0.0)
#
#initial_displacement = 0.0
#for initial_velocity in [0.01, 0.05, 0.1, 0.5]:
#	plot_solution(0.0, initial_velocity)
