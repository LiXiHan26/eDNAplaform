# -*- coding=utf-8
from tools.qcloud_cos import CosConfig
from tools.qcloud_cos import CosS3Client


def getclient():
    # 1. 设置用户属性, 包括 secret_id, secret_key, region 等。Appid 已在 CosConfig 中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
    tmp_secret_id = 'AKIDjOsKg3KSPmzkJm7OVO8jCWggYGvLgv0z'  # 临时密钥的 SecretId，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
    tmp_secret_key = 'v42weEi4EF9pJWfhYGqDSWJzVpwvkLit'  # 临时密钥的 SecretKey，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
    # token = 'TmpToken'                # 临时密钥的 Token，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
    region = 'ap-guangzhou'  # 替换为用户的 region，已创建桶归属的 region 可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
    # COS 支持的所有 region 列表参见https://cloud.tencent.com/document/product/436/6224
    # scheme = 'https'           # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
    config = CosConfig(Region=region, Secret_id=tmp_secret_id, Secret_key=tmp_secret_key)
    # 2. 获取客户端对象
    client = CosS3Client(config)

    return client