from flask import Flask



todos = [{"todo": "sample todo", "done": False}]


def main():
    from views import views
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix="/")
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()
