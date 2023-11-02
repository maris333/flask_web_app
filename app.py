from src import create_app, create_db

if __name__ == "__main__":
    app = create_app()
    create_db(app)
    app.run(debug=True, port=5000)
