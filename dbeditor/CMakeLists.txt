cmake_minimum_required(VERSION 3.5)

project(dbeditor LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

#find_package(Qt5Core)

include_directories(
    ${PROJECT_SOURCE_DIR}/../include
    ${PROJECT_SOURCE_DIR}/../include/sqlite
    ${PROJECT_SOURCE_DIR}/../3rd/wxWidgets/include
    ${PROJECT_SOURCE_DIR}/../3rd/wxWidgets/include/mswu
    ${PROJECT_SOURCE_DIR}/../include/common
    ${PROJECT_SOURCE_DIR}/../include/database
    ${PROJECT_SOURCE_DIR}/../include/sim
    ${PROJECT_SOURCE_DIR}/../include/scriptinterface
)

# General source files
file(GLOB SOURCE_FILES
  ${PROJECT_SOURCE_DIR}/*.cpp
  )

add_executable(dbeditor
  ${SOURCE_FILES}
)
#target_link_libraries(gcblue Qt5::Core)
