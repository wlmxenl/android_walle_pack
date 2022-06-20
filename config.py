#!/usr/bin/python  
# -*-coding:utf-8-*-

# keystore 信息, 签名文件放到 source 目录下
storeFile = "release.jks"
keyAlias = "wall_sample"
keystorePassword = "GO5DSxdGYP"
keyPassword = "GO5DSxdGYP"

# Android SDK buidtools path , please use above 25.0+
sdkBuildToolVersion = "29.0.3"

# 加固后的源文件名（未重签名）、对应渠道配置
autoPackConfig = [
    ("360.apk", "channel_360"),
    ("legu.apk", "channel_legu")
]

# 应用版本号
appName = "sample"
appVersion = "1.0"

# %s 打包完成后会替换为渠道名称
# 示例：sample_1.0_huawei_release.apk
apkFileNamePattern = appName + "_" + appVersion + "_%s_release.apk"
