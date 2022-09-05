"""
| __filename__ = "app.py"
| __coursename__ = "SDEV 400 - Secure Programming in the Cloud"
| __author__ = "Eddy Owings"
| __copyright__ = "None"
| __credits__ = ["Eddy Owings"]
| __license__ = "GPL"
| __version__ = "1.0.0"
| __maintainer__ = "Eddy Owings"
| __email__ = "eowings@student.umgc.edu"
| __status__ = ""

--For this assignment use your Cloud9 environment, to create a Python based interactive
menu-driven application. The following components or functionality must be present in
your application:
1. Uses at least one DynamoDB table
2. Uses at least one S3 bucket
3. Includes a Menu driven interface with at least 6 menu items.
4. Provides a user guide showing how to use the application, explains how the
concept for your application was developed, and provides detailed testing for
all components and functions used in your application
"""
import os
import logging
import datetime
import boto3
import imageio
from boto3.dynamodb.conditions import Key
from cloudpathlib import CloudPath
from PIL import Image, ImageDraw

def make_gif():
    """
    Makes a large gif file from the collected images then deletes images
    """
    c_p = CloudPath("s3://eowings-esp32uploadimages/images/9C:9C:1F:C9:00:20/")
    c_p.download_to("Images")
    jpg_dir = 'Images'
    images = []
    for file_name in sorted(os.listdir(jpg_dir)):
        if file_name.endswith('.jpg'):
            file_path = os.path.join(jpg_dir, file_name)
            images.append(imageio.imread(file_path))
    imageio.mimsave('movie.gif', images, fps=55)
    for _f in os.listdir(jpg_dir):
        os.remove(os.path.join(jpg_dir, _f))

def query_table_newest():
    """Looks up data in table based on newest entry"""
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('eowings_temp_humid')
    data = []
    response = table.scan()
    k = 0
    for i in response['Items']:
        sample_time = response['Items'][k]['sample_time']
        sample_time = int(sample_time) / 1000
        data.append("|{:<20} |{:<10} |{:<15} |{:<10}".format
                    (datetime.datetime.fromtimestamp(sample_time).strftime('%Y-%m-%d %H:%M:%S'),
                     i['device_id'], i['device_data']['temperature'],
                     i['device_data']['humidity']))
        k = k+1
    data.sort()
    print("*"*75)
    print("The latest temp and humidity data is:")
    print("-"*75)
    print("|{:<20} |{:<10} |{:<15} |{:<10}".format('sample_time',
                                                   'device_id', 'temperature', 'humidity'))
    lastest_date = max(data)
    print(lastest_date)
    print("*"*75)


def query_table_all():
    """shows all data in table"""
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('eowings_temp_humid')
    data = []
    response = table.scan()
    k = 0
    for i in response['Items']:
        sample_time = response['Items'][k]['sample_time']
        sample_time = int(sample_time) / 1000
        data.append("|{:<20} |{:<10} |{:<15} |{:<10}".format
                    (datetime.datetime.fromtimestamp(sample_time).strftime('%Y-%m-%d %H:%M:%S'),
                     i['device_id'], i['device_data']['temperature'],
                     i['device_data']['humidity']))
        k = k+1
    data.sort()
    print("*"*75)
    print("All Temp and Humidity data from oldest to newest:")
    print("-"*75)
    print("|{:<20} |{:<10} |{:<15} |{:<10}".format('sample_time',
                                                   'device_id', 'temperature', 'humidity'))
    print(*data, sep='\n')
    print("*"*75)

def find_a_photo_temp(photo_date):
    """
    Takes in date from photo and returns a date

    :param selection(str): Value string to validate
    :rtype: **bool**
    :return: **valid_input(str)**: Returns date in millisecond format to\
    be pulled from DynamoDB to be printed onto image to show the temp\
    and humidity when that image was taken.
    """
    size = len(photo_date)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('eowings_temp_humid')
    data = []
    response = table.scan()
    for i in response['Items']:
        data.append(i['sample_time'])
    for i in range(0, len(data)):
        data[i] = str(data[i])
    check = photo_date[:size -4]
    res = [idx for idx in data if idx.startswith(check)]
    photo_date = max(res)
    photo_date = int(photo_date)
    response_two = table.query(KeyConditionExpression=Key('sample_time').eq(photo_date))
    photo_data = []
    for i in response_two['Items']:
        photo_data.append("Temperature: {} Humidity: {}".format(i['device_data']['temperature'],
                                                                i['device_data']['humidity']))
    photo_data_str = ""
    return photo_data_str.join(photo_data)

def recent_photo_function():
    """
    Finds the most recent photo then pulls date data from photo name./
    then sends that data to find_a_phot_temp function, then uses the/
    returned product to transcribe temp and humidity to photo using pillow.
    """
    file_image = []
    image = []
    prefix = "images/9C:9C:1F:C9:00:20/"
    s_3 = boto3.resource("s3", region_name="us-east-1")
    bucket = s_3.Bucket('eowings-esp32uploadimages')
    res = bucket.objects.filter(Prefix=prefix)
    for obj in res:
        image.append("{}".format(obj.last_modified))
        file_image.append("{},{}".format(obj.key, obj.last_modified))
    newest = max(image)
    newest_image = ""
    for line in file_image:
        if newest in line:
            newest_image = line
    newest_image = newest_image.split(",", 1)[0]
    newest_image = newest_image.split("/", 1)[1]
    newest_image = newest_image.split("/", 1)[1]
    print("Downloaded Image: "+ newest_image)
    cloudpath_item = "s3://eowings-esp32uploadimages/images/9C:9C:1F:C9:00:20/"+newest_image
    c_p = CloudPath(cloudpath_item)
    c_p.download_to("")
    my_image = Image.open(newest_image)
    photo_date = newest_image = newest_image.split(".", 1)[0]
    photo_text = find_a_photo_temp(photo_date)
    title_text = photo_text
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((15, 15), title_text, (237, 230, 211))
    my_image.save("Newest_image_with_weather.jpg")

def avg_temp_function():
    """
    Prints the AVG temp and humidity.
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('eowings_temp_humid')
    temp = []
    humid = []
    response = table.scan()
    k = 0
    for i in response['Items']:
        temp.append(i['device_data']['temperature'])
        humid.append(i['device_data']['humidity'])
        k = k+1
    temp = list(map(float, temp))
    humid = list(map(float, humid))
    temp_avg = sum(temp)/k
    humid_avg = sum(humid)/k
    temp_avg = str(int(temp_avg))
    humid_avg = str(int(humid_avg))
    temp_avg = "Temperature : " + temp_avg
    humid_avg = "Humidity : " + humid_avg

    print("*"*75)
    print("Average Temp and Humidity.")
    print("-"*75)
    print(temp_avg)
    print(humid_avg)
    print("*"*75)

    # Main Menu Function
def menu_function():
    """
    Main Menu Function
    """
    menu = True
    while menu:
        print("""
What would you like to do today?
1.	Latest temp and humidity.
2.	List all temps collected sorted oldest to newest.
3.	Average temperature and humidity.
4.	Most recent photo taken with temp/humidity overlay.
5.	timelapse gif of all images (100MB file).
q.	Exit.
        """)
        menu = input("")
        if menu == "1":
            print("You have entered 1.")
            query_table_newest()
        elif menu == "2":
            print("\nYou have entered 2.")
            query_table_all()
        elif menu == "3":
            print("\nYou have entered 3.")
            avg_temp_function()
        elif menu == "4":
            print("\nYou have entered 4.")
            recent_photo_function()
        elif menu == "5":
            print("\nYou have entered 5.")
            print("\nThis could take a minute or two...")
            make_gif()
        elif menu == "q":
            menu = False
        else:
            print("\nNot Valid Choice Try again")
# End Main Menu Function

logging.basicConfig(filename="homework_four.log", level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s: %(message)s')
print("*"*75)
print("Welcome to the Python SDEV400 Homework 8 Application.")
print("*"*75)
menu_function()
