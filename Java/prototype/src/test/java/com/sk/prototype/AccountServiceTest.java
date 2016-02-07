package com.sk.prototype;

import com.sk.prototype.controller.AccountController;
import com.sk.prototype.domain.Account;
import com.sk.prototype.domain.support.AccountDTO;
import com.sk.prototype.repository.AccountRepository;
import com.sk.prototype.service.AccountService;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.modelmapper.ModelMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.test.SpringApplicationContextLoader;
import org.springframework.context.annotation.EnableAspectJAutoProxy;
import org.springframework.context.annotation.aspectj.EnableSpringConfigured;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import javax.inject.Inject;
import javax.transaction.Transactional;

import java.util.Date;

import static org.fest.assertions.api.Assertions.assertThat;
import static org.mockito.Mockito.when;

/**
 * Created by skplanet on 14. 12. 26..
 */
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = Application.class, loader = SpringApplicationContextLoader.class)
@Transactional
@EnableSpringConfigured
@EnableAspectJAutoProxy
public class AccountServiceTest {

    Logger logger = LoggerFactory.getLogger(AccountController.class);

    @InjectMocks
    private AccountService accountService = new AccountService();

    @Mock
    private AccountRepository accountRepository;

    @Mock
    protected ModelMapper modelMapper;

    @Mock
    private AccountDTO.RequestToCreate accountDTO;

    @Mock
    private Account account;

    @Before
    public void setup() {
        MockitoAnnotations.initMocks(this);

        when(modelMapper.map(accountDTO, Account.class)).thenReturn(account);
        when(accountService.createNew(accountDTO)).thenReturn(account);
        when(accountService.find("joey")).thenReturn(account);
        when(accountService.find("foo")).thenReturn(null);
    }

    @Test
    public void testAccountRead() {
        accountService.createNew(accountDTO);

        Account found = accountService.find("joey");
        assertThat(found).isNotNull();

        Account notFound = accountService.find("foo");
        assertThat(notFound).isNull();

        logger.info("test success...");
    }
}
