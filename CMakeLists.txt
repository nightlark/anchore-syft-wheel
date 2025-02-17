cmake_minimum_required(VERSION 3.10)

project(SyftPythonDistributions NONE)

string(TOLOWER "${CMAKE_HOST_SYSTEM_NAME}" OS_NAME)
string(TOLOWER "${CMAKE_HOST_SYSTEM_PROCESSOR}" CPU_NAME)
string(REPLACE "x86_64" "amd64" CPU_NAME "${CPU_NAME}")
string(REPLACE "aarch64" "arm64" CPU_NAME "${CPU_NAME}")
message(STATUS "OS: ${OS_NAME}, CPU: ${CPU_NAME}")

# Check if a specific architecture is requested on macOS
if("${OS_NAME}" STREQUAL "darwin" AND DEFINED CMAKE_OSX_ARCHITECTURES)
  list(LENGTH CMAKE_OSX_ARCHITECTURES ARCH_COUNT)
  if(ARCH_COUNT GREATER 1)
    message(WARNING "Multiple architectures specified in CMAKE_OSX_ARCHITECTURES, using the first one.")
  endif()
  list(GET CMAKE_OSX_ARCHITECTURES 0 CPU_NAME)
  string(TOLOWER "${CPU_NAME}" CPU_NAME)
  string(REPLACE "x86_64" "amd64" CPU_NAME "${CPU_NAME}")
  string(REPLACE "arm64" "arm64" CPU_NAME "${CPU_NAME}")
endif()

set(DL_EXT "tar.gz")
if("${OS_NAME}" STREQUAL "windows")
  set(DL_EXT "zip")
endif()

include(FetchContent)
include(syft_version.cmake)

set(SYFT_INSTALL_DIR ${CMAKE_BINARY_DIR}/syft-install)

FetchContent_Declare(
  syft
  SOURCE_DIR ${SYFT_INSTALL_DIR}
  URL https://github.com/anchore/syft/releases/download/v${SYFT_VERSION}/syft_${SYFT_VERSION}_${OS_NAME}_${CPU_NAME}.${DL_EXT}
  #URL_HASH
  #DOWNLOAD_EXTRACT_TIMESTAMP TRUE
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ""
  INSTALL_COMMAND ""
)
FetchContent_MakeAvailable(syft)

install(PROGRAMS ${SYFT_INSTALL_DIR}/syft${CMAKE_EXECUTABLE_SUFFIX} DESTINATION bin)
