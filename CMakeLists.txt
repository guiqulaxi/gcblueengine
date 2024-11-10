cmake_minimum_required(VERSION 3.5)

project(gcblue)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

# 设置 C++ 标准  
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 设置输出目录（可选）  
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR})

SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR})
# 添加子目录  
add_subdirectory(${PROJECT_SOURCE_DIR}/src/gcb)
add_subdirectory(${PROJECT_SOURCE_DIR}/src/pygcb)
add_subdirectory(${PROJECT_SOURCE_DIR}/src/game)
# add_subdirectory(${PROJECT_SOURCE_DIR}/src/pygame)
add_subdirectory(${PROJECT_SOURCE_DIR}/src/app)

