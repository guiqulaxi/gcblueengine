set(PYTHON_EXECUTABLE "C:/Users/93551/.conda/envs/test_pybind11/python.exe")
set(PYTHON_INCLUDE_DIR "C:/Users/93551/.conda/envs/test_pybind11/include")
set(PYTHON_LIBRARY "C:/Users/93551/.conda/envs/test_pybind11/libs")
set(pybind11_DIR "C:/Users/93551/.conda/envs/test_pybind11/Lib/site-packages/pybind11/share/cmake/pybind11")
link_directories(${PYTHON_LIBRARY})
find_package(Python REQUIRED)
find_package(pybind11 REQUIRED)

# General source files
file(GLOB SOURCE_FILES
  ${PROJECT_SOURCE_DIR}/src/pygame/*.cpp
  )

# 添加  动态库，并链接 gcb 库（如果需要）
add_library(pygame SHARED ${SOURCE_FILES})
target_link_libraries(pygame PRIVATE game )
target_link_libraries(pygame PRIVATE python3.lib python312.lib $<$<BOOL:${MINGW}>:ws2_32>)
# 设置头文件目录  
target_include_directories(pygame PRIVATE
    ${PROJECT_SOURCE_DIR}/include/game
    # ${PROJECT_SOURCE_DIR}/include/pygcb
    # ${PROJECT_SOURCE_DIR}/include/gcb
    # ${PROJECT_SOURCE_DIR}/include/gcb/ai
    # ${PROJECT_SOURCE_DIR}/include/gcb/common
    # ${PROJECT_SOURCE_DIR}/include/gcb/database
     ${PROJECT_SOURCE_DIR}/include/gcb/sim
    # ${PROJECT_SOURCE_DIR}/include/gcb/graphics
    # ${PROJECT_SOURCE_DIR}/include/gcb/sqlite
    # ${PROJECT_SOURCE_DIR}/3rd/Eigen
    # ${PROJECT_SOURCE_DIR}/3rd/sqlite/include
    # ${PROJECT_SOURCE_DIR}/3rd/date/include
    # ${PROJECT_SOURCE_DIR}/3rd/rapidjson/include
    ${PYTHON_INCLUDE_DIR}
)
target_include_directories(pygame PUBLIC
    ${PROJECT_SOURCE_DIR}/include/pygame
)
target_compile_options(pygame
    PRIVATE
    $<$<CXX_COMPILER_ID:MSVC>:/bigobj>
    $<$<AND:$<CXX_COMPILER_ID:GNU>,$<BOOL:${GNU_BIG_OBJ_FLAG_ENABLE}>>:-Wa,-mbig-obj>
    )
# 后缀名改成pyd能够被python引用,且要去除lib前缀
set_target_properties(pygame PROPERTIES PREFIX "" SUFFIX ".pyd")
# 安装头文件和库（可选）  
#install(TARGETS pygcb LIBRARY DESTINATION lib)  
#install(FILES ${CMAKE_SOURCE_DIR}/include/lib2/lib2.h DESTINATION include/lib2)
