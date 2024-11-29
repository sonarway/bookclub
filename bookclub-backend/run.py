from app import create_app

# Создание приложения
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000) # дефолтный порт фласка, но у меня без explicit сетапа не работало
