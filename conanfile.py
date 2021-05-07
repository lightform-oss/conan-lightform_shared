from conans import ConanFile

class LightformShared(object):
    # https://docs.conan.io/en/latest/reference/conanfile/attributes.html#options
    options = {
        "shared": [True, False]
    }

    # https://docs.conan.io/en/latest/reference/conanfile/attributes.html#default-options
    default_options = {
        "shared": False, # Global static/shared setting for this package
        "boost:extra_b2_flags": "cxxstd=14", # this is critical, otherwise parts of boost won't link
        "ffmpeg:decoder_dxv": True,
        "ffmpeg:freetype": False,
        "ffmpeg:lzma": False,
        "ffmpeg:openjpeg": False,
        "ffmpeg:openssl": False,
        "ffmpeg:x265": False,
        "opencv:contrib": True,
        "opencv:dc1394": False,
        "opencv:eigen": False,
        "opencv:freetype": True,
        "opencv:harfbuzz": False,
        "opencv:jpeg": True,
        "opencv:jpegturbo": True,
        "opencv:nonfree": True, #for sift
        "opencv:protobuf": False,
        "opencv:quirc": True,
        "opencv:tiff": False,
        "opencv:webp": False,
    }

    # Platform-dependent requirements / options
    def requirements(self):
        self.requires("boost/1.73.0")
        self.requires("cmake_installer/3.16.2@conan/stable")
        self.requires("ffmpeg/4.2.1@lightform/stable")
        self.requires("grpc/1.25.0@inexorgame/stable")
        self.requires("libcurl/7.67.0")
        self.requires("libjpeg-turbo/2.0.2")
        self.requires("libpng/1.6.37")
        self.requires("opencv/4.5.0@lightform/stable")
        self.requires("openssl/1.0.2t")
        self.requires("protobuf/3.9.1")
        self.requires("rtaudio/5.1.0@lightform/stable")
        self.requires("zlib/1.2.11")

        if self.settings.os == "Windows":
            self.requires("glew/2.1.0@bincrafters/stable")

        if self.settings.os == "Linux":
            self.requires("libunwind/1.3.1@bincrafters/stable") # This should be cross-platform, but the conan recipe only allows linux builds at the moment

        # Overrides: We don't really care, but two things we require specify different versions and we need to pick one
        self.requires("libiconv/1.16")

    def configure(self):
        #self.options["grpc"].shared = self.options.shared # only support static
        self.options["ffmpeg"].shared = self.options.shared
        self.options["opencv"].shared = self.options.shared
        self.options["boost"].shared = self.options.shared
        self.options["libcurl"].shared = self.options.shared
        self.options["protobuf"].shared = self.options.shared
        self.options["openssl"].shared = self.options.shared
        self.options["libjpeg-turbo"].shared = self.options.shared
        self.options["libpng"].shared = self.options.shared
        self.options["zlib"].shared = self.options.shared

        if self.settings.os == "Linux":
            self.options["opencv"].gtk = 3
            self.options["ffmpeg"].alsa = False

class Package(ConanFile):
    name = "lightform_shared"
    version = "0.1"
