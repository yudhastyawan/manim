from manimpp import *
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm


def multivariate_gaussian(pos, mu, Sigma):
  n = mu.shape[0]
  Sigma_det = np.linalg.det(Sigma)
  Sigma_inv = np.linalg.inv(Sigma)
  N = np.sqrt((2 * np.pi) ** n * Sigma_det)
  fac = np.einsum('...k,kl,...l->...', pos - mu, Sigma_inv, pos - mu)
  return np.exp(-fac / 2) / N

class MplColorHelper:

  def __init__(self, cmap_name, start_val, stop_val):
    self.cmap_name = cmap_name
    self.cmap = plt.get_cmap(cmap_name)
    self.norm = mpl.colors.Normalize(vmin=start_val, vmax=stop_val)
    self.scalarMap = cm.ScalarMappable(norm=self.norm, cmap=self.cmap)

  def get_rgb(self, val):
    return self.scalarMap.to_rgba(val)

  def get_hex(self, val):
    return cm.colors.to_hex(self.get_rgb(val))

class Anim3(Scene):
  def construct(self):
    # Our 2-dimensional distribution will be over variables X and Y
    N = 20
    X1 = np.linspace(-3, 3, N)
    Y1 = np.linspace(-3, 4, N)
    X, Y = np.meshgrid(X1, Y1)

    # Mean vector and covariance matrix
    mu = np.array([0., 1.])
    Sigma = np.array([[1., -0.5], [-0.5, 1.5]])

    # Pack X and Y into a single 3-dimensional array
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X
    pos[:, :, 1] = Y

    Z = multivariate_gaussian(pos, mu, Sigma)
    X = X.flatten()
    Y = Y.flatten()
    Z = Z.flatten()

    clr = MplColorHelper('jet', Z.min(), Z.max())

    xlim = [X.min(),X.max()]
    ylim = [Y.min(),Y.max()]
    axes1 = YAxes(xmin=xlim[0], xmax=xlim[1], ymin=ylim[0], ymax=ylim[1],x_axis_width=5,y_axis_width=6)
    axes_label1 = axes1.get_coordinate_labels(scale_val=0.5)
    width = np.sqrt(np.sum(np.power(axes1.c2p(xlim[0], 0) - axes1.c2p(0, 0), 2)))
    height = np.sqrt(np.sum(np.power(axes1.c2p(0, ylim[0]) - axes1.c2p(0, 0), 2)))
    axes2x = axes1.x_axis.copy().move_to(axes1.x_axis.get_center()+height*DOWN)
    axes2y = axes1.y_axis.copy().move_to(axes1.y_axis.get_center()+width*LEFT)
    axes1.x_axis.set_stroke(opacity=0)
    axes1.y_axis.set_stroke(opacity=0)
    width = np.sqrt(np.sum(np.power(axes2x.get_center() - axes1.c2p(0, 0), 2)))
    height = np.sqrt(np.sum(np.power(axes2y.get_center() - axes1.c2p(0, 0), 2)))
    axes_label1[0].move_to(axes_label1[0].get_center()+height*DOWN)
    axes_label1[1].move_to(axes_label1[1].get_center()+width*LEFT)
    axes_grid1 = axes1.get_grid(5)
    axes_group = VGroup(axes1, axes_label1,axes_grid1,axes2x,axes2y)
    self.add(axes_group)

    width = np.sqrt(np.sum(np.power(axes1.c2p(X1[0],0)-axes1.c2p(X1[1],0),2)))
    height = np.sqrt(np.sum(np.power(axes1.c2p(0, Y1[0]) - axes1.c2p(0, Y1[1]), 2)))
    rectgroup = VGroup()
    for i in range(len(Z)):
      rectgroup.add(Rectangle(width=width,height=height)
                    .move_to(axes1.c2p(X[i],Y[i])).set_fill(color=clr.get_hex(Z[i]),opacity=1)
                    .set_stroke(color=clr.get_hex(Z[i]),opacity=1))
      self.play(FadeIn(rectgroup[-1]),run_time=0.001)
    title = TextMobject("Visualizing the bivariate Gaussian distribution").scale(0.5)
    title.move_to(axes_label1[0].get_center()+0.5*DOWN)
    self.play(Write(title))
    self.wait(3)

if __name__ == '__main__':
    YRender(Anim3, active_preview=True)
