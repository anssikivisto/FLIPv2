import os
import urllib.request
import re

WORDS = [
    "dog", "cat", "bear", "lion", "rabbit", "fox", "elephant", "monkey", "bird", "duck", 
    "horse", "pig", "frog", "fish", "owl", "wolf", "mouse", "turtle", "bee", "butterfly", 
    "penguin", "dolphin", "giraffe", "koala", "tiger", "apple", "banana", "pizza", "milk", 
    "bread", "cheese", "ice cream", "strawberry", "carrot", "cake", "cookie", "water", 
    "orange", "watermelon", "egg", "chicken", "hamburger", "fries", "donut", "candy", 
    "pineapple", "grapes", "corn", "pancake", "honey", "face", "eye", "eyes", "ear", 
    "nose", "mouth", "lips", "tongue", "tooth", "hair", "brain", "heart", "lungs", 
    "bone", "hand", "finger", "thumb", "arm", "leg", "foot", "skull", "baby", "beard", 
    "footprint", "nail", "shirt", "jeans", "dress", "shoe", "boot", "high heels", "socks", 
    "hat", "cap", "gloves", "scarf", "coat", "glasses", "sunglasses", "crown", "ring", 
    "backpack", "handbag", "purse", "tie", "shorts", "swimsuit", "bikini", "sandal", "top", 
    "tree", "flower", "sun", "moon", "star", "cloud", "rain", "snow", "rainbow", "mountain", 
    "volcano", "wave", "leaf", "fire", "rock", "wood", "cactus", "mushroom", "plant", 
    "clover", "palm tree", "pine tree", "desert", "earth", "tornado", "book", "pencil", 
    "pen", "notebook", "pencil case", "ruler", "scissors", "computer", "paper", "crayon", 
    "paint", "school", "class", "teacher", "pupil", "bus", "maths", "music", "art", 
    "sport", "read", "write", "draw", "listen", "bell"
]

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '_', text.lower()).strip('_')

os.makedirs("images", exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'image/svg+xml,image/*,*/*'
}

print("Ladataan kuvakkeita...")
success_count = 0

for word in set(WORDS):
    file_name = f"{slugify(word)}.svg"
    save_path = os.path.join("images", file_name)
    icon_query = word.lower().replace(" ", "-")
    
    urls = [
        f"https://raw.githubusercontent.com/iconify/icon-sets/master/svg/fluent-emoji-flat/{icon_query}.svg",
        f"https://api.iconify.design/fluent-emoji-flat/{icon_query}.svg"
    ]
    
    downloaded = False
    for url in urls:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response, open(save_path, 'wb') as out_file:
                out_file.write(response.read())
            print(f"✓ Ladattu: {file_name}")
            success_count += 1
            downloaded = True
            break
        except Exception:
            continue
    
    if not downloaded:
        print(f"✗ Virhe sanalle '{word}'")

print(f"\nValmis! Ladattiin {success_count}/{len(set(WORDS))} kuvaketta kansioon '/images'.")
