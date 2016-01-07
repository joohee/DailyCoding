package com.vtf.hotzil.utils;

import com.amazonaws.AmazonClientException;
import com.amazonaws.AmazonServiceException;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.sns.AmazonSNS;
import com.amazonaws.services.sns.AmazonSNSClient;
import com.amazonaws.services.sns.model.*;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.vtf.hotzil.domain.AbstractPushMessage;
import com.vtf.hotzil.domain.Device;
import com.vtf.hotzil.domain.support.DeviceType;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.env.Environment;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;
import org.springframework.stereotype.Component;

import javax.inject.Inject;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.security.InvalidParameterException;
import java.util.HashMap;
import java.util.Map;

@Component
public class PushUtil implements InitializingBean {
    private AmazonSNS snsClient;

    @Value("${cloud.aws.credentials.accessKey}")
    private String ACCESS_KEY;

    @Value("${cloud.aws.credentials.secretKey}")
    private String SECRET_KEY;

    @Value("${cloud.aws.sns.endpoint}")
    private String SNS_ENDPOINT;

    @Value("${push.gcm.serverKey}")
    private String SERVER_KEY;

    @Value("${push.appName}")
    private String APP_NAME;

    @Value("${push.apns.cert}")
    private String APNS_CERT_PATH;

    @Value("${push.apns.key}")
    private String APNS_KEY_PATH;

    @Value("${push.apns.sandbox}")
    private Boolean IS_APNS_SANDBOX;

    @Inject
    private Environment env;

    private String certificate;
    private String privateKey;

    private Logger logger = LoggerFactory.getLogger(PushUtils.class);

    private ObjectMapper objectMapper = JsonUtils.mapper();

    public Boolean sendMessage(Device device, AbstractPushMessage pushMessage) {
        return this.sendMessage(snsClient, device, pushMessage);
    }

    public Boolean sendMessage(String deviceType, String devicePushToken, AbstractPushMessage pushMessage) {
        return this.sendMessage(snsClient, deviceType, devicePushToken, pushMessage);
    }

    public Boolean sendGCM(String registrationId, AbstractPushMessage pushMessage) {
        return this.sendGCM(snsClient, registrationId, pushMessage);
    }

    public Boolean sendAPNS(String deviceToken, AbstractPushMessage pushMessage) {
        return this.sendAPNS(deviceToken, pushMessage);
    }

    private CreatePlatformApplicationResult createPlatformApplication(String applicationName, Platform platform, String principal, String credential) {
        return this.createPlatformApplication(snsClient, applicationName, platform, principal, credential);
    }

    private CreatePlatformEndpointResult createPlatformEndpoint(String customData, String platformToken, String applicationArn) {
        return this.createPlatformEndpoint(snsClient, customData, platformToken, applicationArn);
    }

    private void deletePlatformApplication(String applicationArn) {
        this.deletePlatformApplication(snsClient, applicationArn);
    }

    private void pushNotification(Platform platform, String principal, String credential, String platformToken, String applicationName, AbstractPushMessage pushMessage) {
        this.pushNotification(snsClient, platform, principal, credential, platformToken, applicationName, pushMessage);
    }

    private PublishResult publish(String endpointArn, Platform platform, AbstractPushMessage pushMessage) {
        return this.publish(snsClient, endpointArn, platform, pushMessage);
    }

    private String readFromResource(String path) throws IOException {
        Resource cert = new ClassPathResource(path);
        BufferedReader br = new BufferedReader(new InputStreamReader(cert.getInputStream()));
        StringBuffer sb = new StringBuffer(1024);
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append("\n");
        }
        return sb.toString();
    }

    public String jsonify(Object message) {
        try {
            return objectMapper.writeValueAsString(message);
        } catch (Exception e) {
            e.printStackTrace();
            throw (RuntimeException) e;
        }
    }

    private String getAppleMessage(AbstractPushMessage pushMessage) {
        Map<String, Object> appleMessageMap = new HashMap<>();
        Map<String, Object> appMessageMap = pushMessage.toMap();
        appMessageMap.put("sound", "default");
        appleMessageMap.put("aps", appMessageMap);
        return jsonify(appleMessageMap);
    }

    private String getAndroidMessage(AbstractPushMessage pushMessage) {
        Map<String, Object> androidMessageMap = new HashMap<>();
        androidMessageMap.put("collapse_key", "Welcome");
        androidMessageMap.put("data", pushMessage.toMap());
        androidMessageMap.put("delay_while_idle", true);
        androidMessageMap.put("time_to_live", 125);
        androidMessageMap.put("dry_run", false);
        return jsonify(androidMessageMap);
    }

    public static enum Platform {
        APNS,
        APNS_SANDBOX,
        GCM,
    }

      // SNS Client를 지정하는 방식 추가.

    private CreatePlatformApplicationResult createPlatformApplication(AmazonSNS snsClient, String applicationName, Platform platform, String principal, String credential) {
        CreatePlatformApplicationRequest platformApplicationRequest = new CreatePlatformApplicationRequest();
        Map<String, String> attributes = new HashMap<>();
        attributes.put("PlatformPrincipal", principal);
        attributes.put("PlatformCredential", credential);
        platformApplicationRequest.setAttributes(attributes);
        platformApplicationRequest.setName(applicationName);
        platformApplicationRequest.setPlatform(platform.name());
        return snsClient.createPlatformApplication(platformApplicationRequest);
    }

    private CreatePlatformEndpointResult createPlatformEndpoint(AmazonSNS snsClient, String customData, String platformToken, String applicationArn) {
        CreatePlatformEndpointRequest platformEndpointRequest = new CreatePlatformEndpointRequest();
        platformEndpointRequest.setCustomUserData(customData);
        platformEndpointRequest.setToken(platformToken);
        platformEndpointRequest.setPlatformApplicationArn(applicationArn);
        return snsClient.createPlatformEndpoint(platformEndpointRequest);
    }

    private void deletePlatformApplication(AmazonSNS snsClient, String applicationArn) {
        DeletePlatformApplicationRequest request = new DeletePlatformApplicationRequest();
        request.setPlatformApplicationArn(applicationArn);
        snsClient.deletePlatformApplication(request);
    }

    private void pushNotification(AmazonSNS snsClient, Platform platform, String principal, String credential, String platformToken, String applicationName, AbstractPushMessage pushMessage) {
        // Create Platform Application. This corresponds to an app on a platform.
        CreatePlatformApplicationResult platformApplicationResult = createPlatformApplication(snsClient, applicationName, platform, principal, credential);
        logger.info(platformApplicationResult.toString());

        // The Platform Application Arn can be used to uniquely identify the Platform Application.
        String platformApplicationArn = platformApplicationResult.getPlatformApplicationArn();

        // Create an Endpoint. This corresponds to an app on a device.
        CreatePlatformEndpointResult platformEndpointResult = createPlatformEndpoint(snsClient, "CustomData - Useful to store endpoint specific data", platformToken, platformApplicationArn);
        logger.info(platformEndpointResult.toString());

        // Publish a push notification to an Endpoint.
        PublishResult publishResult = publish(snsClient, platformEndpointResult.getEndpointArn(), platform, pushMessage);
        logger.info("Published! \n{MessageId=" + publishResult.getMessageId() + "}");
        // Delete the Platform Application since we will no longer be using it.
        deletePlatformApplication(snsClient, platformApplicationArn);

    }

    private PublishResult publish(AmazonSNS snsClient, String endpointArn, Platform platform, AbstractPushMessage pushMessage) {
        PublishRequest publishRequest = new PublishRequest();
        publishRequest.setMessageStructure("json");
        String message = "";
        switch (platform) {
            case APNS:
            case APNS_SANDBOX:
                message = getAppleMessage(pushMessage);
                break;
            case GCM:
                message = getAndroidMessage(pushMessage);
                break;
        }

        Map<String, String> messageMap = new HashMap<>();
        messageMap.put(platform.name(), message);
        message = jsonify(messageMap);
        publishRequest.setTargetArn(endpointArn);

        logger.info("{Message Body: " + message + "}");
        publishRequest.setMessage(message);
        return snsClient.publish(publishRequest);
    }

    public Boolean sendMessage(AmazonSNS snsClient, Device device, AbstractPushMessage pushMessage) {
        if (DeviceType.I.equals(device.getType())) {
            return sendAPNS(snsClient, device.getPushToken(), pushMessage);
        } else if (DeviceType.A.equals(device.getType())) {
            return sendGCM(snsClient, device.getPushToken(), pushMessage);
        } else {
            logger.error("[Source] Device Type is incorrect...{}, device: {}, pushMessage: {}", device.getType(), device.toString(), pushMessage.toString());
            return false;
        }
    }

    public Boolean sendMessage(AmazonSNS snsClient, String deviceType, String devicePushToken, AbstractPushMessage pushMessage) {
        if ("I".equals(deviceType.toUpperCase())) {
            return sendAPNS(snsClient, devicePushToken, pushMessage);
        } else if ("A".equals(deviceType.toUpperCase())) {
            return sendGCM(snsClient, devicePushToken, pushMessage);
        } else {
            logger.error("[Source] Device Type is incorrect...{}, device Token: {}, pushMessage: {}", deviceType, devicePushToken, pushMessage.toString());
            return false;
        }
    }

    public Boolean sendGCM(AmazonSNS snsClient, String registrationId, AbstractPushMessage pushMessage) {
        try {
            this.pushNotification(snsClient, Platform.GCM, "", SERVER_KEY, registrationId, APP_NAME, pushMessage);
        } catch (EndpointDisabledException ede) {
            logger.error("cause: " + ede.getCause(), ", message: " + ede.getMessage());
            logger.error("[Source] registrationId: {}, pushMessage: {}", registrationId, pushMessage.toString());
            return false;

        } catch (InvalidParameterException ipe) {
            logger.error("invalid parameter exception happened.");
            logger.error("cause: " + ipe.getCause(), ", message: " + ipe.getMessage());
            logger.error("[Source] registrationId: {}, pushMessage: {}", registrationId, pushMessage.toString());

            return false;
        } catch (AmazonServiceException ase) {
            logger.error("Caught an AmazonServiceException, which means your request made it "
                    + "to Amazon SNS, but was rejected with an error response for some reason.");
            logger.error("Error Message:    " + ase.getMessage());
            logger.error("HTTP Status Code: " + ase.getStatusCode());
            logger.error("AWS Error Code:   " + ase.getErrorCode());
            logger.error("Error Type:       " + ase.getErrorType());
            logger.error("Request ID:       " + ase.getRequestId());
            logger.error("[Source] registrationId: {}, pushMessage: {}", registrationId, pushMessage.toString());

            return false;
        } catch (AmazonClientException ace) {
            logger.error("Caught an AmazonClientException, which means the client encountered "
                    + "a serious internal problem while trying to communicate with SNS, such as not "
                    + "being able to access the network.");
            logger.error("Error Message: " + ace.getMessage());
            logger.error("[Source] registrationId: {}, pushMessage: {}", registrationId, pushMessage.toString());
            return false;
        }
        return true;
    }


    public Boolean sendAPNS(AmazonSNS snsClient, String deviceToken, AbstractPushMessage pushMessage) {
        Platform platform;

        if (Boolean.TRUE.equals(IS_APNS_SANDBOX)) {
            platform = Platform.APNS_SANDBOX ;
        } else {
            platform = Platform.APNS;
        }

        try {
            this.pushNotification(snsClient, platform, certificate, privateKey, deviceToken, APP_NAME, pushMessage);
        } catch (EndpointDisabledException ede) {
            logger.error("cause: " + ede.getCause(), ", message: " + ede.getMessage());
            logger.error("[SOURCE] deviceToken: {}, pushMessage: {}", deviceToken, pushMessage.toString());
            return false;

        } catch (InvalidParameterException ipe) {
            logger.error("invalid parameter exception happened.");
            logger.error("cause: " + ipe.getCause(), ", message: " + ipe.getMessage());
            logger.error("[SOURCE] deviceToken: {}, pushMessage: {}", deviceToken, pushMessage.toString());

            return false;
        } catch (AmazonServiceException ase) {
            logger.error("Caught an AmazonServiceException, which means your request made it "
                    + "to Amazon SNS, but was rejected with an error response for some reason.");
            logger.error("Error Message:    " + ase.getMessage());
            logger.error("HTTP Status Code: " + ase.getStatusCode());
            logger.error("AWS Error Code:   " + ase.getErrorCode());
            logger.error("Error Type:       " + ase.getErrorType());
            logger.error("Request ID:       " + ase.getRequestId());
            logger.error("[SOURCE] deviceToken: {}, pushMessage: {}", deviceToken, pushMessage.toString());

            return false;
        } catch (AmazonClientException ace) {
            logger.error("Caught an AmazonClientException, which means the client encountered "
                    + "a serious internal problem while trying to communicate with SNS, such as not "
                    + "being able to access the network.");
            logger.error("Error Message: " + ace.getMessage());
            logger.error("[SOURCE] deviceToken: {}, pushMessage: {}", deviceToken, pushMessage.toString());
            return false;
        }
        return true;
    }

    @Override
    public void afterPropertiesSet() throws Exception {
        AWSCredentials credentials = new BasicAWSCredentials(ACCESS_KEY, SECRET_KEY);
        snsClient = new AmazonSNSClient(credentials);
        snsClient.setEndpoint(SNS_ENDPOINT);

        certificate = readFromResource(APNS_CERT_PATH);
        privateKey = readFromResource(APNS_KEY_PATH);
    }



}

