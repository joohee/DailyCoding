package com.sk.prototype.controller;

import com.sk.prototype.domain.Account;
import com.sk.prototype.domain.support.AccountDTO;
import com.sk.prototype.service.AccountService;
import com.wordnik.swagger.annotations.Api;
import com.wordnik.swagger.annotations.ApiOperation;
import com.wordnik.swagger.annotations.ApiResponse;
import com.wordnik.swagger.annotations.ApiResponses;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import javax.validation.Valid;
import javax.websocket.server.PathParam;

/**
 * Created by skplanet on 14. 12. 19..
 */
@Controller
@Api(value = "account", description = "apis for accounts")
public class AccountController {

    @Autowired
    private ModelMapper modelMapper;

    @Autowired
    private AccountService accountService;

    @RequestMapping(value = "/accounts", method = RequestMethod.POST)
    @ApiOperation(value = "create account", httpMethod = "POST")
    public ResponseEntity createNewAccount(@RequestBody @Valid AccountDTO.RequestToCreate accountDTO
                                         , BindingResult result) throws Exception {
        if (result.hasErrors()) {
            return new ResponseEntity(null, HttpStatus.BAD_REQUEST);
        }
        Account newAccount = accountService.createNew(accountDTO);

        return new ResponseEntity(modelMapper.map(newAccount, AccountDTO.Response.class), HttpStatus.CREATED);
    }

    @RequestMapping(value = "/accounts/{username}", method = RequestMethod.GET)
    @ApiOperation(value = "find account if exists", httpMethod = "GET")
    @ApiResponses(value = { @ApiResponse(code = 200, message = "account exists."),
                            @ApiResponse(code = 404, message = "account not exists.")
                           })
    public ResponseEntity find(@PathParam("username") @PathVariable String username) {
        Account found = accountService.find(username);

        if (found == null) {
            return new ResponseEntity(null, HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity(modelMapper.map(found, AccountDTO.Response.class), HttpStatus.OK);
    }
}
