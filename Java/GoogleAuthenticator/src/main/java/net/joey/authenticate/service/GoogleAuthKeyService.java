package net.joey.authenticate.service;

import lombok.extern.slf4j.Slf4j;
import net.joey.authenticate.domain.AuthResponse;
import org.apache.commons.codec.binary.Base32;
import org.springframework.stereotype.Service;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.Random;

/**
 * Created by a1001962 on 2016. 4. 5..
 */
@Service
@Slf4j
public class GoogleAuthKeyService {

    private final static int SECRET_SIZE = 5;
    private final static int NUM_OF_SCRATCH_CODES = 5;
    private final static int SCRATCH_CODE_SIZE = 5;

    public AuthResponse createKey(String username, String host) {
        // Allocating the buffer
//      byte[] buffer = new byte[secretSize + numOfScratchCodes * scratchCodeSize];
        byte[] buffer = new byte[SECRET_SIZE + NUM_OF_SCRATCH_CODES * SCRATCH_CODE_SIZE];

        // Filling the buffer with random numbers.
        // Notice: you want to reuse the same random generator
        // while generating larger random number sequences.
        new Random().nextBytes(buffer);

        // Getting the key and converting it to Base32
        Base32 codec = new Base32();
//      byte[] secretKey = Arrays.copyOf(buffer, secretSize);
        byte[] secretKey = Arrays.copyOf(buffer, SECRET_SIZE);
        byte[] bEncodedKey = codec.encode(secretKey);

        // 생성된 Key!
        String encodedKey = new String(bEncodedKey);
        log.info("encodedKey : " + encodedKey);

//      String url = getQRBarcodeURL(userName, hostName, secretKeyStr);
        // userName과 hostName은 변수로 받아서 넣어야 하지만, 여기선 테스트를 위해 하드코딩 해줬다.
        String url = getQRBarcodeURL(username, host, encodedKey); // 생성된 바코드 주소!
        log.info("URL : " + url);

        AuthResponse res = new AuthResponse();
        res.setEncodedKey(encodedKey);
        res.setUrlForQR(url);

        return res;
    }

    // 바코드 생성을 위한 URL
    public static String getQRBarcodeURL(String user, String host, String secret) {
        String format = "http://chart.apis.google.com/chart?cht=qr&amp;chs=300x300&amp;chl=otpauth://totp/%s@%s%%3Fsecret%%3D%s&amp;chld=H|0";

        return String.format(format, user, host, secret);
    }

    public boolean checkCode(String secret, long code, long t)
            throws NoSuchAlgorithmException, InvalidKeyException {
        Base32 codec = new Base32();
        byte[] decodedKey = codec.decode(secret);


        // Window is used to check codes generated in the near past.
        // You can use this value to tune how far you're willing to go.
        int window = 3;
        for (int i = -window; i <= window; ++i) {
            long hash = verifyCode(decodedKey, t + i);


            if (hash == code) {
                return true;
            }
        }


        // The validation code is invalid.
        return false;
    }

    private static int verifyCode(byte[] key, long t) throws NoSuchAlgorithmException, InvalidKeyException {
        byte[] data = new byte[8];
        long value = t;
        for (int i = 8; i-- > 0; value >>>= 8) {
            data[i] = (byte) value;
        }


        SecretKeySpec signKey = new SecretKeySpec(key, "HmacSHA1");
        Mac mac = Mac.getInstance("HmacSHA1");
        mac.init(signKey);
        byte[] hash = mac.doFinal(data);

        int offset = hash[20 - 1] & 0xF;

        // We're using a long because Java hasn't got unsigned int.
        long truncatedHash = 0;
        for (int i = 0; i < 4; ++i) {
            truncatedHash <<= 8;
            // We are dealing with signed bytes:
            // we just keep the first byte.
            truncatedHash |= (hash[offset + i] & 0xFF);
        }


        truncatedHash &= 0x7FFFFFFF;
        truncatedHash %= 1000000;

        return (int) truncatedHash;
    }
}
