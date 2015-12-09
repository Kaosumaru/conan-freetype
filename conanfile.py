from conans import ConanFile, CMake
from conans import tools
import os

class freetypeConan(ConanFile):
    name = "freetype"
    version = "2.6.2"
    url = "https://github.com/Kaosumaru/conan-freetype"
    settings = "os", "compiler", "build_type", "arch"
    exports = "freetype/*"

    freetype_name = "freetype-%s" % version
    source_tgz = "http://download.savannah.gnu.org/releases/freetype/%s.tar.gz" % freetype_name

    def source(self):
        self.output.info("Downloading %s" % self.source_tgz)
        tools.download(self.source_tgz, "freetype.tar.gz")
        tools.unzip("freetype.tar.gz", ".")
        os.unlink("freetype.tar.gz")

    def config(self):
        pass
        #self.requires.add("zlib/1.2.8@lasote/stable", private=False)
        #self.options["zlib"].shared = False

    def build(self):
        cmake = CMake(self.settings)
        self.run('cd %s && mkdir build' % self.freetype_name)
        self.run('cd %s/build && cmake -DCMAKE_INSTALL_PREFIX:PATH=../../install .. %s' % (self.freetype_name, cmake.command_line))
        self.run("cd %s/build && cmake --build . --target install %s" % (self.freetype_name, cmake.build_config))

    def package(self):
        self.copy("*.h", dst="include", src="install/include/freetype2")
        self.copy("*.lib", dst="lib", src="install/lib")
        self.copy("*.a", dst="lib", src="install/lib")


    def package_info(self):
        self.cpp_info.libs = ["freetype"]
