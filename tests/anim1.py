from manimpp import *

class Test(MovingCameraScene):
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
    YRender(Test,active_preview=True)