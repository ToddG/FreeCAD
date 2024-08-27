set(Namespace_SRCS
        freecad/search_bar/BuiltInSearchResults.py
        freecad/search_bar/GetItemGroups.py
        freecad/search_bar/IndentedItemDelegate.py
        freecad/search_bar/init_gui.py
        freecad/search_bar/__init__.py
        freecad/search_bar/RefreshTools.py
        freecad/search_bar/resources/Tango-System-search.svg
        freecad/search_bar/resources/Tango-System-search.svg.url
        freecad/search_bar/resources/Tango-Tools-spanner-hammer.svg
        freecad/search_bar/resources/Tango-Tools-spanner-hammer.svg.url
        freecad/search_bar/resources/translations/search_bar_es-ES.qm
        freecad/search_bar/resources/translations/search_bar_es-ES.ts
        freecad/search_bar/resources/translations/update_translation.sh
        freecad/search_bar/ResultsDocument.py
        freecad/search_bar/ResultsPreferences.py
        freecad/search_bar/ResultsRefreshTools.py
        freecad/search_bar/ResultsToolbar.py
        freecad/search_bar/SafeViewer.py
        freecad/search_bar/SearchBoxLight.py
        freecad/search_bar/SearchBox.py
        freecad/search_bar/SearchResults.py
        freecad/search_bar/Serialize.py
        freecad/search_bar/translate_utils.py
        freecad/search_bar/version.py
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
