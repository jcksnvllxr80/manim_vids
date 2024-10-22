from manim import *

class GeometricSeries(Scene):
  def construct(self):
    # Define the scale factor for shrinking squares and rectangles
    unit_size = 4  # This will be the size of the main unit square

    # create full square object
    full_square = Square(side_length=unit_size).set_stroke(WHITE, width=2)

    # Create the summation formula
    sum_formula = MathTex(r"S = \sum_{n=1}^{\infty} \frac{1}{2^n}")
    formula = MathTex(
      r"a=\frac{1}{2},\\r=\frac{1}{2},\\S_n = \frac{a}{1 - r} \approx 1"
    ).scale(1.5)  # Adjust the scale as needed
    formula.move_to(ORIGIN)
    self.play(Write(sum_formula))
    self.wait(1)
    self.play(Transform(sum_formula, formula))
    self.wait(1)
    new_position = LEFT * 5  # Adjust this value to set how far left
    self.play(FadeOut(sum_formula))  # Scale down to 75%
    self.wait(0.5)

    # Create the first rectangle (1/2) - half of the main unit square
    first_rectangle = Rectangle(width=unit_size, height=unit_size / 2)
    first_rectangle.set_fill(BLUE, opacity=0.5)
    first_rectangle.next_to(full_square.get_bottom(), UP, buff=0)
    first_label = MathTex(r"\frac{1}{2}").move_to(first_rectangle).scale(1.0)  # Label

    # Create the second square (1/4) - a quarter of the main unit square, placed on top of the first rectangle
    second_square = Square(side_length=unit_size / 2)
    second_square.set_fill(GREEN, opacity=0.5)
    second_square.next_to(first_rectangle, UP, buff=0).align_to(first_rectangle, LEFT)
    second_label = MathTex(r"\frac{1}{4}").move_to(second_square).scale(0.75)  # Label

    # Create the third rectangle (1/8) - an eighth of the main unit square, placed to the right of the second square and the top of the first
    third_rectangle = Rectangle(width=unit_size / 2, height=unit_size / 4)
    third_rectangle.set_fill(RED, opacity=0.5)
    third_rectangle.next_to(second_square, RIGHT, buff=0).align_to(second_square, DOWN)
    third_label = MathTex(r"\frac{1}{8}").move_to(third_rectangle).scale(0.5)  # Label

    # Create the fourth square (1/16) - a sixteenth of the main unit square, placed above the third rectangle and just to the right of the second
    fourth_square = Square(side_length=unit_size / 4)
    fourth_square.set_fill(YELLOW, opacity=0.5)
    fourth_square.next_to(third_rectangle, UP, buff=0).align_to(third_rectangle, LEFT)
    fourth_label = MathTex(r"\frac{1}{16}").move_to(fourth_square).scale(0.35)  # Label

    # Create the fifth rectangle (1/32) - placed to the right of the fourth square and just on top of the third
    fifth_rectangle = Rectangle(width=unit_size / 4, height=unit_size / 8)
    fifth_rectangle.set_fill(ORANGE, opacity=0.5)
    fifth_rectangle.next_to(fourth_square, RIGHT, buff=0).align_to(fourth_square, DOWN)
    fifth_label = MathTex(r"\frac{1}{32}").move_to(fifth_rectangle).scale(0.25)  # Label

    # Create the sixth square (1/64) - placed to the above of the fifth square and to the right of the fourth
    sixth_square = Square(side_length=unit_size / 8)
    sixth_square.set_fill(PURPLE, opacity=0.5)
    sixth_square.next_to(fifth_rectangle, UP, buff=0).align_to(fifth_rectangle, LEFT)
    sixth_label = MathTex(r"\frac{1}{64}").move_to(sixth_square).scale(0.125)  # Label

    seventh_label = MathTex(r"\dots").next_to(sixth_square, RIGHT, buff=0).scale(0.5)  # Label

    # Add the alternating shapes and labels progressively
    series_label1 = MathTex(r"S = \frac{1}{2}").to_edge(UP)
    self.play(Write(series_label1))
    self.play(FadeIn(first_rectangle), Write(first_label))
    self.wait(1)

    series_label2 = MathTex(r"S = \frac{1}{2} + \frac{1}{4}").to_edge(UP)
    self.play(Transform(series_label1, series_label2))
    self.play(FadeIn(second_square), Write(second_label))
    self.wait(1)

    series_label3 = MathTex(r"S = \frac{1}{2} + \frac{1}{4} + \frac{1}{8}").to_edge(UP)
    self.play(Transform(series_label1, series_label3))
    self.play(FadeIn(third_rectangle), Write(third_label))
    self.wait(1)

    series_label4 = MathTex(r"S = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16}").to_edge(UP)
    self.play(Transform(series_label1, series_label4))
    self.play(FadeIn(fourth_square), Write(fourth_label))
    self.wait(1)

    series_label5 = MathTex(r"S = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \frac{1}{32}").to_edge(UP)
    self.play(Transform(series_label1, series_label5))
    self.play(FadeIn(fifth_rectangle), Write(fifth_label))
    self.wait(1)

    series_label6 = MathTex(r"S = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \frac{1}{32} + \frac{1}{64}").to_edge(UP)
    self.play(Transform(series_label1, series_label6))
    self.play(FadeIn(sixth_square), Write(sixth_label))
    self.wait(1)

    # Draw a full unit square to show how the series fills it
    self.play(Create(full_square), Write(seventh_label))
    self.wait(0.5)

    # Add a label indicating the series approaches 1
    series_label7 = MathTex(r"S = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \frac{1}{32} + \frac{1}{64} + \dots \to 1").to_edge(UP)
    self.play(Transform(series_label1, series_label7))
    self.wait(2)