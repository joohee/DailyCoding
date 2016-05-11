package net.joey.prototype.redis;

import lombok.extern.slf4j.Slf4j;
import org.springframework.dao.DataAccessException;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisOperations;
import org.springframework.data.redis.core.SessionCallback;
import org.springframework.data.redis.core.StringRedisTemplate;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

@Slf4j
public class SampleRedisStore {

	private static final long TTL_IN_SEC = 60L * 24 * 60 * 3;  // 3 days

	private static final String SEP = ":";
	private final String keyPrefix;
	private final StringRedisTemplate writableTemplate;
	private final StringRedisTemplate readableTemplate;

	SampleRedisStore(String keyPrefix, RedisConnectionFactory writableConnectionFactory, RedisConnectionFactory readableConnectionFactory) {
		this.keyPrefix = keyPrefix;
		this.writableTemplate = new StringRedisTemplate(writableConnectionFactory);
		this.readableTemplate = readableConnectionFactory != null ? new StringRedisTemplate(readableConnectionFactory) : this.writableTemplate;
	}

	public boolean add(String key, String value)	{
		this.writableTemplate.execute(new SaveOne(getKeyFor(key), value));
		return true;
	}

	public String get(String rawKey) {
		return this.readableTemplate.opsForValue().get(getKeyFor(rawKey));
	}

	public List<String> get(List<String> keys) {
		List<String> rawKeys = new ArrayList<>(keys.size());
		for (String key : keys) {
			rawKeys.add(getKeyFor(key));
		}

		List<String> values = this.readableTemplate.opsForValue().multiGet(keys);
		return values.stream().filter(v -> {
			if (v != null) {
				return true;
			} else {
				return false;
			}
		}).collect(Collectors.toList());
	}

	private String getKeyFor(String rawKey) {
		StringBuffer sb = new StringBuffer();
		sb.append(keyPrefix).append(SEP).append(rawKey);
		return sb.toString();
	}

	private class SaveOne implements SessionCallback<Object> {
		private final String key;
		private final String value;

		public SaveOne(String key, String value) {
			this.key = key;
			this.value = value;
		}

		public <K, V> Object execute(RedisOperations<K, V> operations) throws DataAccessException {
			operations.multi();
			operations.opsForValue().set((K) key, (V)value, TTL_IN_SEC, TimeUnit.SECONDS);
			return operations.exec();
		}
	}

}
