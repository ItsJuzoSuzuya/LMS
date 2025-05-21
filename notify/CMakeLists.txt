cmake_minimum_required(VERSION 3.14)
project(ntfy)

set(CMAKE_CXX_STANDARD 20)
set(CPR_BUILD_SHARED_LIBS OFF)  

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR})

include_directories(/usr/local/include)  
link_directories(/usr/local/lib)


find_package(PostgreSQL REQUIRED)

add_executable(MyNotificationServer main.cpp)

target_link_libraries(MyNotificationServer PRIVATE cpr ${PostgreSQL_LIBRARIES})
target_include_directories(MyNotificationServer PRIVATE ${PostgreSQL_INCLUDE_DIRS})
