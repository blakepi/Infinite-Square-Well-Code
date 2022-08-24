from ctypes import alignment
from curses.ascii import CR
from quopri import encodestring
from sys import api_version
from turtle import width
from manim import *
from scipy.fftpack import shift
class logo(Scene):
    def construct(self):
        ytlogo = MathTex(r"\beta\lambda\alpha\kappa\epsilon \: \Pi", font_size = 100)
        logo2 = Text('Animated Physics Videos', gradient = (RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE))
        sov = Text('Separation of Variables',font_size=75).shift(UP*1.2)
        assume = MathTex(r"Assume\:\Psi=\psi(x)\phi(t)",font_size=90).shift(DOWN)
        assume[0][6].set_color(PURPLE)
        assume[0][8:12].set_color(RED)
        assume[0][12:16].set_color(BLUE)
        
        self.add(sov)
        self.add(assume)

class scene1(Scene):
    def construct(self):
        #self.camera.background_color = '#8AAAE5'
        titletext = Text('The Infinite Well Potential', font_size=50, gradient = (RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE))
        #blakepi = MathTex(r"by\:\mathbb{B}\mathbb{L}\mathbb{A}\mathbb{K}\mathbb{E} \Pi", font_size = 100)
        blakepi = MathTex(r"by\: \beta\lambda\alpha\kappa\epsilon \: \Pi", font_size = 100)
        
        self.play(Write(titletext))
        self.wait()
        self.play(Transform(titletext, blakepi))
        self.wait()
        self.wait()
        self.wait()
        self.play(FadeOut(titletext))
        

class scene2(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        se = MathTex(r"-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2}+V(x)\psi(x)=E\psi(x)").shift(UP*0.65)
        inpot = Text('Solved in the infinite square well potential.',font_size=30).shift(DOWN)
        the1d = Text('The 1D Time-Independent Schrödinger Equation (TISE):',font_size=35).shift(UP*2)
        noap = MathTex(r"sin(x)\approx x",font_size=100)
        noapp = Text("No approximations necessary!",color=RED).shift(DOWN*1.1)
        l = Line(start=LEFT*3,end=RIGHT*3,color=RED,stroke_width=20)
        #pot = Rectangle(color=BLACK,width=4,height=10).shift(UP*4)
        
        pot = Axes(x_range=[-0.5,2,0.1], y_range=[-1,10,100], tips = False)
        x_label = pot.get_x_axis_label("x")
        y_label = pot.get_y_axis_label("V(x)")
        a = MathTex('0',color=RED).shift(LEFT*3.4+DOWN*3)
        b = MathTex('L',color=BLUE).shift(RIGHT*1.2+DOWN*3)

        aline = Arrow(start = LEFT*3.6 + DOWN*2.7, end=UP*3+LEFT*3.6, color=RED, stroke_width = 8)
        bline = Arrow(start = RIGHT*1.2 + DOWN*2.7, end = UP*3 + RIGHT*1.2, color=BLUE, stroke_width = 8)
        ptit = Text("∞ Square Well Potential",color=WHITE, font_size=40).shift(DOWN*3)
        #self.add(pot,well2,x_label,y_label,ptit)
        
        self.wait()
        self.play(Write(the1d))
        self.play(Write(se))
        self.play(Create(inpot))
        self.wait()
        self.wait()
        self.play(FadeOut(inpot),FadeOut(the1d))
        self.wait()
        self.play(Transform(se,noap))
        self.wait()
        self.play(Create(l),Write(noapp))
        self.wait()
        self.play(FadeOut(noap,noapp,l))
        self.play(Transform(se,pot))
        self.play(Write(x_label))
        self.play(Write(y_label))
        self.play(Create(aline),Create(bline))
        self.play(Write(ptit))
        self.wait()
        self.play(Uncreate(ptit))

class scene3(Scene):
    def construct(self):
        
        pot = Axes(x_range=[-0.5,2,0.1], y_range=[-1,10,100], tips = False)
        x_label = pot.get_x_axis_label("x")
        y_label = pot.get_y_axis_label("V(x)")
        a = MathTex('0',color=RED).shift(LEFT*3.4+DOWN*3)
        b = MathTex('L',color=BLUE).shift(RIGHT*1.2+DOWN*3)

        aline = Arrow(start = LEFT*3.6 + DOWN*2.7, end=UP*3+LEFT*3.6, color=RED, stroke_width = 8)
        bline = Arrow(start = RIGHT*1.2 + DOWN*2.7, end = UP*3 + RIGHT*1.2, color=BLUE, stroke_width = 8)
        b2 = MathTex('L',color=BLUE).shift(LEFT+DOWN*3)
        bline2 = Arrow(start = LEFT + DOWN*2.7, end = UP*3 + LEFT, color=BLUE, stroke_width = 8)

        vft = MathTex(r"V(x) = \begin{cases}0\text\:{for}\:\:0<x<L\\ \infty\text\:{for}\:\:x<0,x>L \end{cases}").shift(RIGHT*3+UP*2)
        
        
        self.add(pot, x_label, y_label, aline, bline)
        self.wait()
        self.play(Write(a), Write(b))
        self.wait()
        self.play(Transform(b,b2),Transform(bline,bline2))
        self.play(Write(vft))
        self.wait()

class scene4(Scene):
    def construct(self):
        pot = Axes(x_range=[-0.5,2,0.1], y_range=[-1,10,100], tips = False)
        x_label = pot.get_x_axis_label("x")
        y_label = pot.get_y_axis_label("V(x)")
        a = MathTex('0',color=RED).shift(LEFT*3.4+DOWN*3)
        b2 = MathTex('L',color=BLUE).shift(LEFT+DOWN*3)
        aline = Arrow(start = LEFT*3.6 + DOWN*2.7, end=UP*3+LEFT*3.6, color=RED, stroke_width = 8)
        bline2 = Arrow(start = LEFT + DOWN*2.7, end = UP*3 + LEFT, color=BLUE, stroke_width = 8)
        vft = MathTex(r"V(x) = \begin{cases}0\text\:{for}\:\:0<x<L\\ \infty\text\:{for}\:\:x<0,x>L \end{cases}").shift(RIGHT*3+UP*2) 

        particle = Text('Particle',color =PURPLE, font_size=30).shift(LEFT*2.25, DOWN*0.9)
        aq = Text('*A Quantum',color=PURPLE, font_size=25).next_to(particle,UP*0.6)
        ptarr = Arrow( start = LEFT*2.25 + DOWN, end = LEFT*2.25 + DOWN*2.4, color = PURPLE, stroke_width=8)
        part1 = Circle(radius = 0.15, color=PURPLE, fill_color = PURPLE, fill_opacity =1).shift(LEFT*2.25+DOWN*2.5)
        part = pot.plot(lambda x: np.sinc(20*(x-0.275)), x_range=[0,0.55], color=PURPLE)

        self.add(pot, x_label, y_label, a, b2, aline, bline2, vft)

        part1.generate_target()
        part1.target.shift(1.2*LEFT)
        self.play(Create(part1),Create(ptarr),Write(particle))
        self.wait()
        self.wait()
        self.play(Write(aq))
        self.wait()
        self.play(Transform(part1,part), Uncreate(ptarr))
        self.play(Uncreate(particle),Uncreate(aq))
        self.wait()
        self.play(MoveToTarget(part1))
        part1.generate_target()
        part1.target.shift(2.3*RIGHT)
        self.play(MoveToTarget(part1))
        part1.generate_target()
        part1.target.shift(2.3*LEFT)
        self.play(MoveToTarget(part1))
        part1.generate_target()
        part1.target.shift(2.3*RIGHT)
        self.play(MoveToTarget(part1))
        part1.generate_target()
        part1.target.shift(2.3*LEFT)
        self.play(MoveToTarget(part1))


class scene5(Scene):
    def construct(self):
        se = MathTex(r"-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2}+V(x)\psi(x)=E\psi(x)",font_size=35)
        se2 = MathTex(r"-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2}+0\cdot\psi(x)=E\psi(x)",font_size=35)
        se3 = MathTex(r"-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2}=E\psi(x)",font_size=35)
        reg = Text('Inside the region 0<x<L, V(x) = 0, so:', font_size = 25).shift(UP*1.1)
        diff = Text('is a second-order linear ordinary differential equation',font_size=25).shift(DOWN)
        
        self.play(Create(se))
        self.wait()
        self.play(Write(reg))
        self.play(Transform(se,se2))
        self.wait()
        self.wait()
        self.play(Transform(se,se3))
        self.wait()
        self.wait()
        self.play(Write(diff))
        self.wait()
        self.play(Uncreate(reg))
        self.wait()
        self.play(FadeOut(se),FadeOut(diff))
        self.wait()
        self.wait()

class scene6(Scene):
    def construct(self):
        se3 = MathTex(r"-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2}=E\psi(x)").shift(DOWN*0.3)
        step10 = Text("Tidy things up (optional).")
        k = MathTex(r"k = \frac{\sqrt{2mE}}{\hbar}")
        step1 = Text("Step 1: Assume a solution of the form:",font_size=40).shift(UP*2)
        ans = MathTex(r"\psi(x)=e^{\lambda x}",font_size=60).shift(UP)
        step2t = Text("Step 2:",font_size =40).shift(UP*2).shift(LEFT*3)
        step2 = MathTex(r"Substitute\: \psi(x)\: into\: TISE.", font_size = 50).next_to(step2t,RIGHT)
        se4 = MathTex(r"-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} e^{\lambda x} = Ee^{\lambda x}").shift(DOWN*1.8)
        se4p2 = MathTex(r"-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} e^{\lambda x} - Ee^{\lambda x} = 0").shift(DOWN*1.8)
        step3 = Text("Step 3: Calculate derivative.")
        dev1 = MathTex(r"{d^2}{dx^2} e^{\lambda x}")
        dev2 = MathTex(r"{d^2}{dx^2} e^{\lambda x} = \lambda^2 e^{\lambda x}")
        dev3 = MathTex(r"-\frac{\hbar^2}{2m}\lambda^2 e^{\lambda x} = Ee^{\lambda x}")
        dev4 = MathTex(r"(-\frac{\hbar^2}{2m}\lambda^2-E)e^{\lambda x}=0")
        Since = MathTex(r"e^{\lambda x} \neq 0\: for\: finite\: \lambda")
        Thus = Text("Thus, we know our zeros must come from the polynomial:")
        Poly = MathTex(r"(-\frac{\hbar^2}{2m}\lambda^2-E)=0")
        solvefor = MathTex(r"Step\: 4\: :\: Solve\: for\: \lambda .")
        lam = MathTex(r"\lambda = frac{i\sqrt{E}}{sqrt{frac{\hbar^2}{2m}}}")
        o = Text('or')
        lam2 = MathTex(r"\lambda = -frac{i\sqrt{E}}{sqrt{frac{\hbar^2}{2m}}}")
        Thus = Text("So, the general solution is:")
        #gensol = MathTex(r"\psi(x)=Ae^frac{i\sqrt{E}}{sqrt{frac{\hbar^2}{2m}}}\cdotx + Be^-frac{i\sqrt{E}}{sqrt{frac{\hbar^2}{2m}}}\cdotx")
        #self.add(se3, step2t,step2,ans)
        self.play(Write(step1))
        self.wait()
        self.wait()
        self.play(Write(ans))
        self.wait()
        self.wait()
        self.wait()
        self.play(Transform(step1,step2t))
        self.wait()
        self.play(Write(step2))
        self.wait()
        self.wait()
        self.wait()
        self.play(Create(se3))
        self.wait()
        self.wait()
        self.play(Create(se4))
        self.wait()
        self.wait()
        self.wait()
        self.play(Transform(se4,se4p2))
        self.wait()
        self.wait()

class scene7(Scene):
    def construct(self):

        se3 = MathTex(r"-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2}=E\psi(x)").shift(DOWN*0.3)
        se4p2 = MathTex(r"-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} e^{\lambda x} - Ee^{\lambda x} = 0").shift(DOWN*1.8)
        ans = MathTex(r"\psi(x)=e^{\lambda x}",font_size=60).shift(UP)
        step2t = Text("Step 2:",font_size = 40).shift(UP*2).shift(LEFT*3)
        step3t = Text('Step 3: Calculate the derivative.',font_size=40).shift(UP*2)
        step2 = MathTex(r"Substitute\: \psi(x)\: into\: TISE.", font_size = 50).next_to(step2t,RIGHT)

        sse3 = MathTex(r"-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2}=E\psi(x)").shift(DOWN*0.3+LEFT*3.5)
        sse4p2 = MathTex(r"-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} e^{\lambda x} - Ee^{\lambda x} = 0").shift(DOWN*1.8+LEFT*3.5)
        sans = MathTex(r"\psi(x)=e^{\lambda x}",font_size=60).shift(UP+LEFT*3.5)
        sstep2t = Text("Step 2:",font_size =40).shift(UP*2).shift(LEFT*3+LEFT*3.5)
        sstep2 = MathTex(r"Substitute\: \psi(x)\: into\: TISE.", font_size = 50).next_to(step2t,RIGHT+LEFT*3.5)

        
        
        deriv = MathTex(r"\frac{d^2}{dx^2} e^{\lambda x}").shift(RIGHT*1.5+UP)
        dereq = MathTex(r"=\frac{d}{dx}(\frac{d}{dx}e^{\lambda x})").next_to(deriv,RIGHT)
        der2 = MathTex(r"=\frac{d}{dx}(\lambda e^{\lambda x})").next_to(deriv,RIGHT).shift(DOWN*1.5)
        der3 = MathTex(r"=\lambda^2 e^{\lambda x}").next_to(deriv,RIGHT).shift(DOWN*3)
        #self.add(deriv,dereq,der2,der3)
        
        
        self.add(se3,se4p2,ans,step2t,step2)
        self.play
        self.play(Transform(se4p2,sse4p2),Transform(ans,sans),Transform(se3,sse3))
        self.play(FadeOut(step2t),Transform(step2,step3t))
        self.wait()
        self.play(Write(deriv))
        self.wait()
        self.wait()
        self.play(Write(dereq))
        self.wait()
        self.wait()
        self.wait()
        self.play(Write(der2))
        self.wait()
        self.wait()
        self.play(Write(der3))
        self.wait()
        self.wait()
        self.wait()
        self.play(Uncreate(der2),Uncreate(dereq),Uncreate(deriv),Uncreate(step2t),Uncreate(step3t),Uncreate(se3),Uncreate(se4p2),Uncreate(ans))
        self.wait()
        

class scene7test(Scene):
    def construct(self):
        deriv = MathTex(r"\frac{d^2}{dx^2} e^{\lambda x}")
        dereq = MathTex(r"=\frac{d}{dx}(\frac{d}{dx}e^{\lambda x})").next_to(deriv,RIGHT)
        der2 = MathTex(r"=\frac{d}{dx}(\lambda e^{\lambda x)").next_to(deriv,RIGHT).shift(DOWN*1.5)
        der3 = MathTex(r"=\lambda^2 e^{\lambda}{x}").next_to(deriv,RIGHT).shift(DOWN*3)
        self.add(deriv,dereq,der2,der3)

class scene8(Scene):
    def construct(self):
        step3t = Text('Step 3: Calculate the derivative.',font_size=40).shift(UP*2)
        step4t = Text('Step 4: Plug in our solved derivative and solve the TISE',font_size=37).shift(UP*2)
        der3 = MathTex(r"=\lambda^2 e^{\lambda x}").shift(DOWN*2+RIGHT*3.35)
        der3s4 = MathTex(r"\lambda^2 e^{\lambda x}").shift(UP)
        se = MathTex(r"-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} e^{\lambda x} - Ee^{\lambda x} = 0")
        se2 = MathTex(r"-\frac{\hbar^2}{2m}\lambda^2 e^{\lambda x} - Ee^{\lambda x} = 0").shift(UP)
        se3 = MathTex(r"(-\frac{\hbar^2}{2m}\lambda^2-E)e^{\lambda x}=0").shift(DOWN*0.5)
        Since = MathTex(r"e^{\lambda x} \neq 0\: for\: finite\: \lambda").shift(DOWN*2)

         

        Thus = Text("Zeros must come from:",font_size=30).shift(RIGHT*3+UP)
        Poly = MathTex(r"(-\frac{\hbar^2}{2m}\lambda^2-E)=0").shift(RIGHT*3)

        solvefor = MathTex(r"Solving\: for\: \lambda \:gives:",font_size=40).shift(RIGHT*3+DOWN)
        lam = MathTex(r"\pm \lambda = \frac{i \sqrt{E}}{\sqrt{\frac{\hbar^2}{2m}}}").shift(RIGHT*3+DOWN*2.25)
        #o = Text('or',font_size=30).shift(RIGHT+DOWN*4)
        #lam2 = MathTex(r"\lambda = -\frac{i \sqrt{E}}{sqrt{\frac{\hbar^2}{2m}}}").shift(RIGHT*2+DOWN*4.5)

        
        self.add(step3t,der3)
        self.wait()
        self.play(Transform(step3t,step4t))
        self.play(Transform(der3,der3s4))
        self.play(Write(se))
        self.wait()
        self.play(Transform(der3,se2),Transform(se,se2))
        self.wait()
        self.wait()
        self.play(Create(se3))
        self.wait()
        self.wait()
        self.play(Write(Since))
        self.wait()
        self.wait()
        self.remove(der3)
        shiftse2 = MathTex(r"-\frac{\hbar^2}{2m}\lambda^2 e^{\lambda x} - Ee^{\lambda x} = 0").shift(UP).shift(LEFT*3.5)
        shiftse3 = MathTex(r"(-\frac{\hbar^2}{2m}\lambda^2-E)e^{\lambda x}=0").shift(DOWN*0.5).shift(LEFT*3.5)
        shiftsince = MathTex(r"e^{\lambda x} \neq 0\: for\: finite\: \lambda").shift(DOWN*2).shift(LEFT*3.5)
        self.play(Transform(Since,shiftsince), Transform(der3,shiftse2), Transform(se,shiftse2), Transform(se3,shiftse3))
        self.wait()
        self.wait()
        self.play(Write(Thus))
        self.play(Write(Poly))
        self.wait()
        self.play(Write(solvefor))
        self.play(Create(lam))
        self.wait()
        self.wait()
        self.play(Uncreate(Since),Uncreate(der3),Uncreate(se),Uncreate(se3))
        self.wait()
        self.wait()
        shiftThus = Text("Zeros must come from:",font_size=30).shift(UP + LEFT*4.5)
        shiftPoly = MathTex(r"(-\frac{\hbar^2}{2m}\lambda^2-E)=0").shift(LEFT*4.5)
        shiftsolvefor = MathTex(r"Solving\: for\: \lambda \:gives:",font_size=40).shift(DOWN + LEFT*4.5)
        shiftlam = MathTex(r"\pm \lambda = \frac{i \sqrt{E}}{\sqrt{\frac{\hbar^2}{2m}}}").shift(DOWN*2.25 + LEFT*4.5)
        Thus2 = Text("So, our general solution is:",font_size=30).shift(RIGHT*3+UP)
        gensol = MathTex(r"\psi(x) = A'e^{ix \sqrt{2mE/\hbar^2}} + B'e^{-ix \sqrt{2mE/\hbar^2}}").shift(RIGHT*2.5)
        self.play(Transform(Thus,shiftThus),Transform(Poly,shiftPoly),Transform(solvefor,shiftsolvefor),Transform(lam,shiftlam))
        self.play(Write(Thus2))
        self.play(Write(gensol))
        Thus3 = MarkupText(f"Which can be rewritten using <span fgcolor='{YELLOW}'>Euler's identity</span>:",font_size=25).shift(RIGHT*3+DOWN)
        eid = MathTex(r"e^{i\theta}=cos(\theta)+isin(\theta)",color=YELLOW).shift(RIGHT*3+DOWN*2)
        regensol = MathTex(r"\psi(x) = Acos(kx})+Bsin(kx)").shift(DOWN*3+RIGHT*3)
        self.play(Write(Thus3))
        self.play(Write(eid))
        self.play(Write(regensol))
        self.wait()
        self.wait()
        self.play(Uncreate(Thus),Uncreate(Poly),Uncreate(solvefor),Uncreate(lam))
        self.wait()
        self.wait()

    
class scene9(Scene):
    def construct(self):
        step4t = Text('Step 4: Plug in our solved derivative and solve the TISE',font_size=37).shift(UP*2)
        Thus2 = Text("So, our general solution is:",font_size=30).shift(RIGHT*3+UP)
        gensol = MathTex(r"\psi(x) = A'e^{ix \sqrt{2mE/\hbar^2}} + B'e^{-ix \sqrt{2mE/\hbar^2}}").shift(RIGHT*2.5)
        Thus3 = MarkupText(f"Which can be rewritten using <span fgcolor='{YELLOW}'>Euler's identity</span>:",font_size=25).shift(RIGHT*3+DOWN)
        eid = MathTex(r"e^{i\theta}=cos(\theta)+isin(\theta)",color=YELLOW).shift(RIGHT*3+DOWN*2)
        regensol = MathTex(r"\psi(x) = Acos(kx})+Bsin(kx)").shift(DOWN*3+RIGHT*3)    
        sThus2 = Text("General solution:",font_size=30).shift(UP+LEFT*5)
        sgs = MathTex(r"\psi(x) = Acos(kx})+Bsin(kx)").shift(LEFT*1.5)
        where = MathTex(r"k = \sqrt{\frac{2mE}{\hbar^2}}",font_size=40).next_to(sgs,RIGHT*2)
        pscene = Group(Thus2,gensol,Thus3,eid,regensol)
        step5 = Text("Step 5: Apply Boundary Conditions to General Solution",font_size=40).shift(UP*2)

        bc = Text("Wave function must = 0 at the walls of the well. Thus, when x = 0 and x = L:",font_size=30).shift(DOWN)
        bcl1 = MathTex(r"Acos(k\cdot 0)+Bsin(k\cdot 0)=0").shift(DOWN*2+LEFT*3.7)
        bcl2 = MathTex(r"Acos(kL)+Bsin(kL)=0").shift(DOWN*3+LEFT*4)
        l1g = MathTex(r"\Rightarrow A=0").next_to(bcl1,RIGHT)
        l2g = MathTex(r"\Rightarrow Bsin(kL)=0").next_to(bcl2,RIGHT)
        l2g2 = MathTex(r"\Rightarrow sin(kL)=0").next_to(l2g,RIGHT)

        self.add(pscene,step4t)
        self.wait()
        pshift = Group(sThus2,sgs,where)
        self.play(Transform(pscene, pshift),Transform(step4t,step5))
        self.wait()
        self.play(Write(bc))
        self.play(Write(bcl1),Write(bcl2))
        self.wait()
        self.play(Create(l1g))
        self.wait()
        self.wait()
        self.play(Create(l2g))
        self.wait()
        self.play(Create(l2g2))
        self.wait()
      
        
        self.play(pscene.animate.shift(UP*5.5),step4t.animate.shift(UP*5.5),bc.animate.shift(UP*5.5),bcl1.animate.shift(UP*5.5),
            bcl2.animate.shift(UP*5.5),l1g.animate.shift(UP*5.5),l2g.animate.shift(UP*5.5),l2g2.animate.shift(UP*5.5))
        self.wait()
        self.wait()



class scene10(Scene):
    def construct(self):
        
        bcl1 = MathTex(r"Acos(k\cdot 0)+Bsin(k\cdot 0)=0").shift(DOWN*2+LEFT*3.7).shift(UP*5.5)
        bcl2 = MathTex(r"Acos(kL)+Bsin(kL)=0").shift(DOWN*3+LEFT*4).shift(UP*5.5)
        l1g = MathTex(r"\Rightarrow A=0").next_to(bcl1,RIGHT)
        l2g = MathTex(r"\Rightarrow Bsin(kL)=0").next_to(bcl2,RIGHT)
        l2g2 = MathTex(r"\Rightarrow sin(kL)=0").next_to(l2g,RIGHT)

        self.add(bcl1,bcl2,l1g,l2g,l2g2)
        self.wait()

        then = MathTex(r"kL = n\pi").shift(UP+RIGHT*3)
        recall = Text("Thus,",font_size=32).next_to(then, UP+LEFT)
        then2 = MathTex(r"k=n\pi/L").shift(UP+RIGHT*3)
        where2 = Text('Where n = 1,2,3...',font_size=30).next_to(then, DOWN)
        
        self.play(Write(recall))
        self.wait()
        self.play(FadeIn(then, shift = DOWN))
        self.wait()
        self.wait()
        self.play(Transform(then, then2))
        self.play(Create(where2))
        self.wait()

        
        then3s1 = MathTex(r"\sqrt{\frac{2mE}{\hbar^2}}=k").shift(UP*0.5 + LEFT*4)
        so = Text("So...",font_size=30).next_to(then3s1, UP + LEFT*3)
        then3s2 = MathTex(r"\sqrt{\frac{2mE}{\hbar^2}}=n\pi/L").shift(UP*0.8 + LEFT*4)
        then4 = MathTex(r"E = \frac{\hbar^2\pi^2n^2}{2mL^2}", color = BLUE).next_to(then3s1, DOWN).shift(LEFT*0.5)
        wow = Text("Energy is quantized!",font_size = 30, color = BLUE).next_to(then4, RIGHT).shift(RIGHT)
        summ = Text("To summarize:",font_size=30).next_to(then4, UP)
        Soln = MathTex(r"\psi(x)=",r"B",r"sin(\frac{n\pi}{L} x)", color = RED).next_to(then4, DOWN).shift(RIGHT*0.65)
        eigfun = MathTex("\leftarrow Energy\: eigenvalues", color = BLUE).next_to(then4, RIGHT)
        eigval = MathTex("\leftarrow Solution", color = RED).next_to(Soln, RIGHT)

        self.play(Write(so))
        self.play(Write(then3s1))
        self.wait()
        self.wait()
        self.wait()
        self.play(Transform(then3s1,then3s2))
        self.wait()
        self.play(Write(then4))
        self.wait()
        self.play(Write(wow))
        self.wait()
        self.wait()
        self.play(FadeIn(Soln, shift = DOWN))
        self.wait()
        self.play(FadeIn(eigval, shift = RIGHT),Transform(wow,eigfun))
        self.wait()
        self.wait()

        box = SurroundingRectangle(Soln[1], buff=0.075)
        self.play(Create(box))
        B = Text("How do we find B?", font_size = 30, color = YELLOW).next_to(box, DOWN*1.15)
        self.wait()
        self.play(FadeIn(B, shift = DOWN))
        self.wait()
        self.wait()
        self.play(Uncreate(B, shift = DOWN),Uncreate(box))
        self.wait()
        self.wait()


class scene11(Scene):
    def construct(self):

            norm = Text("Step 6: Apply Normalization Condition to obtain B.",font_size=30).shift(UP*3.5)
            ncond = MathTex(r"1 = \int_{0}^{L} \lvert\psi(x)\rvert^2 dx").shift(UP*2.5)
            ncond2 = MathTex(r"= B^2 \int_{0}^{L} sin^2(kx) dx").next_to(ncond, DOWN*1.5)
            ncond3 = MathTex(r"= \frac{B^2}{2} \int_{0}^{L} (1-cos(2kx)) dx").next_to(ncond2, DOWN*1.5)
            ncond4 = MathTex(r"=\frac{B^2}{2} [x-sin(2kx) \bigg\rvert_{0}^{L}").next_to(ncond3, DOWN*1.5)

            self.play(Write(norm))
            self.wait()
            self.play(Write(ncond))
            self.wait()
            self.wait()
            self.play(Write(ncond2))
            self.wait()
            self.wait()
            self.play(Write(ncond3))
            self.wait()
            self.play(Write(ncond4))
            self.wait()

            self.play(FadeOut(ncond),FadeOut(ncond2),FadeOut(ncond3), ncond4.animate.shift(UP*4.5 +LEFT*2.5))


            ncond5 = MathTex(r"\Rightarrow \frac{B^2}{2}(L - \frac{sin(2kL)}{2k})").next_to(ncond4, RIGHT)
            ncond6 = MathTex(r"B = \sqrt{\frac{2}{L - \frac{sin(2kL)}{2k}}}").next_to(ncond4,DOWN)
            L = MathTex(r"Substitute: \:L = \frac{n\pi}{k}").next_to(ncond6,RIGHT).shift(RIGHT*0.5)
            ncond7 = MathTex(r"B = \sqrt{\frac{2}{\frac{n\pi}{k} - \frac{sin(2k \frac{n\pi}{k} )}{2k}}}").next_to(ncond6, DOWN)
            ncond8 = MathTex(r" = \sqrt{\frac{2}{\frac{n\pi}{k} -",r"sin(2\pi n)",r"/2k}}").next_to(ncond7,RIGHT)

            self.wait()
            self.play(Create(ncond5))
            self.wait()
            self.play(Create(ncond6))
            self.wait()
            self.play(Write(L))
            self.wait()
            self.play(Create(ncond7))
            self.wait()
            self.play(Create(ncond8))
            self.wait()
            
            box = SurroundingRectangle(ncond8[1], buff = 0.05)
            but = MathTex(r"sin(2\pi n) = 0, \: for\: n=1,2,3...", color = YELLOW).next_to(box, DOWN)
            self.play(Create(box))
            self.play(Write(but))
            self.wait()
            self.wait()
            self.play(Uncreate(box),Uncreate(but))
            self.wait()

            ncond9 = MathTex(r"= \sqrt{\frac{2}{\frac{n\pi}{k}}}").next_to(ncond7,RIGHT)
            ncond10 = MathTex(r" = \sqrt{\frac{2}{L}}").next_to(ncond7,RIGHT)
            B = MathTex(r"B").next_to(ncond8,LEFT)
            finsol = Text("Our final solution is:", font_size=30).shift(UP)
            finsol2 = MathTex(r"\psi(x)=\sqrt\frac{2}{L} sin(\frac{n\pi x}{L})\:for\: 0 \leq x \geq L").next_to(finsol,DOWN)
            self.play(Transform(ncond8, ncond9))
            self.wait()
            self.wait()
            self.wait()
            self.play(Transform(ncond8,ncond10))
            self.wait()
            self.wait()
            self.play(Uncreate(ncond4),Uncreate(ncond5),Uncreate(ncond6),Uncreate(ncond7),Uncreate(L))
            self.play(Write(B))
            self.wait()
            self.play(FadeOut(B),FadeOut(ncond8), FadeOut(L), FadeOut(norm))
            self.wait()
            self.wait()
            self.play(Write(finsol))
            self.play(Write(finsol2))
            self.wait()

            #self.add(norm, ncond,ncond2,ncond3,ncond4)

class scene12(Scene):
    def construct(self):

            
        finsol = Text("Our final solution is:", font_size=30).shift(UP)
        finsol2 = MathTex(r"\psi(x)=\sqrt\frac{2}{L} sin(\frac{n\pi x}{L})\:for\: 0 \leq x \geq L").next_to(finsol,DOWN)
        finsol3 = MathTex(r"\psi(x)=\sqrt\frac{2}{L} sin(\frac{n\pi x}{L})",color=YELLOW).shift(UP*3.3 + RIGHT*4)
        eigenval = MathTex(r"")
        self.add(finsol,finsol2)
        self.wait()
        self.play(FadeOut(finsol),Transform(finsol2,finsol3))
        self.wait()

        pot = Axes(x_range=[-0.5,2,1], y_range=[-1,10,100], tips = False)
        x_label = pot.get_x_axis_label("x")
        y_label = pot.get_y_axis_label("V(x)")
        a = MathTex('0',color=RED).shift(LEFT*3.4+DOWN*3)
        b = MathTex('L',color=BLUE).shift(RIGHT*1.2+DOWN*3)

        aline = Arrow(start = LEFT*3.6 + DOWN*2.7, end=UP*3+LEFT*3.6, color=RED, stroke_width = 8)
        bline = Arrow(start = RIGHT*1.2 + DOWN*2.7, end = UP*3 + RIGHT*1.2, color=BLUE, stroke_width = 8)
        self.play(Create(pot),Create(x_label),Create(y_label),Create(a),Create(b),Create(aline),Create(bline))

        psi1 = pot.plot(lambda x: np.sin(np.pi*x), x_range=[0,1], color=YELLOW)
        psi2 = pot.plot(lambda x: np.sin(2*np.pi*x), x_range=[0,1], color=YELLOW).shift(UP*1.5)
        psi3 = pot.plot(lambda x: np.sin(3*np.pi*x), x_range=[0,1], color=YELLOW).shift(UP*3)
        psi4 = pot.plot(lambda x: np.sin(4*np.pi*x), x_range=[0,1], color=YELLOW).shift(UP*4.5)
        pl1 = MathTex(r"n=1", color= YELLOW).next_to(psi1,RIGHT)
        pl2 = MathTex(r"n=2", color= YELLOW).next_to(psi2,RIGHT)
        pl3 = MathTex(r"n=3", color= YELLOW).next_to(psi3,RIGHT)
        pl4 = MathTex(r"n=4", color= YELLOW).next_to(psi4,RIGHT)
        self.wait()
        self.wait()
        self.play(Create(psi1))
        self.play(Write(pl1))
        self.play(Create(psi2))
        self.play(Write(pl2))
        self.play(Create(psi3))
        self.play(Write(pl3))
        self.play(Create(psi4))
        self.play(Write(pl4))
        self.wait()
        self.wait()

        ground = Text("Ground State", font_size=25, color = GREEN).next_to(psi1, LEFT)
        excbr = BraceBetweenPoints([-4.25,-1,0],[-4.25,2.1,0], color= GREEN).rotate(PI)
        excited = Text("Excited States",font_size=25, color= GREEN).next_to(psi3, LEFT).shift(LEFT*0.3)

        e1 = MathTex(r"E_1=\hbar^2 \pi^2/2mL^2", color = GREEN, font_size=40).next_to(pl1, RIGHT)
        e2 = MathTex(r"E_2=2 \hbar^2 \pi^2/mL^2", color = GREEN,font_size=40).next_to(pl2, RIGHT)
        e3 = MathTex(r"E_3=9\hbar^2 \pi^2/2mL^2", color = GREEN,font_size=40).next_to(pl3, RIGHT)
        e4 = MathTex(r"E_4=8\hbar^2 \pi^2/mL^2", color = GREEN,font_size=40).next_to(pl4, RIGHT)
        self.play(Write(e1))
        self.play(Write(e2))
        self.play(Write(e3))
        self.play(Write(e4))
        self.wait()
        self.play(Write(ground))
        self.play(Create(excbr))
        self.play(Write(excited))
        self.wait()
        self.wait()

class test(Scene):
    def construct(self):
            gensol = MathTex(r"\psi(x) = Ae^{ix \sqrt{2mE/\hbar^2}} + Be^{-ix \sqrt{2mE/\hbar^2}}").shift(RIGHT*2.5)
            regensol = MathTex(r"\psi(x) = A'cos(x \sqrt{2mE/\hbar^2})+B'sin(x \sqrt{2mE/\hbar^2})").shift(DOWN*2)
                    
            Thus3 = MarkupText(f"Which can be rewritten using <span fgcolor='{YELLOW}'>Euler's identity</span>:",font_size=25).shift(RIGHT*3+DOWN)
            #text = MarkupText(f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED)
            self.add(Thus3)
            #self.add(regensol)

