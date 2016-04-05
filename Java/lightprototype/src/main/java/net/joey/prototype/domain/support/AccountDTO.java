package net.joey.prototype.domain.support;

import lombok.Data;
import org.hibernate.validator.constraints.NotEmpty;

import javax.validation.constraints.Size;
import java.util.Date;

/**
 * Created by skplanet on 14. 12. 29..
 */
@Data
public class AccountDTO {

    @NotEmpty
    @Size(min = 4)
    protected String username;

    @NotEmpty
    protected String email;

    @Data
    public static class RequestToCreate extends AccountDTO {
        @NotEmpty
        private String password;
    }

    @Data
    public static class Response extends AccountDTO {
        private Long id;
        private Date joined;
    }
}
