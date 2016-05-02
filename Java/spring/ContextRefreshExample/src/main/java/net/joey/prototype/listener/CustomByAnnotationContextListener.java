package net.joey.prototype.listener;

import lombok.extern.slf4j.Slf4j;
import org.omg.SendingContext.RunTime;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Component;

/**
 * Created by a1100007 on 2016. 5. 2..
 */
@Component
@Slf4j
public class CustomByAnnotationContextListener {

    @EventListener
    public void handleContextRefresh(ContextRefreshedEvent event) {
        log.info("handleContextRefresh with Annotation...");
        log.info("source: {}", event.getSource());

        Thread thread = new Thread(new CustomContextThread());
        thread.setDaemon(true);
        thread.setName(this.getClass().getSimpleName());
        thread.setPriority(Thread.NORM_PRIORITY);
        thread.start();
    }

    private class CustomContextThread implements Runnable {
        @Override
        public void run() {
            while (! Thread.interrupted()) {
                try {
                    log.info("Thread start...{}", this.getClass().getSimpleName());
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

        }

    }
}
