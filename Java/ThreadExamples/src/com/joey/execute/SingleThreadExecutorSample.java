package com.joey.execute;

import com.joey.ThreadUncaughtExceptionHandler;

import java.util.Date;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadFactory;

/**
 * Created with ThreadExamples.
 * User: neigie
 * Date: 2016. 3. 6.
 * Time: 13:02
 * To change this template use File | Settings | File Templates.
 */
public class SingleThreadExecutorSample {

    public static void main(String[] args) {

        ExecutorService executorService = Executors.newSingleThreadExecutor(new ThreadFactory() {
            @Override
            public Thread newThread(Runnable r) {
               Thread t = new Thread(r, "single-thread");
                t.setPriority(Thread.NORM_PRIORITY);
                t.setDaemon(false);
                t.setUncaughtExceptionHandler(new ThreadUncaughtExceptionHandler());
                return t;
            }
        });

        executorService.execute(() -> {
            System.out.println("thread start...date: " + new Date().toString());
            try {
                Thread.sleep(1000L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("thread end...date: " + new Date().toString());

        });
    }
}
