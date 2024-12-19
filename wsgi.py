from app import app
import os


if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    app.run(port=port)
