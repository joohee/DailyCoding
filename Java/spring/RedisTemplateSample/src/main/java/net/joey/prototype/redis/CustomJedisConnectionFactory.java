package net.joey.prototype.redis;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import net.joey.prototype.config.RedisPropertiesConfig;
import org.apache.commons.lang3.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.core.env.Environment;
import org.springframework.data.redis.connection.jedis.JedisConnectionFactory;
import org.springframework.stereotype.Component;
import redis.clients.jedis.JedisPoolConfig;

import javax.inject.Inject;

@Component
public class CustomJedisConnectionFactory implements InitializingBean {
	private final Logger logger = LoggerFactory.getLogger(getClass());

	public static final String REDISKEY_SAMPLE = "sample:";

	@Inject
	private RedisPropertiesConfig config;

	@Inject
	private Environment environment;

	@Inject
	private ObjectMapper objectMapper;

	private JedisConnectionFactory _masterJedisConnectionFactory;

	private JedisConnectionFactory _secondaryJedisConnectionFactory;

	private SampleRedisStore _sampleRedisStore;

	@Override
	public void afterPropertiesSet() throws Exception {
		_masterJedisConnectionFactory = createJedisConnectionFactory(config.getServers().get("master"), config.getMasterPoolConfig());

		String ec2AvailabilityZone = environment.getProperty("EC2_AZ");
		logger.info("ec2AvailabilityZone = {}", ec2AvailabilityZone);

		String secondaryHostName = null;
		if (StringUtils.isNotEmpty(ec2AvailabilityZone)) {
			secondaryHostName = config.getServers().get("secondary-" + ec2AvailabilityZone);
		}
		if (StringUtils.isEmpty(secondaryHostName)) {
			secondaryHostName = config.getServers().get("secondary");
		}
		_secondaryJedisConnectionFactory = createJedisConnectionFactory(secondaryHostName, config.getSecondaryPoolConfig());

		_sampleRedisStore = new SampleRedisStore(REDISKEY_SAMPLE, _masterJedisConnectionFactory, _secondaryJedisConnectionFactory);
	}

	private JedisConnectionFactory createJedisConnectionFactory(String hostWithOptionalPort, JedisPoolConfig poolConfig) {
		String hostName = null;
		Integer port = null;
		String[] parts = StringUtils.split(hostWithOptionalPort, ':');
		if (parts.length > 1) {
			hostName = parts[0];
			port = Integer.parseInt(parts[1]);
		} else {
			hostName = parts[0];
		}

		JedisConnectionFactory jedisConnectionFactory = new JedisConnectionFactory(poolConfig);
		jedisConnectionFactory.setHostName(hostName);
		if (port != null) {
			jedisConnectionFactory.setPort(port);
		}
		jedisConnectionFactory.setUsePool(true);
		jedisConnectionFactory.afterPropertiesSet();

		logger.warn("Redis-connection-factory for {} = host:{}, port:{}, pool-config:{}", hostWithOptionalPort,
				jedisConnectionFactory.getHostName(), jedisConnectionFactory.getPort(), inspectForInfo(jedisConnectionFactory.getPoolConfig()));

		return jedisConnectionFactory;
	}

	private String inspectForInfo(Object config) {
		try {
			return objectMapper.writeValueAsString(config);
		} catch (JsonProcessingException e) {
			logger.error("on inspecting a object", e);
			return config.toString();
		}
	}

	public JedisConnectionFactory master() {
		return _masterJedisConnectionFactory;
	}

	public JedisConnectionFactory secondary() {
		return _secondaryJedisConnectionFactory;
	}

	public SampleRedisStore sampleRedisStore() {
		return _sampleRedisStore;
	}

}
