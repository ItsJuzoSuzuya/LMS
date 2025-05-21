cmake_minimum_required(VERSION 3.14)
project(db)

set(CMAKE_CXX_STANDARD 20)

# Set exe output to root dir
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR})


find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(PostgreSQL REQUIRED)
add_subdirectory(external/pybind11)

pybind11_add_module(db src/db.cpp)

find_library(PQ_LIB pq REQUIRED)
target_link_libraries(db PRIVATE pq)
target_include_directories(db PRIVATE ${Python3_INCLUDE_DIRS})
