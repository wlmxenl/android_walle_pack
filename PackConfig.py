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

# 输出渠道文件名配置
# sample_{版本号}_{渠道号}_release.apk, eg：sample_1.0_huawei_release.apk
apkFileNamePattern = "sample_%s_%s_release.apk"