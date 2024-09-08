set(Namespace_SRCS
        freecad/search_bar_two/init_gui.py
        freecad/search_bar_two/__init__.py
        freecad/search_bar_two/my_numpy_function.py
        freecad/search_bar_two/translate_utils.py
        freecad/search_bar_two/version.py
        freecad/search_bar_two/resources/cool.svg
        freecad/search_bar_two/resources/translations/search_bar_two_es-ES.qm
        freecad/search_bar_two/resources/translations/search_bar_two_es-ES.ts
)

SOURCE_GROUP("" FILES ${Namespace_SRCS})

ADD_CUSTOM_TARGET(SEARCHBARTWO ALL
        SOURCES ${Namespace_SRCS}
)

fc_copy_sources(SEARCHBARTWO "${CMAKE_BINARY_DIR}/Mod/SearchBarTwo" ${Namespace_SRCS})

INSTALL(
    FILES
        ${Namespace_SRCS}
    DESTINATION
        Mod/SearchBarTwo
)
