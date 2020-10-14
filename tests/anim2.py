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