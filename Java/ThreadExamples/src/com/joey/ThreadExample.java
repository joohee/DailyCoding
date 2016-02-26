package com.joey;

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
            t.setUncaughtExceptionHandler((t1, e) -> {
                System.out.println("error occured..." +  t1.getName() + ", " + e.getClass().getSimpleName());
                e.printStackTrace();
            });
            return t;
        }
    });

    public static void main(String[] args) {
        executor.execute(() -> {
            throw new RuntimeException();
        });
    }



}
