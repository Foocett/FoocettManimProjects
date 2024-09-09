# Ngl chatGPT wrote this whole damn thing bc I had no idea what
# I was doing when I wrote this lmaoooooo

from manim import *

class CircleProof(Scene):
    def construct(self):
        # Setup Title
        title = Text("Deriving The Area of a Circle from an Ellipse").scale(1)
        colored_title = title.copy().set_color_by_gradient(ORANGE, YELLOW)
        title_top = colored_title.copy().to_edge(UP).scale(.85)
        self.play(Write(title, run_time=.5))
        self.play(Write(colored_title, run_time=.5))
        self.remove(title)
        self.play(Transform(colored_title, title_top))
        
        # Step 1: Start with the general equation of an ellipse
        ellipse = Ellipse(width=4, height=2, color=ORANGE).set_fill(ORANGE, opacity=0.5).shift(UP)
        ellipse_eq = MathTex("\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1").shift(DOWN).scale(1.25)
        self.play(Create(ellipse), Write(ellipse_eq))
        self.wait(.25)
        ellipse_target = ellipse_eq.copy().shift(UP)
        self.play(FadeOut(ellipse), Transform(ellipse_eq, ellipse_target))


        # Step 2: Rearrange the equation for y
        rearrange_1 = MathTex("y = b \\sqrt{1 - \\frac{x^2}{a^2}}").scale(1.25)
        self.play(Transform(ellipse_eq, rearrange_1))
        self.wait(.25)

        # Step 3: Further rearrangement of y
        rearrange_2 = MathTex("y = \\frac{b}{a} \\sqrt{a^2 - x^2}").scale(1.25)
        self.play(Transform(ellipse_eq, rearrange_2))
        self.wait(.25)

        # Step 4: Set up the integral from 0 to a for the first quadrant
        integral_setup = MathTex("A = 4 \\int_0^a \\frac{b}{a} \\sqrt{a^2 - x^2} \\, dx").scale(1.25)
        self.play(Transform(ellipse_eq, integral_setup))
        self.wait(.25)

        # Step 5: Perform trigonometric substitution (implied)
        substituted_integral = MathTex("A = 4 \\int_0^{\\frac{\\pi}{2}} b a \\cos^2(\\theta) \\, d\\theta").scale(1.25)
        self.play(Transform(ellipse_eq, substituted_integral))
        self.wait(.25)

        # Step 6: Break down the integration step
        # Cosine squared identity
        cos_squared_identity = MathTex("\\cos^2(\\theta) = \\frac{1 + \\cos(2\\theta)}{2}").scale(1.25)
        self.play(Transform(ellipse_eq, cos_squared_identity))
        self.wait(.25)

        # Applying the identity in the integral
        integral_after_identity = MathTex("A = 2ab \\int_0^{\\frac{\\pi}{2}} \\left( 1 + \\cos(2\\theta) \\right) d\\theta").scale(1.25)
        self.play(Transform(ellipse_eq, integral_after_identity))
        self.wait(.25)

        # Split the integral into two parts
        integral_split = MathTex("A = 2ab \\left[ \\int_0^{\\frac{\\pi}{2}} 1 \\, d\\theta + \\int_0^{\\frac{\\pi}{2}} \\cos(2\\theta) \\, d\\theta \\right]").scale(1.25)
        self.play(Transform(ellipse_eq, integral_split))
        self.wait(.25)

        # Final result of the area of the ellipse
        final_result = MathTex("A = 2ab \\times \\frac{\\pi}{2} = \\pi ab").scale(1.25)
        self.play(Transform(ellipse_eq, final_result))
        self.wait(.25)

        # Step 7: Set a = b = r to get the area of a circle
        ellipse_area = MathTex("A = \\pi ab")
        self.play(Transform(ellipse_eq, ellipse_area))

        # Step 7: Set a = b = r to get the area of a circle
        circle_area = MathTex("A = \\pi r^2")
        circle_area_colored = circle_area.copy().set_color_by_gradient(ORANGE, YELLOW)
        self.play(Transform(ellipse_eq, circle_area))
        self.play(Write(circle_area_colored, run_time=1))

        self.wait(1)
