#!/usr/bin/python
# -*-coding:utf-8-*-

import os
import re
import PackConfig
import PackUtils

# config
buildToolsPath = PackUtils.getBuildToolsPath(PackConfig.sdkBuildToolVersion)
checkAndroidV2SignaturePath = PackUtils.getSubDirFilePath("lib", "CheckAndroidV2Signature.jar")
walleChannelWritterPath = PackUtils.getSubDirFilePath("lib", "walle-cli-all.jar")

keystorePath = PackUtils.getSubDirFilePath("source", PackConfig.storeFile)
keyAlias = PackConfig.keyAlias
keystorePassword = PackConfig.keystorePassword
keyPassword = PackConfig.keyPassword


def autoPack(pack_config):
    """
    批量签名并写入渠道号
    :param pack_config: 配置
    :return: None
    """
    protectedSourceApkPath = PackUtils.getSubDirFilePath("source", pack_config[0])
    apkVersionName = PackUtils.getApkVersionName(protectedSourceApkPath)

    # 对齐
    zipAlignedApkPath = protectedSourceApkPath[0: -4] + "_aligned.apk"
    PackUtils.deleteFile(zipAlignedApkPath)

    zipalignShell = buildToolsPath + os.sep + "zipalign -v 4 " + protectedSourceApkPath + " " + zipAlignedApkPath
    os.system(zipalignShell)
    print(zipalignShell)

    # 签名
    signedApkPath = zipAlignedApkPath[0: -4] + "_signed.apk"
    PackUtils.deleteFile(signedApkPath)

    signShell = buildToolsPath + os.sep + "apksigner sign --ks " + keystorePath + \
                " --ks-key-alias " + keyAlias + \
                " --ks-pass pass:" + keystorePassword + \
                " --key-pass pass:" + keyPassword + \
                " --out " + signedApkPath + \
                " " + zipAlignedApkPath
    os.system(signShell)
    print(signShell)

    # 检查V2签名是否正确
    checkV2Shell = "java -jar " + checkAndroidV2SignaturePath + " " + signedApkPath
    os.system(checkV2Shell)

    # 清空输出文件目录
    outputDirPath = os.path.join(os.getcwd(), "channels", pack_config[0][0:-4])
    if not os.path.exists(outputDirPath):
        os.makedirs(outputDirPath)

    with os.scandir(outputDirPath) as it:
        for entity in it:
            if entity.is_file():
                os.remove(entity)
    pass

    # 批量写入渠道号
    channelFilePath = PackUtils.getProjectDirFilePath(pack_config[1])
    writeChannelShell = "java -jar " + walleChannelWritterPath + \
                        " batch -f " + channelFilePath + " " + signedApkPath + " " + outputDirPath
    print(writeChannelShell)
    os.system(writeChannelShell)

    # 删除临时文件
    PackUtils.deleteFile(zipAlignedApkPath)
    PackUtils.deleteFile(signedApkPath)

    # 文件重命名
    if len(PackConfig.apkFileNamePattern) > 0:
        with os.scandir(outputDirPath) as it:
            for file in it:
                print(file.path)
                # 提取渠道名称，360_aligned_signed_huawei.apk -> huawei
                channelName = re.findall(".+_signed_(\S+).apk$", file.path)[0]
                # 重命名, sample_1.0_huawei_release1.apk
                newFileName = PackConfig.apkFileNamePattern % (apkVersionName, channelName)
                os.renames(file.path, os.path.join(os.path.dirname(file.path), newFileName))
        pass

    print("\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   Please check channels in the path   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n")
    print("\n" + outputDirPath + "\n")
    print("\n↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   Please check channels in the path   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑\n")
    pass


# 根据配置打包
for packConfig in PackConfig.autoPackConfig:
    try:
        if os.path.exists(PackUtils.getSubDirFilePath("source", packConfig[0])):
            autoPack(packConfig)
    except FileNotFoundError as e:
        print(packConfig[0] + " not found")
        pass

print("\n**** =============================TASK FINISHED=================================== ****\n")