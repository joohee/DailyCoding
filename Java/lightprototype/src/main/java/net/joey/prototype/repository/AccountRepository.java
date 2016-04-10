package net.joey.prototype.repository;

import net.joey.prototype.domain.Account;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * Created by skplanet on 14. 12. 19..
 */
public interface AccountRepository extends JpaRepository<Account, Integer> {
    Account findByUsername(String username);
}
