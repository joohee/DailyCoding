package net.joey.prototype.netty.chat;

import com.fasterxml.jackson.databind.ObjectMapper;
import net.joey.prototype.domain.ChatMessage;
import io.netty.channel.*;
import io.netty.channel.group.ChannelGroup;
import io.netty.channel.group.DefaultChannelGroup;
import io.netty.util.concurrent.GlobalEventExecutor;

public class ChatServerHandler extends SimpleChannelInboundHandler<String>{
    static final ChannelGroup channels = new DefaultChannelGroup(GlobalEventExecutor.INSTANCE);
    private ObjectMapper mapper = new ObjectMapper();

    @Override
    public void handlerAdded(ChannelHandlerContext ctx) throws Exception {
        Channel incoming = ctx.channel();
        channels.stream().filter(channel -> incoming != channel).forEach(channel -> {
            channel.write("[SERVER] - " + incoming.remoteAddress() + " has joined!" + "\n");
            channel.write("[SERVER] - current connections : " + (channels.size() + 1 + "\n"));
            channel.flush();
        });
        channels.add(ctx.channel());
    }

    @Override
    public void handlerRemoved(ChannelHandlerContext ctx) throws Exception {
        Channel incoming = ctx.channel();

        channels.stream().filter(channel -> incoming != channel).forEach(channel -> {
            channel.write("[SERVER] " + incoming.remoteAddress() + " has left!" + "\n");
            channel.write("[SERVER] - current connections : " + (channels.size() - 1) + "\n");
            channel.flush();
        });
        channels.remove(incoming);
    }

    @Override
    protected void channelRead0(ChannelHandlerContext ctx, String msg) throws Exception {
        Channel incoming = ctx.channel();

        ChatMessage message = mapper.readValue(msg, ChatMessage.class);

        if (! message.getMessage().equals("")) {
            incoming.writeAndFlush("you: " + msg + "\n");
            channels.stream().filter(channel -> channel != incoming).forEach(channel -> {
                channel.writeAndFlush("[" + ctx.channel().remoteAddress() + "] " + msg + "\n");
            });
        }
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {
        cause.printStackTrace();
        ctx.close();
    }
}
