# Guest Book

(Flask + Vue.js app)


#### Run the app:

  1. Start a server:

```
    cd guest-book-server 
    # You can optionally use your favorite Python virtual environment
    pip install -r requirements.txt
    export FLASK_APP=guest-book-server.py
    flask run
```
    

  2. Serve the client:

```
    cd guest-book-client 
    npm install
    npm run serve
```


  3. Open the page http://localhost:8090/ in your favorite browser


#### Notes:

 - if you use a different client port you need to update CORS settings in the `guest-book-server.py`

