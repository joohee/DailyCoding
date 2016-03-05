package com.joey;

/**
 * Created with ThreadExamples.
 * User: neigie
 * Date: 2016. 3. 5.
 * Time: 20:31
 * To change this template use File | Settings | File Templates.
 */
public class ThreadUncaughtExceptionHandler implements Thread.UncaughtExceptionHandler {
    @Override
    public void uncaughtException(Thread t, Throwable e) {
        System.out.println("error occured..." +  t.getName() + ", " + e.getClass().getSimpleName());
        e.printStackTrace();
    }
}
