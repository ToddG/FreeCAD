from freecad.search_bar import SearchResults

globalGroups = []

itemGroups = None
serializedItemGroups = None


def onResultSelected(index, groupId):
    global globalGroups
    nfo = globalGroups[groupId]
    handlerName = nfo["action"]["handler"]
    if handlerName in SearchResults.actionHandlers:
        SearchResults.actionHandlers[handlerName](nfo)
    else:
        from PySide import QtGui
        print(f"handlername note found: {handlerName}, SearchResults.actionHandlers: {SearchResults.actionHandlers}")

        QtGui.QMessageBox.warning(
            None,
            "Could not execute this action",
            "Could not execute this action, it could be from a Mod that has been uninstalled. "
            "Try refreshing the list of tools.",
        )


def getToolTip(groupId, setParent):
    global globalGroups
    nfo = globalGroups[int(groupId)]
    handlerName = nfo["action"]["handler"]
    if handlerName in SearchResults.toolTipHandlers:
        return SearchResults.toolTipHandlers[handlerName](nfo, setParent)
    else:
        print(f"handlerName note found: {handlerName}, SearchResults.toolTipHandlers: {SearchResults.toolTipHandlers}")
        return (
            "Could not load tooltip for this tool, it could be from a Mod that has been uninstalled. "
            "Try refreshing the list of tools."
        )


def getItemGroups():
    global itemGroups, serializedItemGroups, globalGroups

    # Import the tooltip+action handlers and search result providers that are bundled with this Mod.
    # Other providers should import SearchResults and register their handlers and providers
    # import BuiltInSearchResults

    # Load the list of tools, preferably from the cache, if it has not already been loaded:
    if itemGroups is None:
        if serializedItemGroups is None:
            from freecad.search_bar import RefreshTools

            itemGroups = RefreshTools.refreshToolbars(doLoadAllWorkbenches=False)
        else:
            from freecad.search_bar import Serialize

            itemGroups = Serialize.deserialize(serializedItemGroups)

    # Aggregate the tools (cached) and document objects (not cached), and assign an index to each
    igs = itemGroups
    for providerName, provider in SearchResults.resultProvidersUncached.items():
        igs = igs + provider()
    globalGroups = []

    def addId(group):
        globalGroups.append(group)
        group["id"] = len(globalGroups) - 1
        for subitem in group["subitems"]:
            addId(subitem)

    for ig in igs:
        addId(ig)

    return igs
