from src.webserver import app 
#de src\webserver.py importa app

#app.run(debug=True);
#ejecuta app, con debugger

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)