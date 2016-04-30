package net.joey.utils;

import org.apache.commons.codec.binary.Hex;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
 * - hash256(String)
 *  SHA-256 암호화 알고리즘을 이용하여 리턴한다
 * - encrypt(String)
 *  내부 encryptor (PBEWithMD5AndDES 알고리즘 사용 및 base64 인코딩 을 이용하여 암호화한다
 * - decrypt(String)
 *  encrypt(String) 메소드를 이용한 결과값을 복호화한다. 이메일로 전송된 안전한 링크로부터 데이터를 추출하는 데 사용한다.
 * Created by joey on 2015. 3. 26..
 */
public class EncryptUtils {

    private Logger logger = LoggerFactory.getLogger(EncryptUtils.class);
    private StandardPBEStringEncryptor encryptor;
    private static final String ENCRYPT_PASSWORD = "YOUR_KEY";

    public EncryptUtils() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setAlgorithm("PBEWithMD5AndDES");
        encryptor.setPassword(ENCRYPT_PASSWORD);
        encryptor.setStringOutputType("base64");
    }

    public String hash256(String rawData) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(rawData.getBytes());
        return String.valueOf(Hex.encodeHex(md.digest()));
    }

    public String encrypt(String rawData) {
        return encryptor.encrypt(rawData);
    }

    public String decrypt(String encryptedData) {
        return encryptor.decrypt(encryptedData);
    }

}
