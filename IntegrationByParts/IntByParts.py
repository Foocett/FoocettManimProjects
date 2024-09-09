from manim import *

class IntByParts(Scene):
    def construct(self):
        title = Text("Integration By Parts").scale(1.5)
        colored_title = title.copy().set_color_by_gradient(ORANGE, YELLOW)
        title_top = colored_title.copy().to_edge(UP).scale((2/3))
        self.play(Write(title, run_time=1), Write(colored_title, run_time=1.4))
        self.remove(title) 
        self.play(Transform(colored_title, title_top))

        # Step 1a: Write the derivative of the product
        step1a = MathTex(r"\frac{d}{dx}\left[ f(x)g(x) \right]")
        self.play(Write(step1a))
        
        # Step 1b: Fade out the left side and show the product rule result
        step1b = MathTex(r"f'(x)g(x) + f(x)g'(x)")
        self.play(Transform(step1a, step1b))

        # Step 2a: Integrate both sides, starting with the LHS
        step2a = MathTex(r"\int \frac{d}{dx}\left[ f(x)g(x) \right] \, dx")
        self.play(Transform(step1a, step2a))
        
        # Step 2b: Transition to the integrated version on the right side
        step2b = MathTex(r"\int f'(x)g(x) \, dx + \int f(x)g'(x) \, dx")
        self.play(Transform(step1a, step2b))

        
        # Step 3a: LHS simplifies using the fundamental theorem
        step3a = MathTex(r"f(x)g(x)")
        self.play(Transform(step1a, step3a))


        # Step 3b: Transition to the integrated terms on the right side
        step3b = MathTex(r"f(x)g(x) = \int f'(x)g(x) \, dx + \int f(x)g'(x) \, dx")
        self.play(Transform(step1a, step3b))

        # Step 4a: Isolate \int f(x)g'(x) \, dx on the left side
        step4a = MathTex(r"\int f(x)g'(x) \, dx")
        self.play(Transform(step1a, step4a))

        # Step 4b: Move the remaining terms to the right side
        step4b = MathTex(r"f(x)g(x) - \int f'(x)g(x) \, dx")
        self.play(Transform(step1a, step4b))

        # Step 5a: Substituting u and dv (LHS)
        step5a = MathTex(r"\int u \, dv")
        self.play(Transform(step1a, step5a))

        # Step 5b: Transition to the final integration by parts formula on the right
        step5b = MathTex(r"uv - \int v \, du")
        self.play(Transform(step1a, step5b))

        # Optional: Fade out to finish
        self.play(FadeOut(step1a))

