import os
import subprocess

GLFW = "glfw-3.3.4"
GLEW = "glew-2.1.0"

TOP_DIR = os.getcwd()
INSTALL_PREFIX = os.path.abspath(os.path.join(TOP_DIR, "..", "library"))

GLFW_DIR = os.path.join(TOP_DIR, GLFW)
GLEW_DIR = os.path.join(TOP_DIR, GLEW)

#------------------------------------------------------------
# 外部コマンド実行
def Do(cmd):
    command = " ".join(cmd)
    Log("Run: " + command)
    result = subprocess.call(command, shell=True)
    if result != 0:
        Error(command + "  result=" + str(result))

#------------------------------------------------------------
# エラー出力
def Error(msg):
    Log("Error !!! " + msg)
    os.sys.exit(0)

#------------------------------------------------------------
# ログ出力
def Log(msg):
    print("* " + msg)
