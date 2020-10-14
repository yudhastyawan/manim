 # The Galleries of Tests Folder
 
 ## Anim1
 
 
 ```python
 from manimpp import *

class Anim1(MovingCameraScene):
    CONFIG = {
        "camera_config" : {
            "background_color" : cm.BLACK
        }
    }

    xlim = [-3,5.2]
    ylim = [-2,3.5]
    axes1 = YAxes(xlim[0],xlim[1],ylim[0],ylim[1],x_label_decimal=0,y_label_decimal=0)

    def construct(self):
        mgr = VGroup()
        self.axes1.set_stroke(cm.WHITE,1)
        label1 = self.axes1.get_coordinate_labels(list(np.arange(self.xlim[0],self.xlim[1])),
                                                  list(np.arange(self.ylim[0],self.ylim[1])),scale_val=0.5)
        axis_label = self.axes1.get_axis_labels()
        label1.set_color(cm.DARK_GRAY)
        grid = self.axes1.get_grid(5)
        mgr.add(self.axes1,label1,grid, axis_label)
        self.add(self.axes1, axis_label)
        self.play(Write(grid),run_time=5)
        self.add(label1)
        self.play(mgr.move_to,-1*RIGHT)

        graph = self.axes1.get_graph(lambda x: np.log(x), x_min=0.1, x_max=self.xlim[1])
        graph_label = TextMobject("$f(x)=\\ln{x}$").next_to(graph)

        self.play(Write(graph))
        self.add(graph_label)

        graph2 = self.axes1.get_graph(lambda x: x**2, x_min=self.xlim[0], x_max=self.xlim[1])
        graph_label2 = TextMobject("$f(x)=x^2$").next_to(graph)
        self.play(ReplacementTransform(graph,graph2),ReplacementTransform(graph_label,graph_label2))

        circle = Circle(radius=1).shift(self.axes1.c2p(0,0))
        self.play(ReplacementTransform(graph2,circle))
        self.play(
            self.camera_frame.scale,0.5,
            self.camera_frame.move_to, circle.get_center(),
        )
        self.play(FadeOut(mgr),FadeOut(graph_label2))
        self.play(DrawBorderThenFill(circle.set_fill(cm.WHITE,1).set_color(cm.WHITE)))
        self.play(circle.scale, 0.7)
        ytext = TextMobject("y").move_to(circle.get_center()).set_color(cm.BLACK).scale(2)
        self.play(Write(ytext))
        nametext = TextMobject("yudha styawan").next_to(circle,RIGHT)
        self.play(
            self.camera_frame.scale, 1,
            self.camera_frame.move_to, circle.get_center()+2*RIGHT,
            Write(nametext)
        )
        self.wait(3)

if __name__ == '__main__':
    YRender(Anim1,active_preview=True)
 ```
 
 <p align="center"><img src ="./gifs/Anim1.gif" /></p>
 
## Anim2
 
 
 ```python
 from manimpp import *

class Anim2(Scene):
    def construct(self):
        background = Rectangle(width=FRAME_WIDTH, height=FRAME_HEIGHT)
        background.set_fill(color=["#00004a","#00004a","#000078"],opacity=1)
        background.set_stroke(width=0)
        text = TextMobject("\\texttt{Yudha Styawan}").set_color(color=cm.WHITE).scale(2)
        text.set_stroke("#D92121",width=1, opacity=1)
        self.add(background)
        self.add(text)
        self.wait(3)


if __name__ == '__main__':
    YRender(Anim2,active_preview=True)
 ```
 
 <p align="center"><img src ="./gifs/Anim2.gif" /></p>
 
## Anim3
 
 
 ```python
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

 ```
 
 <p align="center"><img src ="./gifs/Anim3.gif" /></p>
 
 
