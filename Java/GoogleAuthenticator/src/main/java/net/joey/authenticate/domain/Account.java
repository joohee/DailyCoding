package net.joey.authenticate.domain;

import lombok.Data;

import javax.persistence.*;
import java.util.Date;

/**
 * Created by skplanet on 14. 12. 19..
 */
@Data
@Entity
public class Account {

    @Id
    @GeneratedValue
    private Long id;

    @Column(unique = true, nullable = false)
    private String username;

    @Column(nullable = false)
    private String password;

    @Column(unique = true)
    private String email;

    @Temporal(TemporalType.DATE)
    private Date joined;
}
