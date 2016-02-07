package com.sk.prototype.scheduler.crawl;

import com.google.api.client.googleapis.json.GoogleJsonResponseException;
import com.google.api.client.http.HttpRequest;
import com.google.api.client.http.HttpRequestInitializer;
import com.google.api.client.http.HttpTransport;
import com.google.api.client.http.javanet.NetHttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.services.youtube.YouTube;
import com.google.api.services.youtube.model.ResourceId;
import com.google.api.services.youtube.model.SearchListResponse;
import com.google.api.services.youtube.model.SearchResult;
import com.google.api.services.youtube.model.Thumbnail;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.Iterator;
import java.util.List;

/**
 * Created by skplanet on 14. 12. 31..
 */
@Service
public class YoutubeCrawler {
    private static Logger logger = LoggerFactory.getLogger(YoutubeCrawler.class);

    @Value("${youtube.apikey}")
    private String youtubeApiKey;

    /** Global instance of the HTTP transport. */
    private static final HttpTransport HTTP_TRANSPORT = new NetHttpTransport();

    /** Global instance of the JSON factory. */
    private static final JsonFactory JSON_FACTORY = new JacksonFactory();

    /** Global instance of the max number of videos we want returned (50 = upper limit per page). */
    private static final long NUMBER_OF_VIDEOS_RETURNED = 25;

    /** Global instance of Youtube object to make all API requests. */
    private static YouTube youtube;

    @Async
    public void search() {

        try {
            youtube = new YouTube.Builder(HTTP_TRANSPORT, JSON_FACTORY, new HttpRequestInitializer() {
                public void initialize(HttpRequest request) throws IOException {}
            }).setApplicationName("youtube-vtf-search").build();

            // Get query term from user.
            // TODO : modify
            String queryTerm = "beauty";

            YouTube.Search.List search = youtube.search().list("id,snippet");
            search.setKey(youtubeApiKey);
            search.setQ(queryTerm);
            search.setType("video");
            // TODO 날짜 range 제한이 필요하다면 체크.
            //search.setPublishedAfter(new DateTime(new Date().getTime()));
            search.setFields("items(id/kind,id/videoId,snippet/title,snippet/thumbnails/default/url,snippet/publishedAt)");
            search.setMaxResults(NUMBER_OF_VIDEOS_RETURNED);
            SearchListResponse searchResponse = search.execute();

           List<SearchResult> searchResultList = searchResponse.getItems();
            if (searchResultList != null) {
                //prettyPrint(searchResultList.iterator(), queryTerm);
                logger.info("execute complete...");
            }
        } catch (GoogleJsonResponseException e) {
            logger.error("There was a service error: " + e.getDetails().getCode() + " : "
                    + e.getDetails().getMessage());
        } catch (IOException e) {
            logger.error("There was an IO error: " + e.getCause() + " : " + e.getMessage());
        } catch (Throwable t) {
            t.printStackTrace();
        }

    }

    private static void prettyPrint(Iterator<SearchResult> iteratorSearchResults, String query) {

        logger.info("\n=============================================================");
        logger.info(
                "   First " + NUMBER_OF_VIDEOS_RETURNED + " videos for search on \"" + query + "\".");
        logger.info("=============================================================\n");

        if (!iteratorSearchResults.hasNext()) {
            logger.info(" There aren't any results for your query.");
        }

        while (iteratorSearchResults.hasNext()) {

            SearchResult singleVideo = iteratorSearchResults.next();
            ResourceId rId = singleVideo.getId();

            // Double checks the kind is video.
            if (rId.getKind().equals("youtube#video")) {
                Thumbnail thumbnail = (Thumbnail) singleVideo.getSnippet().getThumbnails().get("default");

                logger.info(" Video Id" + rId.getVideoId());
                logger.info(" Title: " + singleVideo.getSnippet().getTitle());
                logger.info(" Thumbnail: " + thumbnail.getUrl());
                logger.info(" Published: " + singleVideo.getSnippet().getPublishedAt());
                logger.info("\n-------------------------------------------------------------\n");
            }
        }
    }
}
