"""
Script to replace image URLs in markdown document with self-hosted images.
"""

# Steps involved
# 1. Get a list of all image URLs from given markdown file 
#   file (given via command line argument or to iterate through files in a directory)
# 2. Check if the files are reachable and are images
# 3. Download the image
# 4. Upload the image to Internet where image can be served from
# todo get a domain name that can be used forever?
# todo decide where to host the images - Amazon S3 bucket or simple web host or VPN at DigitalOcean
# ! can Github be used - now that it offers free private repositories


import re
import my_module
import sys
import requests
import os
from urllib.parse import urlparse

def is_image_downloadable(link):
    """Returns whether image is downloadable or not
    """
    pass

def main(file_path):
    
    # read file
    # extract image links (this should happen in a function)
    # download image (this should happen in a function)
    # upload image to github repository (how is this to be done with os level installations?) (this should certainly happen in a function)
    # obtain or create link to uploaded file (prev function should return the url of the recently uploaded image)
    # replace the original link in the file with this new link to uploaded file
    # save the file to a new file for test purposes
    
    script_dir = my_module.cd_to_script_dir()
    markdown_file = file_path
    # get file basename without extension - https://stackoverflow.com/questions/4444923/get-filename-without-extension-in-python/4444952
    file_basename = os.path.splitext(markdown_file)[0]
    # if len(file_basename) > 20: # reduce the file basename
    #     file_basename = file_basename[:20]

    output_file = script_dir + '/' + 'test_output_file.md'
    with open(markdown_file, 'r') as f:
        markdown_text = f.read()

    # setup pattern to search for url
    # the pattern in action here - https://regex101.com/r/v6ZFhQ/1
    pattern = r'(?P<before_url>!\[[^\]]*\]\()(?P<url>.*?)(?P<trailing>\s*("(?:.*[^"])")?\s*\))' # this pattern will find url and then text in quotes. Returns a tuple.
    regex = re.compile(pattern)
    new_text = ''
    for line in markdown_text.splitlines():
        # search_result = regex.findall(line) # this results in a list with all groups
        # instead trying the match option as that seems to have a more powerful output
        # more details of how this will work is here - https://stackoverflow.com/a/1800907 from [How can I get part of regex match as a variable in python? - Stack Overflow](https://stackoverflow.com/questions/1800817/how-can-i-get-part-of-regex-match-as-a-variable-in-python)
        search_result = regex.match(line)
        if search_result:
            url = search_result.groupdict().get('url')
            print("line is {}".format(line))
            print('url portion is {}'.format(url))
            # now need to download this image to local computer
            r=requests.get(url) # download the image file
            if r.status_code == 200 : # image exists, let us save it and upload it to target directory and change the line
                # extract image name
                a = urlparse(url)
                image_name = os.path.basename(a.path)
                # save the image to local folder
                # urllib.request.urlretrieve(image["url"], image_name) # ! Can requests library accomplish this?
                with open(image_name, 'wb') as f:
                    f.write(r.content)
                # now upload this file to github, to our target directory
                # name of file is image_name
                
                # now clean up by deleting the image file that was downloaded

                
                # if successfully uploaded, then change the line in the markdown file
                if successfully_uploaded:
                    # enter the desired url by string formating
                    modified_line = regex.sub(r'\g<before_url>https://i.imgur.com/MJfIe7y.jpg\g<trailing>', line)
                print("Modified line is {}".format(modified_line))
                line = modified_line
        new_text = new_text + line + "\n"
    with open(output_file, 'w') as f:
        f.write(new_text)


if __name__ == "__main__":
    my_module.cd_to_script_dir()
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # set a default markdown file for testing purposes
        file_path = './test.md'
    main(file_path)
