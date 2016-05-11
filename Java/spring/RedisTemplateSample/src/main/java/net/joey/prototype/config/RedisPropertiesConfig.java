package net.joey.prototype.config;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;
import redis.clients.jedis.JedisPoolConfig;

import java.util.Map;

/**
 * Created by joey on 2015. 4. 24..
 */
@Configuration
@ConfigurationProperties("redis")
@Data
public class RedisPropertiesConfig {

    private Map<String, String> servers;

	private JedisPoolConfig masterPoolConfig;

	private JedisPoolConfig secondaryPoolConfig;

}
