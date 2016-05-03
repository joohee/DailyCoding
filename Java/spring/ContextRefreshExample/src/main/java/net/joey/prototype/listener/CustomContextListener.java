package net.joey.prototype.listener;

import lombok.extern.slf4j.Slf4j;
import org.springframework.context.ApplicationListener;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.stereotype.Component;

/**
 * Created by a1100007 on 2016. 5. 2..
 */
@Component
@Slf4j
public class CustomContextListener implements ApplicationListener<ContextRefreshedEvent> {
    @Override
    public void onApplicationEvent(ContextRefreshedEvent event) {
        log.info("onApplicationEvent: {}" + event.getSource());

        Thread thread = new Thread(new CustomContextThread());
        thread.setName(this.getClass().getSimpleName());
        thread.setDaemon(true);
        thread.start();
    }

    private class CustomContextThread implements Runnable {
        @Override
        public void run() {
            while (! Thread.interrupted()) {
                log.info("Thread start...{}", this.getClass().getSimpleName());
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
