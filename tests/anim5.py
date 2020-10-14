from manimpp import *

class Anim5(Scene):
    def construct(self):
        Ftext = TextMobject("F").scale(2)
        Jtext = TextMobject("W").scale(2)
        Fvalue = DecimalNumber(10,num_decimal_places=3,include_sign=False,unit="\\rm N",)
        Jvalue = DecimalNumber(0,num_decimal_places=3,include_sign=False,unit="\\rm Joule",)
        Xvalue = DecimalNumber(0, num_decimal_places=3, include_sign=False, unit="\\rm m", )
        line = Line(0*LEFT+0.5*DOWN,0.5*RIGHT+0.5*DOWN)

        axes = YAxes(xmin=0,xmax=5)
        axes.y_axis.set_stroke(opacity=0)
        rect = Rectangle(width=1,height=1).set_fill(color=cm.GREEN_A,opacity=1)

        Ftext.next_to(axes.x_axis,7*LEFT+1*UP)
        Fvalue.next_to(Ftext,0.5*DOWN)

        Jtext.next_to(Fvalue,2*DOWN)
        Jvalue.next_to(Jtext,0.5*DOWN)

        rect.move_to(axes.c2p(0,0.5))
        Xvalue.next_to(line,0.5*DOWN)

        line.add_updater(lambda l: l.put_start_and_end_on(0*LEFT+0.5*DOWN,rect.get_center()[0]*RIGHT+0.5*DOWN))

        def Xvalue_updater(mob):
            mob.next_to(line,0.5*DOWN)
            mob.set_value(axes.p2c(rect.get_center())[0])

        Xvalue.add_updater(Xvalue_updater)
        Jvalue.add_updater(lambda val: val.set_value(Xvalue.get_value()*Fvalue.get_value()))

        self.add(Ftext,Fvalue,Jtext,Jvalue,Xvalue,axes,rect,line)

        self.play(
            rect.shift,axes.c2p(5,0),
            rate_func=there_and_back,
            run_time=5,

        )
        self.wait()
        Fvalue.set_value(20)
        self.play(
            rect.shift, axes.c2p(5, 0),
            rate_func=there_and_back,
            run_time=5,

        )

        self.wait()

if __name__ == '__main__':
    YRender(Anim5, active_preview=True)