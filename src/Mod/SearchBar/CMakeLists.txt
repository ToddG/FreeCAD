set(Namespace_SRCS
    freecad/search_bar/animAopt.gif
    freecad/search_bar/animB2op.gif
    freecad/search_bar/BuiltInSearchResults.py
    freecad/search_bar/GetItemGroups.py
    freecad/search_bar/IndentedItemDelegate.py
    freecad/search_bar/InitGui.py
    freecad/search_bar/Init.py
    freecad/search_bar/LICENSE
    freecad/search_bar/package.xml
    freecad/search_bar/README.md
    freecad/search_bar/RefreshTools.py
    freecad/search_bar/ResultsDocument.py
    freecad/search_bar/ResultsPreferences.py
    freecad/search_bar/ResultsRefreshTools.py
    freecad/search_bar/ResultsToolbar.py
    freecad/search_bar/SafeViewer.py
    freecad/search_bar/screenshot.png
    freecad/search_bar/SearchBoxLight.py
    freecad/search_bar/SearchBox.py
    freecad/search_bar/SearchResults.py
    freecad/search_bar/Serialize.py
    freecad/search_bar/Tango-System-search.svg
    freecad/search_bar/Tango-Tools-spanner-hammer.svg
)



SOURCE_GROUP("" FILES ${Namespace_SRCS})

ADD_CUSTOM_TARGET(SEARCHBAR ALL
        SOURCES ${Namespace_SRCS}
)

fc_copy_sources(SEARCHBAR "${CMAKE_BINARY_DIR}/Mod/SearchBar" ${Namespace_SRCS})

INSTALL(
    FILES
        ${Namespace_SRCS}
    DESTINATION
        Mod/SearchBar
)
