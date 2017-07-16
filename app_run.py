from app import create_app

app = create_app()


def init_db():
    from app.ext.db import model
    try:
        print("---initdb---")
        from app.model.user import User
        from app.model.cdn import Cdn
        from app.model.resource import Resource
        model.metadata.create_all()
    except Exception as e:
        print(e)


init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, workers=3, debug=app.config.get("DEBUG"))
