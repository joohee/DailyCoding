package com.sk.prototype.controller;

import com.sk.prototype.Application;
import com.sk.prototype.domain.Account;
import com.wordnik.swagger.annotations.Api;
import com.wordnik.swagger.annotations.ApiOperation;
import org.modelmapper.ModelMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import javax.inject.Inject;
import java.util.Map;

/**
 * Created by skplanet on 14. 12. 19..
 */
@Controller
@Api(value = "welcome", description = "test APIs")
public class WelcomeController {

    private Logger logger = LoggerFactory.getLogger(WelcomeController.class);

    @Autowired
    private ModelMapper modelMapper;

    @Value("${application.message}")
    private String appMessage;

    @Value("${youtube.apikey}")
    private String youtubeApiKey;

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
