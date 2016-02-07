package com.sk.netty.client.chat;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.sk.netty.client.domain.ChatMessage;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;
import io.netty.util.AttributeKey;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by skplanet on 15. 1. 5..
 */
public class ChatClientHander extends SimpleChannelInboundHandler<String> {
    private Logger logger = LoggerFactory.getLogger(ChatClientHander.class);

    @Override
    protected void channelRead0(ChannelHandlerContext ctx, String msg) throws Exception {
        System.err.println(msg);
//        logger.error(msg);
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {
        // Close the connection when an exception is raised.
        cause.printStackTrace();
        ctx.close();
    }

}
