package com.sk.prototype.service;

import com.sk.prototype.scheduler.crawl.YoutubeCrawler;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import javax.inject.Inject;

/**
 * Created by skplanet on 14. 12. 31..
 */
@Service
public class YoutubeService {
    private Logger logger = LoggerFactory.getLogger(YoutubeService.class);

    @Inject
    private YoutubeCrawler crawler;

    @Scheduled(fixedRate=60000)
    public void executeSearch() {
        for (int i = 0; i < 5; i++) {
            Thread thread = new Thread(() -> crawler.search());
            thread.setName("thread-" + i);
            thread.start();

            logger.info(thread.getName() + " started...");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
