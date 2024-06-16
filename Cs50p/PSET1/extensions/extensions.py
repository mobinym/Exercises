import mimetypes

filename = input("Enter filename: ")
filename = filename.strip()
media_type = mimetypes.guess_type(filename)[0]

if media_type:
    print(media_type)
else:
    print("application/octet-stream")