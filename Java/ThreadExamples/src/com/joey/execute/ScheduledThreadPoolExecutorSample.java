package com.joey.execute;

import com.joey.ThreadUncaughtExceptionHandler;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadFactory;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Created with ThreadExamples.
 * User: neigie
 * Date: 2016. 3. 7.
 * Time: 10:14
 * To change this template use File | Settings | File Templates.
 */
public class ScheduledThreadPoolExecutorSample {

    public static void main(String[] args) {
        ExecutorService executorService = Executors.newScheduledThreadPool(5, new ThreadFactory() {
            private AtomicInteger threadNumber = new AtomicInteger(1);

            @Override
            public Thread newThread(Runnable r) {
                Thread t = new Thread(r, "scheduled-thread-" + threadNumber.getAndIncrement());
                t.setDaemon(false);
                t.setPriority(Thread.NORM_PRIORITY);
                t.setUncaughtExceptionHandler(new ThreadUncaughtExceptionHandler());
                return t;
            }
        });

        for (int i = 0; i < 10; i++) {
            executorService.execute(() -> {
                String threadName = Thread.currentThread().getName();
                System.out.println("threadName: " + threadName + " - execute by scheduled thread pool....");
            });
        }
    }
}

