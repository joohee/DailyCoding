import net.joey.utils.EncryptUtils;
import org.junit.Test;

import static org.fest.assertions.api.Assertions.assertThat;

/**
 * Created by joey on 2016. 4. 28..
 */
public class EncryptUtilsTest {
    EncryptUtils encryptUtils = new EncryptUtils();

    private String rawData = "neigie@gmail.com";

    @Test
    public void testCreate() {
        String encrypted = encryptUtils.encrypt(rawData);
        String decrypted = encryptUtils.decrypt(encrypted);

        assertThat(rawData).isEqualTo(decrypted);
    }
}
