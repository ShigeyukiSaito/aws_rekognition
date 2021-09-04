#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

#あらかじめS3に保存した画像から、URLを抽出する。

import boto3
import webbrowser

def detect_text(photo, bucket):

    client=boto3.client('rekognition')

    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                        
    textDetections=response['TextDetections']
    print ('Detected text\n----------')

    url=''
    check=False

    for text in textDetections:

        if text['Type'] == 'LINE':
            if text['DetectedText'].startswith('http://') or text['DetectedText'].startswith('https://'):
                if check==False:
                    url += text['DetectedText']
                    # print (url)
                    check=True
                    '''
                    print ('Detected text:' + text['DetectedText'])
                    print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
                    print ('Id: {}'.format(text['Id']))
                    if 'ParentId' in text:
                        print ('Parent Id: {}'.format(text['ParentId']))
                    print ('Type:' + text['Type'])
                    print()
                    '''
            elif check==True :
                url += text['DetectedText']
                #　ファイルの拡張子で終端を特定
                if text['DetectedText'].endswith('/') or text['DetectedText'].endswith('.html') or text['DetectedText'].endswith('.pdf'):
                    return url
                # ここから独自の処理

    #return len(textDetections)

def main():

    bucket='url-detection'
    photo='32284.jpg'
    text_count=detect_text(photo,bucket)
    # print("Text detected: " + str(text_count))
    print("URL: " + str(text_count))
    browser = webbrowser.get('chrome')
    browser.open(text_count)


if __name__ == "__main__":
    main()