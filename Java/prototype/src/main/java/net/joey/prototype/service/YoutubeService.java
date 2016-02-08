package net.joey.prototype.service;

import net.joey.prototype.scheduler.crawl.YoutubeCrawler;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import javax.inject.Inject;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadFactory;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Created by skplanet on 14. 12. 31..
 */
@Service
public class YoutubeService {
    private Logger logger = LoggerFactory.getLogger(YoutubeService.class);

    private ExecutorService executorService = Executors.newFixedThreadPool(5, new ThreadFactory() {
        private AtomicInteger threadNumber = new AtomicInteger(1);
        @Override
        public Thread newThread(Runnable r) {
            Thread t = new Thread(r, "youtube-crawled-" + threadNumber.getAndIncrement());
            t.setDaemon(false);
            t.setPriority(Thread.NORM_PRIORITY);
            return t;
        }
    });

    @Inject
    private YoutubeCrawler crawler;

    @Scheduled(fixedRate=60000)
    public void executeSearch() {
        for (int i = 0; i < 5; i++) {
            executorService.execute(() -> {
                logger.info("started...");
                crawler.search();
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            });
        }
    }
}
