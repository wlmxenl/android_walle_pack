import getpass
import os
import platform
import re
import PackConfig

def getBuildToolsPath(build_tools_version):
    """
    获取 build-tools 目录绝对路径
    :param build_tools_version: 版本号
    :return: str
    """
    if len(build_tools_version) == 0:
        raise AttributeError("buildToolsVersion required")

    build_tools_abs_path = ""
    # windows
    if platform.system() == 'Windows':
        for envItem in os.getenv('PATH').split(";"):
            if envItem.__contains__("platform-tools"):
                sdk_path = os.path.dirname(envItem)
                build_tools_abs_path = os.path.join(sdk_path, "build-tools", build_tools_version)
        pass
    # macos
    elif platform.system() == 'Darwin':
        sdk_path = "/Users/" + getpass.getuser() + "/Library/Android/sdk"
        build_tools_abs_path = os.path.join(sdk_path, "build-tools", build_tools_version)
        pass

    if not os.path.exists(build_tools_abs_path):
        raise FileNotFoundError("build-tools {} not found".format(build_tools_version))

    return build_tools_abs_path


def getSubDirFilePath(dir_name, file_name):
    """
    获取项目指定目录下文件绝对路径
    :param dir_name: 文件夹名
    :param file_name: 文件名
    :return: abs_path
    """
    source_file_path = os.path.join(os.getcwd(), dir_name, file_name)
    if not os.path.exists(source_file_path):
        raise FileNotFoundError(source_file_path)
    return source_file_path


def getProjectDirFilePath(file_name):
    """
    获取项目目录下文件绝对路径
    :param file_name: 文件名
    :return: abs_path
    """
    source_file_path = os.path.join(os.getcwd(), file_name)
    if not os.path.exists(source_file_path):
        raise FileNotFoundError(source_file_path)
    return source_file_path


def deleteFile(file_path):
    """
    删除指定路径文件
    :param file_path: 文件路径
    :return: None
    """
    if os.path.exists(file_path):
        os.remove(file_path)


def getApkVersionName(apk_file_path):
    aapt_path = os.path.join(getBuildToolsPath(PackConfig.sdkBuildToolVersion), 'aapt.exe' if platform.system() == 'Windows' else 'aapt')
    cmd_output = os.popen(f"{aapt_path} dump badging {apk_file_path}").read()
    result = re.findall("versionName='(\S+)'", cmd_output)
    assert len(result) > 0, ValueError('apk versionName is empty.')
    return result[0]

if __name__ == '__main__':
    print(getApkVersionName('source/360.apk'))