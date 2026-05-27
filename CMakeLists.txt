cmake_minimum_required(VERSION 3.16)
project(MLCompiler LANGUAGES C)
set(CMAKE_C_STANDARD 11)
add_executable(mlc src/main.c)

# Testing
enable_testing()

# Unity as a vendored static library
add_library(unity STATIC tests/unity/unity.c)
target_include_directories(unity PUBLIC tests/unity)

# First test executable
add_executable(test_hello tests/test_hello.c)
target_link_libraries(test_hello PRIVATE unity)

# Register with CTest
add_test(NAME hello_test COMMAND test_hello)
