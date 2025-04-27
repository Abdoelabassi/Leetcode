# steup project
cmake_minimum_required(VERSION 3.16...3.21)
project(dsa)

include_directories(${PROJECT_SOURCE_DIR}/include)
file(GLOB sources ${PROJECT_SOURCE_DIR}/src/*.cc)
file(GLOB headers ${PROJECT_SOURCE_DIR}/include/*.hh)

add_executable(dsa dsa.cc ${sources} ${headers})

install(TARGETS dsa DESTINATION bin)