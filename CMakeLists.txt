SET( PROJECT "hello_cpp" )
SET( YPREFIX "/usr" )

SET( VERSION_MAJOR "0")
SET( VERSION_MINOR "1" )
SET( VERSION_PATCH "0" )
SET( VERSION "${VERSION_MAJOR}.${VERSION_MINOR}.${VERSION_PATCH}${GIT_SHA1_VERSION}" )

SET( SOURCES hello_cpp.cpp )

ADD_DEFINITIONS(-DVERSION="${VERSION}")

project ( ${PROJECT} )
add_executable( ${PROJECT} ${SOURCES} )

install (TARGETS ${PROJECT} DESTINATION bin)