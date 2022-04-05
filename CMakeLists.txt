# proje adı
project(Amonia)

# minimum cmake sürümü
cmake_minimum_required(VERSION 3.10)
# compile
add_executable(amonia amonia.cpp source/tools.cpp)
target_compile_options (amonia PRIVATE -std=c++11)
target_compile_definitions (amonia PRIVATE BOOST_ERROR_CODE_HEADER_ONLY)
#target_link_libraries (numb mariadbclientpp)
set(amonia amonia)
set(amonia_VERSION_MAJOR 2)
set(amonia_VERSION_MINOR 0)

include_directories(header/)

message(STATUS "her sey qaydasindadir")

