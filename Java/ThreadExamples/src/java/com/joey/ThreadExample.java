package com.joey;

import com.joey.handler.ThreadUncaughtExceptionHandler;

import java.util.concurrent.Executor;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadFactory;
import java.util.concurrent.atomic.AtomicInteger;

public class ThreadExample {

	private static final Executor executor = Executors.newFixedThreadPool(3, new ThreadFactory() {
		private AtomicInteger num = new AtomicInteger();

		@Override
		public Thread newThread(Runnable r) {
			Thread t = new Thread(r, "thread-" + num.getAndIncrement());
			t.setDaemon(false);
			t.setPriority(Thread.NORM_PRIORITY);
			t.setUncaughtExceptionHandler(new ThreadUncaughtExceptionHandler());
			return t;
		}
	});

	public static void main(String[] args) {
		for (int i = 0; i < 5; i++) {
			executor.execute(() -> {
				try {
//					log.info("Thread started...{}", this.getClass().getSimpleName());
					Thread.sleep(1000L);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				throw new RuntimeException();
			});
		}

	}


}
