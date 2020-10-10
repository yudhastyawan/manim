from manimpp import *
import numpy as np

class Test(YScene):
    text1 = TextMobject("$\\int_{a}^{b} x \\,dx$")
    text2 = TextMobject("$F=m \\times a$")
    line1 = Line(np.array([-7,0,0]),np.array([7,0,0]))
    xmin = 0
    xmax = 3*PI
    ymin = 0
    ymax = 1
    dx = PI/2
    dy = 1
    x_vals = list(np.arange(xmin,xmax+dx,dx))
    y_vals = list(np.arange(ymin,ymax+dy,dy))
    axes1 = YAxes(xmin=xmin,xmax=xmax,
                  ymin=ymin,ymax=ymax,
                  x_tick_frequency=PI/2,
                  y_tick_frequency=0.25,
                  x_label_decimal=1,
                  y_label_decimal=2,
                  x_labeled_nums=x_vals,
                  y_labeled_nums=y_vals,
                  y_axis_width=1,
                  x_axis_width=10,
                  axes_color=cm.BLUE_C)

    def construct(self):
        self.setBackgroundColor(cm.WHITE)

        self.axes1.shift(LEFT*5+DOWN*1)
        labels = self.axes1.get_axis_labels("distance","amplitude").set_color(cm.BLACK)
        labels[1].rotate(90*DEGREES)
        coord_ticks = self.axes1.get_coordinate_labels(x_vals=self.x_vals, y_vals=self.y_vals) # add axes ticks
        coord_ticks.set_color(cm.BLACK)
        labels[1].next_to(coord_ticks[1],LEFT)
        labels[0].next_to(coord_ticks[0], DOWN)
        self.add(labels)
        self.add(coord_ticks)
        self.add(self.axes1)

        self.line1.set_color(cm.BLACK)
        self.line1.move_to(3.5*UP)
        self.add(self.line1)

        self.text1.set_color(cm.BLACK)
        self.text1.next_to(self.line1,DOWN)
        self.play(Write(self.text1))
        self.wait()

        self.text2.set_color(cm.BLACK)
        self.text2.next_to(self.text1, DOWN)
        self.play(Write(self.text2))
        self.wait()

        equation = lambda x: np.sin(x)

        graph = self.axes1.get_graph(equation,
                                       color=cm.RED,
                                       x_min=self.xmin,
                                       x_max=self.xmax
                                       )
        self.play(Write(graph))
        self.wait()

if __name__ == '__main__':
    test = Test()
    print(os.getcwd())
    YRender(test,active_preview=True)