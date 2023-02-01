import wget
import os

folder_path = 'C:\\Users\\Pictures\\img'
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

number = 50

for i in range(1, number+1):
    if i < 10:
        index = '0'+str(i) #个位数前加'0'
    else:
        index = str(i)

    path = f'{folder}\\neru_img{index}.jpg'
    url = f'https://xxxx.com/xxxxx/xxxx/ooxx_img_{index}.jpg'
    print(f"\nDownlaoing img{index}")
    wget.download(url, path)

print("\n--- Downloading Completed. ^_^ ---")
