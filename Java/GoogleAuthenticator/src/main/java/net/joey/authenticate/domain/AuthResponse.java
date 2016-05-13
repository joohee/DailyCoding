package net.joey.authenticate.domain;

import lombok.Data;

@Data
public class AuthResponse {

    String encodedKey;

    String urlForQR;
}
