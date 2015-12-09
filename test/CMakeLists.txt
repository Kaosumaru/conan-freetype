PROJECT(fttest)
cmake_minimum_required(VERSION 3.0)

include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

ADD_EXECUTABLE(fttest fttest.cpp)

TARGET_LINK_LIBRARIES(fttest ${CONAN_LIBS})
