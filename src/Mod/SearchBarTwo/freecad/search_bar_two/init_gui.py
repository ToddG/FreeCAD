import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad.search_bar_two.translate_utils import translate
from freecad. search_bar_two import my_numpy_function

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")
TRANSLATIONSPATH = os.path.join(os.path.dirname(__file__), "resources/translations")

class SearchBarTwo(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """
    MenuText = translate("search_bar_two", "SearchBarTwo")
    ToolTip = translate("search_bar_two", "a simple SearchBarTwo")
    Icon = os.path.join(ICONPATH, "cool.svg")
    toolbox = []

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        # Add translations path
        Gui.addLanguagePath(TRANSLATIONSPATH)
        Gui.updateLocale()

        App.Console.PrintMessage(translate(
            "search_bar_two",
            "Switching to search_bar_two") + "\n")
        App.Console.PrintMessage(translate(
            "search_bar_two",
            "Run a numpy function:") + "sqrt(100) = {}\n".format(my_numpy_function.my_foo(100)))

        self.appendToolbar(translate("Toolbar", "Tools"), self.toolbox)
        self.appendMenu(translate("Menu", "Tools"), self.toolbox)

    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        App.Console.PrintMessage(translate(
            "search_bar_two",
            "Workbench search_bar_two activated.") + "\n")

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        App.Console.PrintMessage(translate(
            "search_bar_two",
            "Workbench search_bar_two de-activated.") + "\n")


Gui.addWorkbench(SearchBarTwo())
