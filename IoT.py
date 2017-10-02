#!/usr/bin/python
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
# Edit this to be the awshost you got from `aws iot describe-endpoint`
awshost = "a14iqywcdjr3cu.iot.us-east-1.amazonaws.com"
# Edit this to be your device name in the AWS IoT console
thing = "test"
if __name__ == "__main__":
    # define your variables
    awsport = 8883
    caPath = "aws-iot-rootCA.crt"
    certPath = "cert.pem"
    keyPath = "privkey.pem"
    # Set up the shadow client
    myShadowClient = AWSIoTMQTTShadowClient(thing)
    myShadowClient.configureEndpoint(awshost, awsport)
    myShadowClient.configureCredentials(caPath, keyPath, certPath)
    myShadowClient.configureConnectDisconnectTimeout(60)
    myShadowClient.configureMQTTOperationTimeout(10)
    myShadowClient.connect()
    myDeviceShadow = myShadowClient.createShadowHandlerWithName("test", True)
    # You can implement a custom callback function if you like, but once working I didn't require one. We still need to define it though.
    customCallback = "" 
    # The main loop
    while 1==1:
        # Create our payload in JSON format
        tempreading = "{ \"state\" : { \"reported\": { \"temp\": \"%s\", \"humid\": \"%s\" } } }"
        # Print the result just for some debugging
        print("payload: %s" % tempreading)
        myDeviceShadow.shadowUpdate(tempreading, customCallback, 5)
        # Wait a minute before updating again, you can lower this for debug purposes
        time.sleep(60)