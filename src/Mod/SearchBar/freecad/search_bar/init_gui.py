import FreeCADGui

# -------------------------------------------------------------------------------------
# Avoid garbage collection by storing these in a global variables
# widget action
wax = None
# search box light
sea = None
# toolbar
tbr = None
# -------------------------------------------------------------------------------------


def addToolSearchBox():
    import importlib
    from PySide import QtGui
    from freecad.search_bar import SearchBoxLight
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
        if tbr is None:
            # QtGui.QDockWidget()
            tbr = QtGui.QToolBar("SearchBar")

            # Include FreeCAD in the name so that one can find windows labeled with FreeCAD easily
            # in window managers which allow search through the list of open windows.
            tbr.setObjectName("SearchBar")
            tbr.addAction(wax)
        mw.addToolBar(tbr)
        tbr.show()


addToolSearchBox()
FreeCADGui.getMainWindow().workbenchActivated.connect(addToolSearchBox)
