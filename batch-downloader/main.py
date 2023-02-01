import wget
import os

folder_path = 'C:\\Users\\Ryou\\Pictures\\neru_nagahama\\hitoiro'
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

number = 50

for i in range(1, number+1):
    if i < 10:
        index = '0'+str(i)
    else:
        index = str(i)

    path = f'{folder}\\neru_img{index}.jpg'
    url = f'https://hito-iro.jp/wp/wp-content/uploads/2023/01/neru-nagahama_{index}.jpg'
    print(f"\nDownlaoing img{index}")
    wget.download(url, path)

print("\n--- Downloading Completed. ^_^ ---")