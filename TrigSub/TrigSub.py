from manim import *

class TrigSub(Scene):
    def construct(self):
        # Setup Title    
        title = Text("Foundation of Trigonometric Substitution")
        colored_title = title.copy().set_color_by_gradient(ORANGE, YELLOW)
        title_top = colored_title.copy().to_edge(UP).scale(.75)
        
        # Setup Equations
        initialEq = MathTex(r"\int \frac{1}{\sqrt{a^2+x^2}} \, dx").scale(1.25)
        sub = MathTex(r"\text{let }x = a \tan(\theta) \text{ for } \frac{-\pi}{2} < \theta < \frac{\pi}{2}").scale(1.25)
        dSub = MathTex(r"\text{let }dx = \sec^2(\theta) d\theta").scale(1.25)
        subEq = MathTex(r"\int \frac{a\sec^2(\theta)}{\sqrt{a^2+a^2 \tan^2(\theta)}} \ d\theta").scale(1.25)
        simplifyA = MathTex(r"\sqrt{a^2+(a\tan(\theta))^2} =\sqrt{a^2+a^2\tan^2(\theta)} = \sqrt{a^2(1+\tan^2(\theta))}").scale(1)
        simplifyB = MathTex(r"\sqrt{a^2\sec^2(\theta)} = a\sec(\theta)").scale(1.25)
        expl = MathTex(r"\text{(Absolute value can be ignored within} 0 < \theta < \frac{\pi}{2}\text)").scale(.75).move_to(DOWN).scale(1.25)
        applySimplify = MathTex(r"\int \frac{a\sec^2(\theta)}{a^2\sec(\theta)} \ d\theta").scale(1.25)
        applySimplifyTwo = MathTex(r"\int \frac{\sec(\theta)}{a} d\theta").scale(1.25)
        solve = MathTex(r"\ln|\frac{1}{a}((\sec(\theta)+\tan(\theta))|").scale(1.25)
        convert = MathTex(r"\tan(\theta) = \frac{x}{a} \longrightarrow \sec(\theta)=\frac{\sqrt{a^2+x^2}}{a}").scale(1.25)
        includeX = MathTex(r"\ln|\frac{\sec(\theta)+\tan(\theta)}{a}|").scale(1.25)
        plusC = MathTex(r"\ln|\frac{\sqrt{a^2+x^2}+x}{a}|+C").scale(1.25)
        final = plusC.copy().set_color_by_gradient(ORANGE, YELLOW)
        # Animate Title
        self.play(Write(title, run_time=.5))
        self.play(Write(colored_title, run_time=.5))
        self.remove(title)
        self.play(Transform(colored_title, title_top))

        # Animate Equations
        self.play(Write(initialEq))
        self.wait(.25)
        self.play(Transform(initialEq, sub))
        self.wait(.25)
        self.play(Transform(initialEq, dSub))
        self.wait(.25)
        self.play(Transform(initialEq, subEq))
        self.wait(.25)
        self.play(Transform(initialEq, simplifyA))
        self.wait(.25)
        self.play(Transform(initialEq, simplifyB), FadeIn(expl))
        self.wait(.25)
        self.play(Transform(initialEq, applySimplify), FadeOut(expl))
        self.wait(.25)
        self.play(Transform(initialEq, applySimplifyTwo))
        self.wait(.25)
        self.play(Transform(initialEq, solve))
        self.wait(.25)
        self.play(Transform(initialEq, convert))
        self.wait(.25)
        self.play(Transform(initialEq, includeX))
        self.wait(.25)
        self.play(Transform(initialEq, plusC))
        self.wait(.25)
        self.play(Write(final), run_time=1)
       
        # Final Delay
        self.wait(2)