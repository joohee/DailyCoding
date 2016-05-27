package net.joey.prototype.mysql.support;

import com.github.shyiko.mysql.binlog.BinaryLogClient;
import com.github.shyiko.mysql.binlog.event.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class TraceEventListener implements BinaryLogClient.EventListener {

    private final Logger logger = LoggerFactory.getLogger(this.getClass().getSimpleName());

    @Override
    public void onEvent(Event event) {
        if (logger.isInfoEnabled()) {
            logger.info("Received " + event);
        }

        if (logger.isWarnEnabled()) {
            EventHeaderV4 header = event.getHeader();
            EventData data = event.getData();

            logger.info("[Header] Type: {}, Data: {}]", header.getEventType(), data);
        }

    }
}
