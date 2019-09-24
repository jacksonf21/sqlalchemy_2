import boto3
import re

def detect_text(photo, bucket):

    client=boto3.client('rekognition')

    response=client.detect_text(Image={'S3Object':{'Bucket': bucket,'Name': photo}})
                        
    textDetections=response['TextDetections']
    ret_arr = []
    
    # print ('Detected text\n----------')
    for text in textDetections:
            # print ('Detected text:' + text['DetectedText'])
            # print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            # print ('Id: {}'.format(text['Id']))
            # if 'ParentId' in text:
            #     print ('Parent Id: {}'.format(text['ParentId']))

            if (bool(text['Type'] == 'LINE')):
                line_item = {}
                
                try:
                    price = re.search('[0-9]*\.[0-9]{2}', text['DetectedText']).group()
                    quantity = re.search('[1-9]*\s', text['DetectedText']).group().strip()
                    item_sub = re.sub(price, '', text['DetectedText'])
                    item = re.sub(quantity, '', item_sub)

                    line_item['quantity'] = quantity 
                    line_item['item'] = item
                    line_item['price'] = price

                    ret_arr.append(line_item)
                except:
                    pass

    return ret_arr
    # return len(textDetections)



# for running aws_rekog directly uncomment below
# def main():

#     bucket='bucket'
#     photo='photo'
#     # text_count=detect_text(photo,bucket)
#     # print("Text detected: " + str(text_count))


# if __name__ == "__main__":
#     main()