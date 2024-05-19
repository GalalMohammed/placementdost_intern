import requests

def download_image(url, save_path):
    """
    Downloads an image from the given URL and saves it to the specified save path.

    Args:
        url (str): The URL of the image to download.
        save_path (str): The path to save the downloaded image.
    """
    response = requests.get(url)
    print( response.status_code)
    if response.status_code == 200:
      with open(save_path, 'wb') as file:
        file.write(response.content)
      print("Image downloaded successfully!")
    else:
      print("Failed to download image.")
