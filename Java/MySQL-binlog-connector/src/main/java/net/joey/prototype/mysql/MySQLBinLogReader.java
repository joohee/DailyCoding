package net.joey.prototype.mysql;

import com.github.shyiko.mysql.binlog.BinaryLogClient;
import lombok.extern.slf4j.Slf4j;
import net.joey.prototype.mysql.support.CapturingEventListener;
import net.joey.prototype.mysql.support.CountDownEventListener;
import net.joey.prototype.mysql.support.TraceEventListener;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.sql.SQLException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadFactory;

/**
 * Created by a1100007 on 2016. 5. 26..
 */
@Component
@Slf4j
public class MySQLBinLogReader {

	@Value("${spring.datasource.url}")
	private String _jdbcUrl;

	@Value("${spring.datasource.username}")
	private String _username;

	@Value("${spring.datasource.platform}")
	private String _platform;

	private static final String JDBC_PREFIX = "jdbc:mysql://";

	private static final String DELIM = "/";

	private static final String SUB_DELIM = ":";

	private ExecutorService executorService = Executors.newCachedThreadPool(new ThreadFactory() {
		@Override
		public Thread newThread(Runnable r) {
			Thread thread = new Thread(r);
			thread.setDaemon(true);
			thread.setName("MySQLBinLogThread");
			thread.setPriority(Thread.NORM_PRIORITY);
			return thread;
		}
	});

	@EventListener
	public void handleMySQLBinLogEvent(ContextRefreshedEvent event) throws SQLException {
		String[] strs = _jdbcUrl.replace(JDBC_PREFIX, "").split(DELIM);
		String[] hostAndPort = strs[0].split(SUB_DELIM);

		String host = hostAndPort[0];
		String port = hostAndPort[1];
		BinaryLogClient binaryLogClient = new BinaryLogClient(host, Integer.parseInt(port), _username, _platform);
		TraceEventListener traceEventListener = new TraceEventListener();
		binaryLogClient.registerEventListener(traceEventListener);
		binaryLogClient.registerEventListener(new CountDownEventListener());
		binaryLogClient.registerEventListener(new CapturingEventListener());

		log.info(binaryLogClient.toString());

		executorService.execute(new Runnable() {
			@Override
			public void run() {
				while (!Thread.interrupted()) {
					log.info("Thread lives...");
					try {
						binaryLogClient.connect();
					} catch (IOException e) {
						e.printStackTrace();
						// restart?
						try {
							binaryLogClient.disconnect();
						} catch (IOException e1) {
							e1.printStackTrace();
						}
					}
				}

				if (Thread.interrupted()) {
					try {
						Thread.sleep(3000L);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
					try {
						binaryLogClient.connect();
					} catch (IOException e) {
						e.printStackTrace();
					}
				}
			}
		});

	}
}
