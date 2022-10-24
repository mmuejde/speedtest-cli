from datetime import datetime as dt

from speedtest import Speedtest

test = Speedtest()
test_config = test.get_config().get('client')

print(f"Testing download and upload speed...")
download_speed = test.download()
download_speed = download_speed/1000000

upload_speed = test.upload()
upload_speed = upload_speed/1000000

with open(f'{dt.now()}.log', 'w+') as writer:
    writer.write(f"********** Results **********\n")
    writer.write(f"Your public IP: {test_config.get('ip')}\n")
    writer.write("Download Speed: {:.2f} Mbit/s\n".format(download_speed))
    writer.write("Upload Speed: {:.2f} Mbit/s".format(upload_speed))
