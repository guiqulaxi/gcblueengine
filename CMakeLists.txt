cmake_minimum_required(VERSION 3.5)

project(gcblue)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(PYTHON_EXECUTABLE "C:/Users/93551/.conda/envs/test_pybind11/python.exe")
set(PYTHON_INCLUDE_DIR "C:/Users/93551/.conda/envs/test_pybind11/include")
set(PYTHON_LIBRARY "C:/Users/93551/.conda/envs/test_pybind11/libs")
set(pybind11_DIR "C:/Users/93551/.conda/envs/test_pybind11/Lib/site-packages/pybind11/share/cmake/pybind11")

include_directories(${PYTHON_INCLUDE_DIR})
link_directories(${PYTHON_LIBRARY})
find_package(Python REQUIRED)
find_package(pybind11 REQUIRED)

# find_package(Qt6Core)
# find_package(Qt6Network)
# find_package(Qt6Gui)

include_directories(
    ${PROJECT_SOURCE_DIR}/include/ai
    ${PROJECT_SOURCE_DIR}/include/common
    ${PROJECT_SOURCE_DIR}/include/database
    ${PROJECT_SOURCE_DIR}/include/graphics
#    ${PROJECT_SOURCE_DIR}/include/network
    ${PROJECT_SOURCE_DIR}/include/scriptinterface
    ${PROJECT_SOURCE_DIR}/include/sim
    ${PROJECT_SOURCE_DIR}/include/sqlite
    ${PROJECT_SOURCE_DIR}/include
#    ${PROJECT_SOURCE_DIR}/3rd/wxWidgets/include
#    ${PROJECT_SOURCE_DIR}/3rd/wxWidgets/include/mswu
    ${PROJECT_SOURCE_DIR}/3rd/Eigen
    ${PROJECT_SOURCE_DIR}/3rd/pybind11/include
    ${PROJECT_SOURCE_DIR}/3rd/sqlite/include
    ${PROJECT_SOURCE_DIR}/3rd/date/include
    ${PROJECT_SOURCE_DIR}/3rd/nlohmann/include
    ${PROJECT_SOURCE_DIR}/3rd/httplib/include
    C:/ProgramData/anaconda3/include
)

# General source files
file(GLOB SOURCE_FILES
  ${PROJECT_SOURCE_DIR}/src/ai/*.cpp
  ${PROJECT_SOURCE_DIR}/src/common/*.cpp
  ${PROJECT_SOURCE_DIR}/src/database/*.cpp
  ${PROJECT_SOURCE_DIR}/src/graphics/*.cpp
#  ${PROJECT_SOURCE_DIR}/src/network/*.cpp
  ${PROJECT_SOURCE_DIR}/src/scriptinterface/*.cpp
  ${PROJECT_SOURCE_DIR}/src/sim/*.cpp
  ${PROJECT_SOURCE_DIR}/src/sqlite/*.cpp
  ${PROJECT_SOURCE_DIR}/src/*.cpp
  ${PROJECT_SOURCE_DIR}/3rd/sqlite/src/*.c
  )
if(CMAKE_COMPILER_IS_GNUCXX)
    #检查GNU是否支持-Wa,-mbig-obj
    include(CheckCXXCompilerFlag)
    check_cxx_compiler_flag("-Wa,-mbig-obj" GNU_BIG_OBJ_FLAG_ENABLE)
    message(STATUS GNU_BIG_OBJ_FLAG_ENABLE=${GNU_BIG_OBJ_FLAG_ENABLE})
endif()
add_executable(gcblue
  main.cpp
  ${SOURCE_FILES}
)
target_compile_options(gcblue
    PRIVATE
    $<$<CXX_COMPILER_ID:MSVC>:/bigobj>
    $<$<AND:$<CXX_COMPILER_ID:GNU>,$<BOOL:${GNU_BIG_OBJ_FLAG_ENABLE}>>:-Wa,-mbig-obj>
    )
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR})
# wxWidgets
# 配置wxWidgets库地址，用于find_package
#set(wxWidgets_ROOT_DIR ${PROJECT_SOURCE_DIR}/3rd/wxWidgets)
#set(wxWidgets_LIB_DIR ${PROJECT_SOURCE_DIR}/3rd/wxWidgets/lib)
target_link_libraries(gcblue  python3.lib python312.lib
$<$<BOOL:${MINGW}>:ws2_32>)
#target_link_libraries(gcblue  python3.lib python312.lib ${wxWidgets_LIBRARIES})
# target_link_libraries(gcblue Qt6::Core Qt6::Network Qt6::Gui)
