from manimpp import *

class Anim4(Scene):
    def construct(self):
        number_line = NumberLine(x_min=-2, x_max=2)
        text = TextMobject("Text") \
            .next_to(number_line, DOWN)
        dashed_line = DashedLine(
            number_line.get_left(),
            number_line.get_right(),
            color=YELLOW,
        ).set_stroke(width=11)

        self.add(number_line)
        self.wait(0.3)

        self.play(
            LaggedStart(
                *[ShowCreationThenDestruction(dashed_segment)
                  for dashed_segment in dashed_line],
                run_time=5
            ),
            AnimationGroup(
                Animation(Mobject(), run_time=2.1),  # PAUSE
                Write(text), lag_ratio=1
            )
        )
        self.wait()


if __name__ == '__main__':
    YRender(Anim4,active_preview=True)