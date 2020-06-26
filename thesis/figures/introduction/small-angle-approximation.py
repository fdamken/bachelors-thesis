import matplotlib.pyplot as plt
import numpy as np



lim = (-1.5 * np.pi, 1.5 * np.pi)
domain = np.linspace(*lim, 1000)

sin = np.sin(domain)
cos = np.cos(domain)


plt.figure(figsize = (5, 5))
plt.axvline(ls = 'dashed', alpha = 0.25, color = 'black')
plt.plot(domain, np.sin(domain), label = r'$\sin(\varphi)$')
plt.plot(domain, domain, label = r'Approx. $\sin(\varphi)$')
plt.gca().set_aspect('equal')
plt.xlim(lim)
plt.ylim(lim)
plt.legend(loc = 'upper left')
plt.xlabel(r'$\varphi$')
plt.xticks([-np.pi, 0, np.pi], [r'$-\pi$', r'$0$', r'$\pi$'])
plt.title(r'Small Angle Approximation of $\sin(\varphi)$')
plt.tight_layout()
plt.savefig('generated/small-angle-approximation-sin.pdf')
plt.close()

plt.figure(figsize = (5, 5))
plt.axvline(ls = 'dashed', alpha = 0.25, color = 'black')
plt.plot(domain, np.cos(domain), label = r'$\cos(\varphi)$')
plt.plot(domain, np.ones(domain.shape), label = r'Approx. $\cos(\varphi)$')
plt.gca().set_aspect('equal')
plt.xlim(lim)
plt.ylim(lim)
plt.legend(loc = 'upper left')
plt.xlabel(r'$\varphi$')
plt.xticks([-np.pi, 0, np.pi], [r'$-\pi$', r'$0$', r'$\pi$'])
plt.title(r'Small Angle Approximation of $\cos(\varphi)$')
plt.tight_layout()
plt.savefig('generated/small-angle-approximation-cos.pdf')
plt.close()
