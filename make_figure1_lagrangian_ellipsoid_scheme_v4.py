import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, FancyBboxPatch, FancyArrowPatch

OUTDIR = '/mnt/data/figure1_scheme_outputs_v4'
os.makedirs(OUTDIR, exist_ok=True)


def rot(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])


def sample_disc(n=55, radius=0.42, center=(-2.4, -1.7), seed=2):
    rng = np.random.default_rng(seed)
    ang = rng.uniform(0, 2*np.pi, size=n)
    rad = np.sqrt(rng.uniform(0, radius**2, size=n))
    return center[0] + rad*np.cos(ang), center[1] + rad*np.sin(ang)


def sample_ellipse(n=140, a=1.85, b=0.95, theta=np.deg2rad(25), center=(1.15, 0.1), seed=7):
    rng = np.random.default_rng(seed)
    ang = rng.uniform(0, 2*np.pi, size=n)
    rad = np.sqrt(rng.uniform(0, 0.88**2, size=n))
    pts = np.vstack([rad*np.cos(ang), rad*np.sin(ang)])
    A = rot(theta) @ np.diag([a, b])
    pts = (A @ pts).T
    pts[:, 0] += center[0]
    pts[:, 1] += center[1]
    return pts[:, 0], pts[:, 1]


def add_box(ax, xy, w, h, lw=1.1):
    patch = FancyBboxPatch(xy, w, h,
                           boxstyle='round,pad=0.02,rounding_size=0.03',
                           facecolor='white', edgecolor='0.35', linewidth=lw)
    ax.add_patch(patch)
    return patch


def add_two_line_box(ax, xy, w, h, title, formula, fontsize_title=12, fontsize_formula=12, lw=1.1):
    x, y = xy
    add_box(ax, xy, w, h, lw=lw)
    ax.text(x + w/2, y + 0.64*h, title, ha='center', va='center', fontsize=fontsize_title)
    ax.text(x + w/2, y + 0.34*h, formula, ha='center', va='center', fontsize=fontsize_formula)


def add_arrow(ax, xy1, xy2, lw=1.2):
    arr = FancyArrowPatch(xy1, xy2, arrowstyle='-|>', mutation_scale=12, linewidth=lw, color='0.2')
    ax.add_patch(arr)
    return arr


fig = plt.figure(figsize=(14.4, 4.8))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1], left=0.04, right=0.985, top=0.88, bottom=0.10, wspace=0.18)

# Panel (a)
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_aspect('equal')
ax1.set_xlim(-3.8, 3.8)
ax1.set_ylim(-2.8, 2.8)
ax1.set_xticks([])
ax1.set_yticks([])
for s in ax1.spines.values():
    s.set_visible(False)
ax1.set_title('Diagnostic', fontsize=14, pad=10)
ax1.text(0.01, 0.98, '(a)', transform=ax1.transAxes, ha='left', va='top', fontsize=13, fontweight='bold')

xx = np.linspace(-3.8, 3.8, 28)
yy = np.linspace(-2.8, 2.8, 20)
X, Y = np.meshgrid(xx, yy)
U = 0.55*np.sin(0.95*Y) + 0.12*np.cos(0.7*X)
V = -0.55*np.sin(0.95*X) + 0.12*np.cos(0.7*Y)
ax1.streamplot(X, Y, U, V, color='0.85', density=0.9, linewidth=0.7, arrowsize=0.55, zorder=0)

circ_center = (-2.45, -1.65)
ax1.add_patch(Circle(circ_center, radius=0.48, fill=False, lw=1.7, ec='tab:blue', zorder=2))
xb, yb = sample_disc(center=circ_center)
ax1.scatter(xb, yb, s=16, color='tab:blue', alpha=0.75, zorder=3)
ax1.text(circ_center[0], circ_center[1]-0.78, r'$t=0$', color='tab:blue', ha='center', va='center', fontsize=11)
add_arrow(ax1, (-1.55, -1.1), (0.0, -0.15), lw=1.3)

ell_center = (1.15, 0.12)
a, b, theta = 1.95, 1.0, np.deg2rad(27)
xo, yo = sample_ellipse(a=a, b=b, theta=theta, center=ell_center)
ax1.scatter(xo, yo, s=18, color='tab:orange', alpha=0.80, zorder=3)
ell = Ellipse(ell_center, width=2*a, height=2*b, angle=np.rad2deg(theta), fill=False, lw=2.0, ec='tab:orange', zorder=4)
ax1.add_patch(ell)
R = rot(theta)
maj = R @ np.array([a, 0.0])
minv = R @ np.array([0.0, b])
ax1.plot([ell_center[0]-maj[0], ell_center[0]+maj[0]], [ell_center[1]-maj[1], ell_center[1]+maj[1]], color='0.45', lw=1.0, alpha=0.6)
ax1.plot([ell_center[0]-minv[0], ell_center[0]+minv[0]], [ell_center[1]-minv[1], ell_center[1]+minv[1]], color='0.45', lw=1.0, alpha=0.6)
ax1.text(ell_center[0], ell_center[1]-1.45, r'$t>0$', color='tab:orange', ha='center', va='center', fontsize=11)
ax1.text(2.75, 1.72, r'$g(t)$', fontsize=12)
ax1.text(1.55, -2.05, 'M(t): coarse-grained gradient', fontsize=10.5)

# Panel (b)
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.axis('off')
ax2.set_title('Model hierarchy', fontsize=14, pad=10)
ax2.text(0.01, 0.98, '(b)', transform=ax2.transAxes, ha='left', va='top', fontsize=13, fontweight='bold')

w, h = 0.58, 0.15
x0 = 0.21
add_two_line_box(ax2, (x0, 0.73), w, h, 'Empirical train', r'$(M(t), g(t))$')
add_two_line_box(ax2, (x0, 0.43), w, h, 'Phenomenological SODE', r'$dM,\, dg$')
add_two_line_box(ax2, (x0, 0.13), w, h, 'Intrinsic model', r'$(v,\, \sigma,\, A,\, \omega,\, \alpha)$')
add_arrow(ax2, (0.50, 0.73), (0.50, 0.58))
add_arrow(ax2, (0.50, 0.43), (0.50, 0.28))
ax2.text(0.57, 0.655, 'identify', fontsize=10, color='0.35')
ax2.text(0.57, 0.355, 'change of variables', fontsize=10, color='0.35')

# Panel (c)
ax3 = fig.add_subplot(gs[0, 2])
ax3.set_xlim(0, 1)
ax3.set_ylim(0, 1)
ax3.axis('off')
ax3.set_title('Calibration logic', fontsize=14, pad=10)
ax3.text(0.01, 0.98, '(c)', transform=ax3.transAxes, ha='left', va='top', fontsize=13, fontweight='bold')

add_box(ax3, (0.08, 0.70), 0.84, 0.18)
ax3.text(0.50, 0.79, r'$dM = B_M \, dt + \Sigma_M \, dW_M$', ha='center', va='center', fontsize=12)
ax3.text(0.50, 0.73, r'$dg = (Mg+gM^\top) \, dt + B_g \, dt + \Sigma_g \, dW_g$', ha='center', va='center', fontsize=12)

for y, lab in zip([0.56, 0.42, 0.28], ['physics ansatz', 'fit generator', 'validate / refine']):
    ax3.text(0.50, y, lab, ha='center', va='center', fontsize=11)
add_arrow(ax3, (0.50, 0.70), (0.50, 0.60))
add_arrow(ax3, (0.50, 0.53), (0.50, 0.45))
add_arrow(ax3, (0.50, 0.39), (0.50, 0.31))
add_arrow(ax3, (0.50, 0.25), (0.50, 0.18))

add_box(ax3, (0.17, 0.04), 0.66, 0.11)
ax3.text(0.50, 0.105, r'$\dot\sigma = 2A\cos\alpha + R_\sigma$', ha='center', va='center', fontsize=12)
ax3.text(0.50, 0.065, r'$R_\sigma = a_0(r) + a_1(r)\sigma$', ha='center', va='center', fontsize=12)

png = os.path.join(OUTDIR, 'fig01_scheme_clean_v4.png')
pdf = os.path.join(OUTDIR, 'fig01_scheme_clean_v4.pdf')
fig.savefig(png, dpi=260, bbox_inches='tight')
fig.savefig(pdf, bbox_inches='tight')
print('saved', png)
print('saved', pdf)
