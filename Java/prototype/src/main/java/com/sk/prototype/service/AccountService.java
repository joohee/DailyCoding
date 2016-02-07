package com.sk.prototype.service;

import com.mysql.jdbc.exceptions.MySQLIntegrityConstraintViolationException;
import com.sk.prototype.domain.Account;
import com.sk.prototype.domain.support.AccountDTO;
import com.sk.prototype.repository.AccountRepository;
import org.modelmapper.ModelMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.inject.Inject;
import java.util.Date;

/**
 * Created by skplanet on 14. 12. 19..
 */
@Service
public class AccountService {
     private Logger logger = LoggerFactory.getLogger(AccountService.class);

    @Inject
    private ModelMapper modelMapper;

    @Inject
    private AccountRepository accountRepository;

    public Account createNew(AccountDTO.RequestToCreate accountDTO)  {
        Account account = modelMapper.map(accountDTO, Account.class);
        // TODO : password encryption
        account.setJoined(new Date());

        return accountRepository.save(account);
    }

    public Account find(String username) {
        Account account = accountRepository.findByUsername(username);
        return account;
    }
}
