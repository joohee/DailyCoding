package com.joey.execute;

import com.joey.handler.ThreadUncaughtExceptionHandler;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadFactory;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Created with ThreadExamples.
 * User: neigie
 * Date: 2016. 3. 6.
 * Time: 13:06
 * To change this template use File | Settings | File Templates.
 */
public class FixedThreadPoolExecutorSample {

    public static void main(String[] args) {
        ExecutorService executorService = Executors.newFixedThreadPool(5, new ThreadFactory() {
            private final AtomicInteger threadNumber = new AtomicInteger(1);
            @Override
            public Thread newThread(Runnable r) {
                Thread t = new Thread(r, "fixed-thread-" + threadNumber.getAndIncrement());
                t.setDaemon(false);
                t.setPriority(Thread.NORM_PRIORITY);
                t.setUncaughtExceptionHandler(new ThreadUncaughtExceptionHandler());
                return t;
            }
        });

        for (int i = 0; i < 5; i++) {
            executorService.execute(() -> {
                String name = Thread.currentThread().getName();
                System.out.println("before name: " + name);
                try {
                    Thread.sleep(3000L);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("after name: " + name);
            });
        }
    }
}
