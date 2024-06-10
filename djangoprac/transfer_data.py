import pymongo
from Paytm.models import User, Account
import django
import os

# Ensure the Django environment is set up
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoprac.settings')
django.setup()

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['paytm']

# Fetch users from MongoDB
mongo_users = db.users.find()
user_map = {}

# Transfer users to Django
for mongo_user in mongo_users:
    try:
        user, created = User.objects.get_or_create(
            username=mongo_user['username'].strip().lower(),
            defaults={
                'password': mongo_user['password'],
                'first_name': mongo_user.get('firstname', '').strip(),
                'last_name': mongo_user.get('lastname', '').strip()
            }
        )
        user_map[mongo_user['_id']] = user
    except Exception as e:
        print(f"Error importing user {mongo_user['username']}: {e}")

# Fetch accounts from MongoDB
mongo_accounts = db.accounts.find()

# Transfer accounts to Django
for mongo_account in mongo_accounts:
    try:
        user_id = mongo_account['userId']
        user = user_map.get(user_id)
        if user:
            Account.objects.get_or_create(
                user=user,
                defaults={'balance': mongo_account['balance']}
            )
    except Exception as e:
        print(f"Error importing account for user {user_id}: {e}")

print("Data transfer complete.")
