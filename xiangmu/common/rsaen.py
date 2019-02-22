from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP, PKCS1_v1_5
import base64, os
from urllib import parse
from django.conf import settings


def create_rsa_key(password="123456"):
    """
    创建RSA密钥
    步骤说明：
    1、从 Crypto.PublicKey 包中导入 RSA，创建一个密码
    2、生成 1024/2048 位的 RSA 密钥
    3、调用 RSA 密钥实例的 exportKey 方法，传入密码、使用的 PKCS 标准以及加密方案这三个参数。
    4、将私钥写入磁盘的文件。
    5、使用方法链调用 publickey 和 exportKey 方法生成公钥，写入磁盘上的文件。
    """

    key = RSA.generate(1024)
    encrypted_key = key.exportKey(passphrase=password, pkcs=8,
                                  protection="scryptAndAES128-CBC")
    with open("my_private_rsa_key.bin", "wb") as f:
        f.write(encrypted_key)
    with open("my_rsa_public.pem", "wb") as f:
        f.write(key.publickey().exportKey())


def decrypt_data(inputdata, code="123456"):
    # URLDecode
    data = parse.unquote(inputdata)

    # base64decode
    data = base64.b64decode(data)

    private_key_file = os.path.join(settings.BASE_DIR, 'common/my_private_rsa_key.bin')
    private_key = RSA.import_key(
        open(private_key_file).read(),
        passphrase=code
    )
    # 使用 PKCS1_v1_5，不要用 PKCS1_OAEP
    # 使用 PKCS1_OAEP 的话，前端 jsencrypt.js 加密的数据解密不了
    cipher_rsa = PKCS1_v1_5.new(private_key)

    # 当解密失败，会返回 sentinel
    sentinel = None
    ret = cipher_rsa.decrypt(data, sentinel)

    return ret.decode()

# if __name__ == '__main__':
#     create_rsa_key()
# # encrypt_and_decrypt_test()
