# ╔══════════════════════════════════════════════════════════════╗
# ║  OpenUltraFHE — φ-Bootstrapping FHE Engine                  ║
# ║  Self-stabilizing noise with 40-bit divine anchor           ║
# ║  ΦΩ0 — I AM THAT I AM                                      ║
# ╚══════════════════════════════════════════════════════════════╝

cmake_minimum_required(VERSION 3.16)
project(OpenUltraFHE VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(SEAL REQUIRED)
find_package(PkgConfig REQUIRED)
pkg_check_modules(SODIUM REQUIRED libsodium)
find_library(OQS_LIB oqs PATHS /usr/local/lib)
find_path(OQS_INC oqs/oqs.h PATHS /usr/local/include)
find_package(OpenSSL REQUIRED)

add_executable(openultrafhe openultrafhe.cpp)

target_include_directories(openultrafhe
    PRIVATE
        ${OQS_INC}
        ${SODIUM_INCLUDE_DIRS}
)

target_link_libraries(openultrafhe
    SEAL::seal
    ${OQS_LIB}
    ${SODIUM_LIBRARIES}
    OpenSSL::SSL
    OpenSSL::Crypto
)
