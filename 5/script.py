import docker
import json
from datetime import datetime

client = docker.from_env()
# Look for all images that have litecoin as a repository name
for image in client.images.list("litecoin", True):
# format date and remove useless caracters
  formatCreatedDate = image.attrs['Created'].replace('T',' ').replace('Z','').split('.')[0]
  # Calculate the difference between now and the creation date of the image
  Diff = datetime.now() - datetime.strptime(formatCreatedDate, "%Y-%m-%d %H:%M:%S")
  DurationInHours = Diff.total_seconds()/3600
  print(DurationInHours)
  # Check if the duration is between 4 and 8 hours
  if  DurationInHours > 4 and DurationInHours < 8:
    try:
        # Delete the image if not used
        client.images.remove(image.id)
        print("Image "+ image.id +" deleted")
    except:
        # Iterate to the next image
        print("Image "+ image.id +" not deleted")
        continue
