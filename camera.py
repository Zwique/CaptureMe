import os

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if not os.path.exists('photos'):
    os.makedirs('photos')

def get_next_photo_index():
    existing_files = os.listdir('photos')
    max_index = 0

    for file in existing_files:
        if file.startswith('captured_photo') and file.endswith('.jpg'):
            try:
                index = int(file[len('captured_photo'):len(file) - len('.jpg')])
                max_index = max(max_index, index)
            except ValueError:
                continue

    return max_index + 1

def save_photo(photo):
    if photo and allowed_file(photo.filename):
        photo_index = get_next_photo_index()
        filename = os.path.join('photos', f"captured_photo{photo_index}.jpg")
        photo.save(filename)
        return filename
    return None
