package net.joey.prototype;
/**
 * Created by a1100007 on 2016. 5. 11..
 */

import lombok.extern.slf4j.Slf4j;
import net.joey.prototype.redis.CustomJedisConnectionFactory;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.SpringApplicationContextLoader;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.web.WebAppConfiguration;

import javax.inject.Inject;

import static org.fest.assertions.Assertions.assertThat;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = {Application.class}, loader = SpringApplicationContextLoader.class)
@WebAppConfiguration
@ActiveProfiles("localhost")
@Slf4j
public class SampleRedisStoreTest {

	@Inject
	private CustomJedisConnectionFactory connectionFactory;

	@Test
	public void testAddAndGet() {
		String sampleKey = "sampleKey";
		String sampleValue = "sampleValue";

		boolean resultForAdd = connectionFactory.sampleRedisStore().add(sampleKey, sampleValue);
		assertThat(resultForAdd).isTrue();

		String returnValue = connectionFactory.sampleRedisStore().get(sampleKey);
		assertThat(sampleValue.equals(returnValue)).isTrue();
	}
}