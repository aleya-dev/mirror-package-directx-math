from conan import ConanFile
from conan.tools.files import copy, mkdir
import os


required_conan_version = ">=2.0"


class DirectXMathConan(ConanFile):
    name = "directx-math"
    version = "feb2024b"

    exports_sources = "source/Inc/*"
    no_copy_source = True

    def package(self):
        source_dir = os.path.join(self.source_folder, "source", "Inc")
        include_dir = os.path.join(self.package_folder, "include")

        mkdir(self, include_dir)
        copy(self, "*", source_dir, include_dir)

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "directxmath")

        self.cpp_info.components["directxmath"].libs = []
        self.cpp_info.components["directxmath"].set_property("cmake_target_name", "Microsoft::DirectXMath")
        self.cpp_info.components["directxmath"].includedirs = ["include"]
        self.cpp_info.components["directxmath"].bindirs = []
        self.cpp_info.components["directxmath"].libdirs = []
