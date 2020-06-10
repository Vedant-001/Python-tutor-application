from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty,StringProperty,ListProperty
from kivy.factory import Factory
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.graphics import Color
import random


lesson = 1


class MainWindow(Screen):
    pass


class ContentWindow(Screen):
    global lesson
    def btn1(self):
        global lesson
        if lesson > 1 :
            sm.current = "loop"
        else :
            invalidEntry()

    def btn2(self):
        global lesson
        if lesson > 2 :
            sm.current = "data"
        else :
            invalidEntry()

    def btn3(self):
        global lesson
        if lesson > 3 :
            sm.current = "functions"
        else :
            invalidEntry()

    def btn4(self):
        global lesson
        if lesson > 4 :
            sm.current = "datahandling"
        else :
            invalidEntry()

    def btn5(self):
        global lesson
        if lesson > 5 :
            sm.current = "app"
        else :
            invalidEntry()


class DataWindow(Screen):
    pass


class FunctionWindow(Screen):
    pass



class DataHandlingWindow(Screen):
    pass


class AppWindow(Screen):
    pass

class OperatorWindow(Screen):
    pass

class BasicWindow(Screen):
    pass

class Basic2Window(Screen):
    pass

class Basic3Window(Screen):
    pass


class ArithmaticOperatorWindow(Screen):
    pass


class ConditionalOperatorWindow(Screen):
    pass


class BitwiseOperatorWindow(Screen):
    pass


class AssignmentOperatorWindow(Screen):
    pass


class LogicalOperatorWindow(Screen):
    pass


class IdentityOperatorWindow(Screen):
    def select(self):
        if sel % 3 == 0:
            sm.current = "test1"
        elif sel % 3 == 1:
            sm.current = "test11"
        elif sel % 3 == 2:
            sm.current = "test111"
    pass



class Test1Window(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass

class Test2Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)

    def zero(self):
        global count
        count = 0
        pass


class Test3Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)

    def zero(self):
        global count
        count = 0
        pass


class Test4Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)

    def zero(self):
        global count
        count = 0
        pass



class Test5Window(Screen):

    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
        if lesson > 1:
            counting(count)
        else:
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()

    def zero(self):
        global count
        count = 0
        pass




class Test11Window(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "d" or self.answer.text =="D":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class Test22Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test33Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "d" or self.answer.text == "D":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test44Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "c" or self.answer.text == "C":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test55Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel
        sel = sel + 1
        if self.answer.text == "D" or self.answer.text == "d":
            global count
            count = count + 1
            print(count)
        if lesson > 1:

            counting(count)
        else:
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()
    def zero(self):
        global count
        count = 0
        pass



class Test111Window(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text =="B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class Test222Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)

    def zero(self):
        global count
        count = 0
        pass



class Test333Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test444Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):

        if self.answer.text == "c" or self.answer.text == "C":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test555Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
        if lesson > 1 :

            counting(count)
        else :
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()
    def zero(self):
        global count
        count = 0
        pass


class tTest1Window(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class tTest2Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class tTest3Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class tTest4Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class tTest5Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel,lesson
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
        if lesson > 2:
            counting(count)
        else:
            if count == 4:
                ifpass4()

            elif count == 5:
                ifpass5()

            else:
                iffail()
        count = 0

    def zero(self):
        global count
        count = 0
        pass



class tTest11Window(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text =="B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class tTest22Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class tTest33Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class tTest44Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class tTest55Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count, lesson
            count = count + 1
            print(count)
        if lesson > 2:

            counting(count)
        else:
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()
        count = 0
    def zero(self):
        global count
        count = 0
        pass



class tTest111Window(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text =="B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class tTest222Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class tTest333Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class tTest444Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):

        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class tTest555Window(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel, lesson
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
        if lesson > 2:

            counting(count)
        else :
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()
        count = 0

    def zero(self):
        global count
        count = 0
        pass



class tFinalWindow(Screen):
    def select(self):
        if sel % 3 == 0:
            sm.current = "2test1"
        elif sel % 3 == 1:
            sm.current = "2test11"
        elif sel % 3 == 2:
            sm.current = "2test111"

    pass


class FinalWindow3(Screen):
    def select(self):
        if sel % 3 == 0:
            sm.current = "3test1"
        elif sel % 3 == 1:
            sm.current = "3test11"
        elif sel % 3 == 2:
            sm.current = "3test111"
    pass


class FinalWindow4(Screen):
    def select(self):
        if sel % 3 == 0:
            sm.current = "4test1"
        elif sel % 3 == 1:
            sm.current = "4test11"
        elif sel % 3 == 2:
            sm.current = "4test111"
    pass

class FinalWindow5(Screen):
    def select(self):
        if sel % 3 == 0:
            sm.current = "5test1"
        elif sel % 3 == 1:
            sm.current = "5test11"
        elif sel % 3 == 2:
            sm.current = "5test111"
    pass

class FinalWindow6(Screen):
    def select(self):
        if sel % 3 == 0:
            sm.current = "6test1"
        elif sel % 3 == 1:
            sm.current = "6test11"
        elif sel % 3 == 2:
            sm.current = "6test111"
    pass
class Test1Window3(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class Test2Window3(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test3Window3(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test4Window3(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test5Window3(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel,lesson
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
        if lesson > 3:
            counting(count)
        else:
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()
    def zero(self):
        global count
        count = 0
        pass



class Test11Window3(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):

        if self.answer.text == "d" or self.answer.text =="D":
            global count
            count = count + 1
            print(count)

    def zero(self):

        global count
        count = 0
        pass


class Test22Window3(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test33Window3(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "d" or self.answer.text == "D":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test44Window3(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "c" or self.answer.text == "C":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test55Window3(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel
        sel = sel + 1
        if self.answer.text == "D" or self.answer.text == "d":
            global count
            count = count + 1
            print(count)
        if lesson > 3:

            counting(count)
        else:
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()
    def zero(self):
        global count
        count = 0
        pass



class Test111Window3(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text =="B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class Test222Window3(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test333Window3(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)

    def zero(self):
        global count
        count = 0
        pass



class Test444Window3(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):

        if self.answer.text == "c" or self.answer.text == "C":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test555Window3(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
        if lesson > 3 :

            counting(count)
        else :
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()
    def zero(self):
        global count
        count = 0
        pass


class Test1Window4(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class Test2Window4(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test3Window4(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test4Window4(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test5Window4(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel,lesson
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
        if lesson > 4:
            counting(count)
        else:
            if count == 4:
                ifpass4()

            elif count == 5:
                ifpass5()

            else:
                iffail()
        count = 0

    def zero(self):
        global count
        count = 0
        pass



class Test11Window4(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text =="B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class Test22Window4(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test33Window4(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test44Window4(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test55Window4(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count, lesson
            count = count + 1
            print(count)
        if lesson > 4:

            counting(count)
        else:
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()
        count = 0
    def zero(self):
        global count
        count = 0
        pass



class Test111Window4(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text =="B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class Test222Window4(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test333Window4(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test444Window4(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):

        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test555Window4(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel, lesson
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
        if lesson > 4:

            counting(count)
        else :
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()
        count = 0

    def zero(self):
        global count
        count = 0
        pass


class Test1Window5(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class Test2Window5(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test3Window5(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test4Window5(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test5Window5(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel,lesson
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
        if lesson > 5:
            counting(count)
        else:
            if count == 4:
                ifpass4()

            elif count == 5:
                ifpass5()

            else:
                iffail()
        count = 0

    def zero(self):
        global count
        count = 0
        pass



class Test11Window5(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text =="B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class Test22Window5(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test33Window5(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test44Window5(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test55Window5(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count, lesson
            count = count + 1
            print(count)
        if lesson > 5:

            counting(count)
        else:
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()
        count = 0
    def zero(self):
        global count
        count = 0
        pass



class Test111Window5(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text =="B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class Test222Window5(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test333Window5(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test444Window5(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):

        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test555Window5(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel, lesson
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
        if lesson > 5:

            counting(count)
        else :
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()
        count = 0

    def zero(self):
        global count
        count = 0
        pass

class Test1Window6(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class Test2Window6(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test3Window6(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test4Window6(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test5Window6(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel,lesson
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
        if lesson > 6:
            counting(count)
        else:
            if count == 4:
                ifpass4()

            elif count == 5:
                ifpass5()

            else:
                iffail()
        count = 0

    def zero(self):
        global count
        count = 0
        pass



class Test11Window6(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text =="B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class Test22Window6(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test33Window6(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test44Window6(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test55Window6(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count, lesson
            count = count + 1
            print(count)
        if lesson > 6:

            counting(count)
        else:
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()
        count = 0
    def zero(self):
        global count
        count = 0
        pass



class Test111Window6(Screen):
    answer = ObjectProperty(None)
    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text =="B":
            global count
            count = count + 1

            print(count)
    def zero(self):
        global count
        count = 0
        pass


class Test222Window6(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test333Window6(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        if self.answer.text == "a" or self.answer.text == "A":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass



class Test444Window6(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):

        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
    def zero(self):
        global count
        count = 0
        pass




class Test555Window6(Screen):
    answer = ObjectProperty(None)

    def get_text_inputs(self):
        global sel, lesson
        sel = sel + 1
        if self.answer.text == "b" or self.answer.text == "B":
            global count
            count = count + 1
            print(count)
        if lesson > 6:

            counting(count)
        else :
            if count == 4:
                ifpass4()
            elif count == 5:
                ifpass5()
            else:
                iffail()
        count = 0

    def zero(self):
        global count
        count = 0
        pass


class LoopWindow(Screen):
    pass

class ForLoop(Screen):
    pass


class Forwithelse(Screen):
    pass


class WhileLoop(Screen):
    pass


class WhileWithElse(Screen):
    pass

class IfElse(Screen):
    pass

class TryCatch(Screen):
    pass

class App2Window(Screen):
    pass


class App3Window(Screen):
    pass


class App4Window(Screen):
    pass

class A2Window(Screen):
    pass

class A3Window(Screen):
    pass

class A4Window(Screen):
    pass


class FifthWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


sel = 0
number = 0
count = 0


def counting(count):
    if count == 0:
        pop = Popup(title='Test Over!   : RESULT TIME:- ', content=Label(text='You Scored 0/5\n'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
    elif count == 1:
        pop = Popup(title='Test Over!   : RESULT TIME:- ', content=Label(text='You Scored 1/5\n'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
    elif count == 2:
        pop = Popup(title='Test Over!   : RESULT TIME:- ', content=Label(text='You Scored 2/5\n'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
    elif count == 3:
        pop = Popup(title='Test Over!   : RESULT TIME:- ', content=Label(text='You Scored 3/5\n'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
    elif count == 4:
        pop = Popup(title='Test Over!   : RESULT TIME:- ', content=Label(text='You Scored 4/5\n'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
    elif count == 5:
        pop = Popup(title='Test Over!   : RESULT TIME:- ', content=Label(text='You Scored 5/5\n'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
    sm.current = "content"


def invalidEntry():
    pop = Popup(title='Invalid Entry',content=Label(text='You Need To Complete Previous Lessons\n            To Study This Lesson'),size_hint=(None, None), size=(400, 400))
    pop.open()


def ifpass4() :
    pop = Popup(title='Test Over!   : RESULT TIME:- ',content=Label(text='You Scored 4/5\n\nCongratulations you have passed the test\nYou can now proceed for the futrther Lesson'),size_hint=(None, None), size=(400, 400))
    pop.open()
    global lesson, count
    lesson = lesson + 1
    count = 0


def ifpass5():
    pop = Popup(title='Test Over!   : RESULT TIME:- ',content=Label(text='Wow!!!You Scored 5/5\n\nCongratulations you have passed the test\nYou can now proceed for the futrther Lesson'),size_hint=(None, None), size=(400, 400))
    pop.open()
    global lesson, count
    lesson = lesson + 1
    count = 0


def iffail() :
    pop = Popup(title='Test Over!   : RESULT:- ', content=Label(text='Oops! Sorry you could not clear this lesson\nTry again   BEST OF LUCK!!!'),size_hint=(None, None), size=(400, 400))
    pop.open()
    global count
    count = 0


sm = WindowManager()

kv = Builder.load_file("my.kv")

screens = [App3Window(name="app3"), App2Window(name="app2"), BasicWindow(name="basic"), Basic2Window(name="basic2"),
           Basic3Window(name="basic3"), LogicalOperatorWindow(name="lop"), BitwiseOperatorWindow(name="bop"),
           ConditionalOperatorWindow(name="cop"), ArithmaticOperatorWindow(name="aop"),
           IdentityOperatorWindow(name="iop"), AssignmentOperatorWindow(name="asop"), FifthWindow(name="fifth"),
           OperatorWindow(name="op"), ContentWindow(name="content"), MainWindow(name="main"), Test1Window(name="test1"),
           Test2Window(name="test2"), Test3Window(name="test3"), Test4Window(name="test4"), Test5Window(name="test5"),
           Test11Window(name="test11"), Test22Window(name="test22"), Test33Window(name="test33"),
           Test44Window(name="test44"), Test55Window(name="test55"), Test111Window(name="test111"),
           Test222Window(name="test222"), Test333Window(name="test333"), Test444Window(name="test444"),
           Test555Window(name="test555"), LoopWindow(name="loop"), DataWindow(name="data"),
           DataHandlingWindow(name="datahandling"), FunctionWindow(name="functions"), AppWindow(name="app"),
           tTest1Window(name="2test1"), tTest2Window(name="2test2"), tTest3Window(name="2test3"),
           tTest4Window(name="2test4"), tTest5Window(name="2test5"), tTest11Window(name="2test11"),
           tTest22Window(name="2test22"), tTest33Window(name="2test33"), tTest44Window(name="2test44"),
           tTest55Window(name="2test55"), tTest111Window(name="2test111"), tTest222Window(name="2test222"),
           tTest333Window(name="2test333"), tTest444Window(name="2test444"), tTest555Window(name="2test555"),
           tFinalWindow(name="2final"), Test1Window3(name="3test1"), Test2Window3(name="3test2"),
           Test3Window3(name="3test3"), Test4Window3(name="3test4"), Test5Window3(name="3test5"),
           Test11Window3(name="3test11"), Test22Window3(name="3test22"), Test33Window3(name="3test33"),
           Test44Window3(name="3test44"), Test55Window3(name="3test55"), Test111Window3(name="3test111"),
           Test222Window3(name="3test222"), Test333Window3(name="3test333"), Test444Window3(name="3test444"),
           Test555Window3(name="3test555"), FinalWindow3(name="final3"), Test1Window4(name="4test1"),
           Test2Window4(name="4test2"), Test3Window4(name="4test3"), Test4Window4(name="4test4"),
           Test5Window4(name="4test5"), Test11Window4(name="4test11"), Test22Window4(name="4test22"),
           Test33Window4(name="4test33"), Test44Window4(name="4test44"), Test55Window4(name="4test55"),
           Test111Window4(name="4test111"), Test222Window4(name="4test222"), Test333Window4(name="4test333"),
           Test444Window4(name="4test444"), Test555Window4(name="4test555"), FinalWindow4(name="final4"),
           Test1Window5(name="5test1"), Test2Window5(name="5test2"), Test3Window5(name="5test3"),
           Test4Window5(name="5test4"), Test5Window5(name="5test5"), Test11Window5(name="5test11"),
           Test22Window5(name="5test22"), Test33Window5(name="5test33"), Test44Window5(name="5test44"),
           Test55Window5(name="5test55"), Test111Window5(name="5test111"), Test222Window5(name="5test222"),
           Test333Window5(name="5test333"), Test444Window5(name="5test444"), Test555Window5(name="5test555"),
           FinalWindow5(name="final5"), Test1Window6(name="6test1"), Test2Window6(name="6test2"),
           Test3Window6(name="6test3"), Test4Window6(name="6test4"), Test5Window6(name="6test5"),
           Test11Window6(name="6test11"), Test22Window6(name="6test22"), Test33Window6(name="6test33"),
           Test44Window6(name="6test44"), Test55Window6(name="6test55"), Test111Window6(name="6test111"),
           Test222Window6(name="6test222"), Test333Window6(name="6test333"), Test444Window6(name="6test444"),
           Test555Window6(name="6test555"), FinalWindow6(name="final6"),ForLoop(name="FL"),Forwithelse(name="FWE"),
           WhileLoop(name="While"),WhileWithElse(name="WWE"),IfElse(name="ifelse"),TryCatch(name="TC"),A2Window(name="def2"),
           A3Window(name="def3"),A4Window(name="def4")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"


class MyMainApp(App):
    def build(self):
        return sm




if __name__ == "__main__":
    MyMainApp().run()

