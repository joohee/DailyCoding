package net.joey.prototype.service;

import lombok.extern.slf4j.Slf4j;
import net.joey.prototype.domain.Account;
import net.joey.prototype.domain.support.AccountDTO;
import net.joey.prototype.repository.AccountRepository;
import org.modelmapper.ModelMapper;
import org.springframework.stereotype.Service;

import javax.inject.Inject;
import java.util.Date;

/**
 * Created by skplanet on 14. 12. 19..
 */
@Service
@Slf4j
public class AccountService {

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
