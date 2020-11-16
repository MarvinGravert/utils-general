from decouple import config

PORT = config("PORT", cast=str, default="50051")
