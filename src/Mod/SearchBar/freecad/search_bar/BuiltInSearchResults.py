# You can add your own result providers and action/tooltip handlers, by
# importing this module and calling the registration functions as follows.  We
# use wrapper functions which import the actual implementation and call it, in
# order to avoid loading too much code during startup.
import importlib

from freecad.search_bar import SearchResults

SearchResults.registerResultProvider(
    "refreshTools",
    getItemGroupsCached=lambda: importlib.import_module(
        "freecad.search_bar.ResultsRefreshTools"
    ).refreshToolsResultsProvider(),
    getItemGroupsUncached=lambda: [],
)
SearchResults.registerResultProvider(
    "document",
    getItemGroupsCached=lambda: [],
    getItemGroupsUncached=lambda: importlib.import_module(
        "freecad.search_bar.ResultsDocument"
    ).documentResultsProvider(),
)
SearchResults.registerResultProvider(
    "toolbar",
    getItemGroupsCached=lambda: importlib.import_module("freecad.search_bar.ResultsToolbar").toolbarResultsProvider(),
    getItemGroupsUncached=lambda: [],
)
SearchResults.registerResultProvider(
    "param",
    getItemGroupsCached=lambda: importlib.import_module("freecad.search_bar.ResultsPreferences").paramResultsProvider(),
    getItemGroupsUncached=lambda: [],
)

SearchResults.registerResultHandler(
    "refreshTools",
    action=lambda nfo: importlib.import_module("freecad.search_bar.ResultsRefreshTools").refreshToolsAction(nfo),
    toolTip=lambda nfo, setParent: importlib.import_module(
        "freecad.search_bar.ResultsRefreshTools"
    ).refreshToolsToolTip(nfo, setParent),
)
SearchResults.registerResultHandler(
    "toolbar",
    action=lambda nfo: importlib.import_module("freecad.search_bar.ResultsToolbar").toolbarAction(nfo),
    toolTip=lambda nfo, setParent: importlib.import_module("freecad.search_bar.ResultsToolbar").toolbarToolTip(
        nfo, setParent
    ),
)
SearchResults.registerResultHandler(
    "tool",
    action=lambda nfo: importlib.import_module("freecad.search_bar.ResultsToolbar").subToolAction(nfo),
    toolTip=lambda nfo, setParent: importlib.import_module("freecad.search_bar.ResultsToolbar").subToolToolTip(
        nfo, setParent
    ),
)
SearchResults.registerResultHandler(
    "subTool",
    action=lambda nfo: importlib.import_module("freecad.search_bar.ResultsToolbar").subToolAction(nfo),
    toolTip=lambda nfo, setParent: importlib.import_module("freecad.search_bar.ResultsToolbar").subToolToolTip(
        nfo, setParent
    ),
)
SearchResults.registerResultHandler(
    "document",
    action=lambda nfo: importlib.import_module("freecad.search_bar.ResultsDocument").documentAction(nfo),
    toolTip=lambda nfo, setParent: importlib.import_module("freecad.search_bar.ResultsDocument").documentToolTip(
        nfo, setParent
    ),
)
SearchResults.registerResultHandler(
    "documentObject",
    action=lambda nfo: importlib.import_module("freecad.search_bar.ResultsDocument").documentObjectAction(nfo),
    toolTip=lambda nfo, setParent: importlib.import_module("freecad.search_bar.ResultsDocument").documentObjectToolTip(
        nfo, setParent
    ),
)
SearchResults.registerResultHandler(
    "param",
    action=lambda nfo: importlib.import_module("freecad.search_bar.ResultsPreferences").paramAction(nfo),
    toolTip=lambda nfo, setParent: importlib.import_module("freecad.search_bar.ResultsPreferences").paramToolTip(
        nfo, setParent
    ),
)
SearchResults.registerResultHandler(
    "paramGroup",
    action=lambda nfo: importlib.import_module("freecad.search_bar.ResultsPreferences").paramGroupAction(nfo),
    toolTip=lambda nfo, setParent: importlib.import_module("freecad.search_bar.ResultsPreferences").paramGroupToolTip(
        nfo, setParent
    ),
)
