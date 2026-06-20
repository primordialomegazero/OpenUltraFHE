cmake_minimum_required(VERSION 3.16)
project(OpenUltraFHE VERSION 1.2.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(SEAL REQUIRED)
find_library(OQS_LIB oqs PATHS /usr/local/lib)
find_path(OQS_INC oqs/oqs.h PATHS /usr/local/include)

add_executable(openultrafhe_mirror openultrafhe_mirror.cpp)
target_include_directories(openultrafhe_mirror PRIVATE ${OQS_INC})
target_link_libraries(openultrafhe_mirror SEAL::seal ${OQS_LIB})
