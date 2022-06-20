此脚本基于 [Jay-Goo/ProtectedApkResignerForWalle](https://github.com/Jay-Goo/ProtectedApkResignerForWalle) 项目并根据自己现维护项目的使用场景修改而来，仅在个人设备调试通过。

- 支持多加固平台动态配置
- 自动查找 sdk/build-tools 路径（需配置 PATH -> `Sdk\platform-tools (adb)`  环境变量）

## 使用说明
1. 将签名文件存放到 `source` 目录下
2. 修改 `config.py` 配置（应用名称、版本号、输出渠道包命名规则、签名信息）
3. 360加固后的包存放至 `source` 目录下，命名为 `360.apk`
4. 乐固平台加固后的包存放至 `source` 目录下，命名为 `legu.apk`
5. 在脚本目录下执行 `py ApkResigner.py`
6. 渠道包输出路径 -> 当前目录下 `channel\360\`、`channel\legu\`