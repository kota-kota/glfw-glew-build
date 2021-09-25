import os
import shutil
import common as cmn

# Visual Studio
PROGRAM_FILES = os.environ.get("PROGRAMFILES(X86)")
VC_DIR = os.path.join(PROGRAM_FILES, "Microsoft Visual Studio 14.0", "VC")
VC_BIN_DIR = os.path.join(VC_DIR, "bin")
VCVARSALL_BAT = "\"" + os.path.join(VC_DIR, "vcvarsall.bat") + "\""

# Install path
INSTALL_PREFIX_OS = os.path.join(cmn.INSTALL_PREFIX, "windows")

def main():
  cmn.Log("Start " + __file__)
  cmn.Log("INSTALL_PREFIX_OS: " + INSTALL_PREFIX_OS)
  Build_glfw("x86", "Debug")
  Build_glfw("x86", "Release")
  Build_glfw("x64", "Debug")
  Build_glfw("x64", "Release")
  Build_glew("x86", "Debug")
  Build_glew("x86", "Release")
  Build_glew("x64", "Debug")
  Build_glew("x64", "Release")

#------------------------------------------------------------
# glfwビルド
#    host       "x86" or "x64"
#    build_type "Debug" or "Release"
def Build_glfw(host, build_type):
  cmn.Log("Build glfw host=" + host + " build_type=" + build_type)
  INSTALL_PREFIX = os.path.join(INSTALL_PREFIX_OS, host, build_type)
  os.chdir(cmn.GLFW_DIR)
  shutil.rmtree("build", ignore_errors=True)
  os.makedirs("build", exist_ok=True)
  os.chdir("build")
  # cmake generator
  cmd = ["cmake -G \"Visual Studio 16 2019\""]
  if host == "x86":
    cmd += ["-A Win32"]
  else:
    cmd += ["-A x64"]
  cmd += ["-DCMAKE_INSTALL_PREFIX=" + INSTALL_PREFIX]
  cmd += ["-DBUILD_SHARED_LIBS=ON"]
  cmd += [".."]
  cmn.Do(cmd)
  # cmake build
  cmd = ["cmake --build ."]
  cmd += ["--config " + build_type]
  cmd += ["--target INSTALL"]
  cmn.Do(cmd)

#------------------------------------------------------------
# glewビルド
#    host       "x86" or "x64"
#    build_type "Debug" or "Release"
def Build_glew(host, build_type):
  cmn.Log("Build glew host=" + host + " build_type=" + build_type)
  INSTALL_PREFIX = os.path.join(INSTALL_PREFIX_OS, host, build_type)
  os.chdir(cmn.GLEW_DIR)
  shutil.rmtree("build_win", ignore_errors=True)
  os.makedirs("build_win", exist_ok=True)
  os.chdir("build_win")
  # cmake generator
  cmd = ["cmake -G \"Visual Studio 16 2019\""]
  if host == "x86":
    cmd += ["-A Win32"]
  else:
    cmd += ["-A x64"]
  cmd += ["-DCMAKE_INSTALL_PREFIX=" + INSTALL_PREFIX]
  cmd += [os.path.join("..", "build", "cmake")]
  cmn.Do(cmd)
  # cmake build
  cmd = ["cmake --build ."]
  cmd += ["--config " + build_type]
  cmd += ["--target INSTALL"]
  cmn.Do(cmd)

if __name__ == '__main__':
    main()
