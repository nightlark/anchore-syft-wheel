cmake_minimum_required(VERSION 3.24)

project(SyftPythonDistributions NONE)

string(TOLOWER "${CMAKE_HOST_SYSTEM_NAME}" OS_NAME)
string(TOLOWER "${CMAKE_HOST_SYSTEM_PROCESSOR}" CPU_NAME)
string(REPLACE "x86_64" "amd64" CPU_NAME "${CPU_NAME}")
message(STATUS "OS: ${OS_NAME}, CPU: ${CPU_NAME}")

include(FetchContent)
include(syft_version.cmake)

set(SYFT_INSTALL_DIR ${CMAKE_BINARY_DIR}/syft-install)

FetchContent_Declare(
  syft
  SOURCE_DIR ${SYFT_INSTALL_DIR}
  URL https://github.com/anchore/syft/releases/download/v${SYFT_VERSION}/syft_${SYFT_VERSION}_${OS_NAME}_${CPU_NAME}.tar.gz
  #URL_HASH
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ""
  INSTALL_COMMAND ""
)
FetchContent_MakeAvailable(syft)

install(PROGRAMS ${SYFT_INSTALL_DIR}/syft${CMAKE_EXECUTABLE_SUFFIX} DESTINATION bin)
