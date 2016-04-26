package net.joey.utils;

import org.apache.commons.codec.binary.Hex;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
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

    public static String hash256(String rawData) throws NoSuchAlgorithmException {
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
