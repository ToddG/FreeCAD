# import os
# import FreeCADGui as Gui
# import FreeCAD as App
# from freecad.search_bar.translate_utils import translate
# from freecad. search_bar import my_numpy_function
#
# ICONPATH = os.path.join(os.path.dirname(__file__), "resources")
# TRANSLATIONSPATH = os.path.join(os.path.dirname(__file__), "resources/translations")
#
# class SearchBar(Gui.Workbench):
#     """
#     class which gets initiated at startup of the gui
#     """
#     MenuText = translate("search_bar", "SearchBar")
#     ToolTip = translate("search_bar", "a simple SearchBar")
#     Icon = os.path.join(ICONPATH, "cool.svg")
#     toolbox = []
#
#     def GetClassName(self):
#         return "Gui::PythonWorkbench"
#
#     def Initialize(self):
#         """
#         This function is called at the first activation of the workbench.
#         here is the place to import all the commands
#         """
#         # Add translations path
#         Gui.addLanguagePath(TRANSLATIONSPATH)
#         Gui.updateLocale()
#
#         App.Console.PrintMessage(translate(
#             "search_bar",
#             "Switching to search_bar") + "\n")
#         App.Console.PrintMessage(translate(
#             "search_bar",
#             "Run a numpy function:") + "sqrt(100) = {}\n".format(my_numpy_function.my_foo(100)))
#
#         self.appendToolbar(translate("Toolbar", "Tools"), self.toolbox)
#         self.appendMenu(translate("Menu", "Tools"), self.toolbox)
#
#     def Activated(self):
#         '''
#         code which should be computed when a user switch to this workbench
#         '''
#         App.Console.PrintMessage(translate(
#             "search_bar",
#             "Workbench search_bar activated.") + "\n")
#
#     def Deactivated(self):
#         '''
#         code which should be computed when this workbench is deactivated
#         '''
#         App.Console.PrintMessage(translate(
#             "search_bar",
#             "Workbench search_bar de-activated.") + "\n")
#
#
# Gui.addWorkbench(SearchBar())
import importlib

import FreeCADGui
from PySide import QtGui

from freecad.search_bar import SearchBoxLight

# Avoid garbage collection by storing the action in a global variable
wax = None
sea = None
tbr = None


def addToolSearchBox():
    global wax, sea, tbr
    mw = FreeCADGui.getMainWindow()
    if mw:
        if sea is None:
            sea = SearchBoxLight.SearchBoxLight(
                getItemGroups=lambda: importlib.import_module("freecad.search_bar.GetItemGroups").getItemGroups(),
                getToolTip=lambda groupId, setParent: importlib.import_module(
                    "freecad.search_bar.GetItemGroups"
                ).getToolTip(groupId, setParent),
                getItemDelegate=lambda: importlib.import_module(
                    "freecad.search_bar.IndentedItemDelegate"
                ).IndentedItemDelegate(),
            )
            sea.resultSelected.connect(
                lambda index, groupId: importlib.import_module("freecad.search_bar.GetItemGroups").onResultSelected(
                    index, groupId
                )
            )

        if wax is None:
            wax = QtGui.QWidgetAction(None)
            wax.setWhatsThis(
                "Use this search bar to find tools, document objects, preferences and more"
            )

        sea.setWhatsThis(
            "Use this search bar to find tools, document objects, preferences and more"
        )
        wax.setDefaultWidget(sea)
        # mbr.addWidget(sea)
        # mbr.addAction(wax)
        if tbr is None:
            tbr = QtGui.QToolBar("SearchBar")  # QtGui.QDockWidget()
            # Include FreeCAD in the name so that one can find windows labeled with FreeCAD easily
            # in window managers which allow search through the list of open windows.
            tbr.setObjectName("SearchBar")
            tbr.addAction(wax)
        mw.addToolBar(tbr)
        tbr.show()


addToolSearchBox()
FreeCADGui.getMainWindow().workbenchActivated.connect(addToolSearchBox)
