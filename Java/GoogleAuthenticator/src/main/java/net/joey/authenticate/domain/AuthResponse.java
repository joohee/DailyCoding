package net.joey.authenticate.domain;

import lombok.Data;

/**
 * Created by a1001962 on 2016. 4. 5..
 */
@Data
public class AuthResponse {

    String encodedKey;

    String urlForQR;
}
