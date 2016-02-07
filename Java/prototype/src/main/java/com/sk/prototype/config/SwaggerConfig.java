package com.sk.prototype.config;

import com.mangofactory.swagger.configuration.SpringSwaggerConfig;
import com.mangofactory.swagger.models.dto.ApiInfo;
import com.mangofactory.swagger.plugin.EnableSwagger;
import com.mangofactory.swagger.plugin.SwaggerSpringMvcPlugin;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.inject.Inject;

/**
 * Created by skplanet on 15. 1. 16..
 */
@Configuration
@EnableSwagger
public class SwaggerConfig {

    @Inject
    private SpringSwaggerConfig springSwaggerConfig;

    @Bean
    public SwaggerSpringMvcPlugin swaggerSpringMvcPlugin() {
        return new SwaggerSpringMvcPlugin(this.springSwaggerConfig)
                .apiInfo(apiInfo());
                //.includePatterns(".*prototype.*");
    }

    private ApiInfo apiInfo() {
        ApiInfo apiInfo = new ApiInfo(
                "Prototype Apps API Title",
                "Prototype Apps API Description",
                "Prototype Apps API terms of service",
                "Prototype Apps API Contact Email",
                "Prototype Apps API Licence Type",
                "Prototype Apps API License URL"
        );
        return apiInfo;
    }
}
