

# General source files
file(GLOB SOURCE_FILES
    ${PROJECT_SOURCE_DIR}/src/gcb/ai/*.cpp
    ${PROJECT_SOURCE_DIR}/src/gcb/common/*.cpp
    ${PROJECT_SOURCE_DIR}/src/gcb/database/*.cpp
    ${PROJECT_SOURCE_DIR}/src/gcb/graphics/*.cpp
    #  ${PROJECT_SOURCE_DIR}/src/gcb/network/*.cpp
    #${PROJECT_SOURCE_DIR}/src/gcb/scriptinterface/*.cpp
    ${PROJECT_SOURCE_DIR}/src/gcb/sim/*.cpp
    ${PROJECT_SOURCE_DIR}/src/gcb/sqlite/*.cpp
    ${PROJECT_SOURCE_DIR}/src/gcb/*.cpp
    ${PROJECT_SOURCE_DIR}/src/gcb/Game.cpp
)
link_directories(
    ${PROJECT_SOURCE_DIR}/3rd/geotiff/lib
    ${PROJECT_SOURCE_DIR}/3rd/tiff/lib
    ${PROJECT_SOURCE_DIR}/3rd/proj/lib
    ${PROJECT_SOURCE_DIR}/3rd/sqlite/lib)

# 添加  动态库，并链接 common 库（如果需要）
add_library(gcb SHARED ${SOURCE_FILES})
# 设置头文件目录  
target_include_directories(gcb PUBLIC
    ${PROJECT_SOURCE_DIR}/include/gcb
    ${PROJECT_SOURCE_DIR}/include/gcb/ai
    ${PROJECT_SOURCE_DIR}/include/gcb/common
    ${PROJECT_SOURCE_DIR}/include/gcb/database
    ${PROJECT_SOURCE_DIR}/include/gcb/sim


)
target_include_directories(gcb PRIVATE
    ${PROJECT_SOURCE_DIR}/include/gcb/graphics
    ${PROJECT_SOURCE_DIR}/include/gcb/sqlite
    ${PROJECT_SOURCE_DIR}/3rd/Eigen
    ${PROJECT_SOURCE_DIR}/3rd/sqlite/include
    ${PROJECT_SOURCE_DIR}/3rd/date/include
    ${PROJECT_SOURCE_DIR}/3rd/httplib/include
    ${PROJECT_SOURCE_DIR}/3rd/cmdline/include
    ${PROJECT_SOURCE_DIR}/3rd/geotiff/include
    ${PROJECT_SOURCE_DIR}/3rd/tiff/include
    ${PROJECT_SOURCE_DIR}/3rd/proj/include
    ${PROJECT_SOURCE_DIR}/3rd/rapidjson/include

)
target_compile_options(gcb
    PRIVATE
    $<$<CXX_COMPILER_ID:MSVC>:/bigobj>
    $<$<AND:$<CXX_COMPILER_ID:GNU>,$<BOOL:${GNU_BIG_OBJ_FLAG_ENABLE}>>:-Wa,-mbig-obj>
    )


target_link_libraries(gcb PRIVATE libgeotiff libtiff libproj sqlite3)
# target_link_libraries(lib2 PRIVATE common) # 如果需要链接 common  

# 安装头文件和库（可选）  
#install(TARGETS lib2 LIBRARY DESTINATION lib)  
#install(FILES ${CMAKE_SOURCE_DIR}/include/lib2/lib2.h DESTINATION include/lib2)
