# set(PYTHON_EXECUTABLE "C:/Users/93551/.conda/envs/test_pybind11/python.exe")
# set(PYTHON_INCLUDE_DIR "C:/Users/93551/.conda/envs/test_pybind11/include")
# set(PYTHON_LIBRARY "C:/Users/93551/.conda/envs/test_pybind11/libs")
# set(pybind11_DIR "C:/Users/93551/.conda/envs/test_pybind11/Lib/site-packages/pybind11/share/cmake/pybind11")

# include_directories(${PYTHON_INCLUDE_DIR})
# link_directories(${PYTHON_LIBRARY})
# find_package(Python REQUIRED)
# find_package(pybind11 REQUIRED)


# General source files
file(GLOB SOURCE_FILES
  ${PROJECT_SOURCE_DIR}/src/app/*.cpp
  )
if(CMAKE_COMPILER_IS_GNUCXX)
    #检查GNU是否支持-Wa,-mbig-obj
    include(CheckCXXCompilerFlag)
    check_cxx_compiler_flag("-Wa,-mbig-obj" GNU_BIG_OBJ_FLAG_ENABLE)
    message(STATUS GNU_BIG_OBJ_FLAG_ENABLE=${GNU_BIG_OBJ_FLAG_ENABLE})
endif()
add_executable(app
  ${SOURCE_FILES}
)
target_include_directories(app PRIVATE
    ${PROJECT_SOURCE_DIR}/include/ai
    ${PROJECT_SOURCE_DIR}/include/common
    ${PROJECT_SOURCE_DIR}/include/database
    ${PROJECT_SOURCE_DIR}/include/scriptinterface
    ${PROJECT_SOURCE_DIR}/include/sim
    ${PROJECT_SOURCE_DIR}/include/sqlite
    ${PROJECT_SOURCE_DIR}/include
    ${PROJECT_SOURCE_DIR}/include/game
    ${PROJECT_SOURCE_DIR}/3rd/Eigen
    ${PROJECT_SOURCE_DIR}/3rd/pybind11/include
    ${PROJECT_SOURCE_DIR}/3rd/sqlite/include
    ${PROJECT_SOURCE_DIR}/3rd/date/include
    ${PROJECT_SOURCE_DIR}/3rd/rapidjson/include
    ${PROJECT_SOURCE_DIR}/3rd/httplib/include
    ${PROJECT_SOURCE_DIR}/3rd/cmdline/include
)
target_compile_options(app
    PRIVATE
    $<$<CXX_COMPILER_ID:MSVC>:/bigobj>
    $<$<AND:$<CXX_COMPILER_ID:GNU>,$<BOOL:${GNU_BIG_OBJ_FLAG_ENABLE}>>:-Wa,-mbig-obj>
    )
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR})
target_link_libraries(app  gcb pygcb game
$<$<BOOL:${MINGW}>:ws2_32>)
