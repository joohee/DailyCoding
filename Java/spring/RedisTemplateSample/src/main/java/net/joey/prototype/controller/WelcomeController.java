package net.joey.prototype.controller;

import com.wordnik.swagger.annotations.Api;
import com.wordnik.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import net.joey.prototype.domain.Account;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

/**
 * Created by skplanet on 14. 12. 19..
 */
@Controller
@Api(value = "welcome", description = "test APIs")
@Slf4j
public class WelcomeController {

    @Value("${application.message}")
    private String appMessage;

    @RequestMapping(value = "/", method = RequestMethod.GET)
    @ApiOperation(value = "index", httpMethod = "GET")
    public String welcome(Model model) {
        model.addAttribute("message", appMessage);
        return "index";

    }

    @RequestMapping(value = "/test", method = RequestMethod.GET)
    @ApiOperation(value = "test", httpMethod = "GET")
    public ResponseEntity test() {
        Account account = new Account();
        account.setId(1L);
        account.setUsername("test");
        account.setEmail("test@test.com");
        return new ResponseEntity(account, HttpStatus.NOT_FOUND);
    }
}
