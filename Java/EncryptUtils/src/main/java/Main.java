import net.joey.utils.EncryptUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.security.NoSuchAlgorithmException;

public class Main {

    private static Logger logger = LoggerFactory.getLogger(Main.class);
    public static void main(String[] args) throws NoSuchAlgorithmException {
        EncryptUtils encryptUtils = new EncryptUtils();
        String result = encryptUtils.hash256("abcdef");
        logger.info("The Result: {}", result);
    }
}
