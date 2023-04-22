from config import app
# from models import User


@app.route('/')
def root_route():
    return 'how you doin\n'



if __name__ =='__main__':
    app.run(port = 5555, debug = True)