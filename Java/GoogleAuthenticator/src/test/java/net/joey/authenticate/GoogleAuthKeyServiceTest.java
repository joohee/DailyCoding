package net.joey.authenticate;
/**
 * Created by a1001962 on 2016. 4. 5..
 */

import lombok.extern.slf4j.Slf4j;
import net.joey.authenticate.domain.AuthResponse;
import net.joey.authenticate.service.GoogleAuthKeyService;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.SpringApplicationContextLoader;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.web.WebAppConfiguration;

import javax.inject.Inject;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Date;

import static org.fest.assertions.Assertions.assertThat;


@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = {Application.class}, loader = SpringApplicationContextLoader.class)
@WebAppConfiguration
@ActiveProfiles("localhost")
@Slf4j
public class GoogleAuthKeyServiceTest {

    @Inject
    private GoogleAuthKeyService googleAuthKeyService;

    @Test
    public void testCreateKey() {
        String username = "username";
        String host = "test.domain.com";
        AuthResponse res = googleAuthKeyService.createKey(username, host);

        log.info("encodedKey: {}, url: {}", res.getEncodedKey(), res.getUrlForQR());
    }

    @Test
    public void testCheckCode() {
        //String encodedUrlForBarcode = "http://chart.apis.google.com/chart?cht=qr&amp;chs=300x300&amp;" +
//                "chl=otpauth://totp/username@test.hotzil.com%3Fsecret%3D6OJ5EJ72&amp;chld=H|0";
        String encodedKey = "2AMJNXHE";
        String userCode = "895313";
        long l = new Date().getTime();
        long ll =  l / 30000;

        try {
            boolean result = googleAuthKeyService.checkCode(encodedKey, Integer.parseInt(userCode), ll);
            log.info("result: {}", result);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        } catch (InvalidKeyException e) {
            e.printStackTrace();
        }
    }

}
