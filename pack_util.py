import os
import platform


def getBuildToolsPath(build_tools_version):
    """
    获取 build-tools 目录绝对路径
    :param build_tools_version: 版本号
    :return: str
    """
    if len(build_tools_version) == 0:
        raise AttributeError("buildToolsVersion required")

    build_tools_abs_path = ""
    if platform.system() == 'Windows':
        for envItem in os.environ.items():
            if envItem[0] == 'PATH':
                for pathEnvItem in envItem[1].split(";"):
                    if pathEnvItem.__contains__("platform-tools"):
                        sdk_path = os.path.dirname(pathEnvItem)
                        build_tools_abs_path = os.path.join(sdk_path, "build-tools", build_tools_version)
        pass

    if not os.path.exists(build_tools_abs_path):
        raise FileNotFoundError("build-tools {} not found".format(build_tools_version))

    return build_tools_abs_path
