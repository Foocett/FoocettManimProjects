from manim import *


class SineApprox(Scene):
    def construct(self):
        # Create the axes for plotting
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-2.5, 2.5, 1],
            axis_config={"color": BLUE}
        ) 

        x_axis = axes.get_x_axis()
        y_axis = axes.get_y_axis()

        # Create the title at the top
        anim_title = Text("Taylor Series Approximation of sin(x)", font_size=24).to_edge(UP)
        
        # Create the label for the approximation, initially y = x
        label = MathTex("y = x").next_to(anim_title, DOWN, buff=0.5)
        
        template_sine = axes.plot(lambda x: np.sin(x), color=YELLOW)

        # Initial linear function y = x
        linear_graph = axes.plot(lambda x: x, color=RED)

        # Display the title, axes, and initial graph
        self.play(Write(anim_title, run_time=1), Create(x_axis, run_time=1))  
        self.wait(0.25)
        self.play(Create(template_sine, run_time=1.5), Create(linear_graph, run_time=1.5))
        
        # Add label for y = x under the title
        self.play(Write(label))

        # Taylor series expansion of sin(x)
        def taylor_sin(x, n):
            """Compute the nth Taylor approximation to sin(x)."""
            result = 0
            for k in range(n):
                coef = ((-1) ** k) / np.math.factorial(2 * k + 1)
                result += coef * (x ** (2 * k + 1))
            return result

        # Function to generate LaTeX string for Taylor series approximation
        def taylor_latex(n):
            """Generate the LaTeX for the nth Taylor approximation to sin(x)."""
            terms = []
            for k in range(n):
                sign = "-" if k % 2 == 1 else "+" if k > 0 else ""  # Assign + or - based on k
                denom = f"\\frac{{x^{{{2 * k + 1}}}}}{{{np.math.factorial(2 * k + 1)}}}"
                terms.append(f"{sign} {denom}")
            
            # Join the terms up to n, but stop adding new terms after the fifth one
            if n <= 7:
                equation = " ".join(terms)
            else:
                equation = " ".join(terms[:7]) + " + \\dots"  # Add ellipsis after the 5th term

            return equation

        # First transformation from y = x to first Taylor term (just x)
        approx_wave = axes.plot(lambda x: taylor_sin(x, 1), color=RED)
        self.play(Transform(linear_graph, approx_wave))

        # Speed scaling for exponentially increasing speed
        speed_factor = 1
        scale_factor = 1

        # Add more terms in the Taylor series
        for n in range(2, 15):
            new_wave = axes.plot(lambda x, n=n: taylor_sin(x, n), color=RED)
            # Update the label with the current Taylor series approximation equation
            latex_str = taylor_latex(n)
            new_label = MathTex(f"y = {latex_str}")
            
            # Ensure the label is centered and grows symmetrically
            new_label.scale(scale_factor).next_to(anim_title, DOWN, buff=0.5)
            
            # Smooth transition between label versions
            self.play(Transform(label, new_label), Transform(linear_graph, new_wave), run_time=1 / speed_factor)
            speed_factor *= 1.2  # Exponentially increasing speed
            if n < 7:
                scale_factor *= .975 # Decrease the scale factor for the label
    

                # General Taylor series for sin(x)
        general_taylor = MathTex(
            r"\sin(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}"
        ).next_to(anim_title, DOWN, buff=0.5)

        # Transition the label into the general Taylor series form
        self.play(Transform(label, general_taylor))

        new_label = label.copy().set_color_by_gradient(ORANGE, YELLOW)
        new_title = anim_title.copy().set_color_by_gradient(ORANGE, YELLOW)
        self.play(Write(new_label, run_time=1), 
                  Write(new_title, run_time=1))

        self.wait(2)
