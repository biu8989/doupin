function enrsa(data) {
    var publickey = '-----BEGIN PUBLIC KEY-----\n' +
        'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDPYkQjFYh89yEUmqjzER+YTEcv\n' +
        'jQXM/I0y0JpYP3xPJq0nyQx+Ib+GxBC86TQjb5pGjJnANFGRFHUx56X05szMWjZI\n' +
        'CWogSRIpA9Wcazrrpst1df4g1zfoF7GbhZLf/A/kWIPbEULIOrbh2WH2YTSOpdsj\n' +
        '9iGfV2ZGFhUj7XFR/QIDAQAB\n' +
        '-----END PUBLIC KEY-----';
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(publickey);
    datamw = encrypt.encrypt(data);
    return datamw;
}