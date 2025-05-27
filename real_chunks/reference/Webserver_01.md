### Adding a Web Server to Your Sim > The Default Document Root Directory

 active, you must at least specify the following :

```python
web.server.enable = True

```

To have your web server listen on port `8890`, rather than `8888`, you would specify:

```python
web.server.port = 8890
```

To serve files from a directory called ```my_document_root```, rather than ```www```:

```python
web.server.document_root = "my_document_root"
```

To see client/server communication:

```python
web.server.debug = True
```

## When the Web Server Starts
The web server, if enabled, will start during sim initialization. When it does, it will look for the specified document root directory. By default that’s `“www”`. If root directory doesn’t exist, one will be created with a simple `index.html` file , a style sheet, and a couple of directories.


## Connecting to Your Web Server
Assuming that you accepted the default port, connect to ```http://localhost:8888/``` (```https://localhost:8888/``` if `ssl_enable=True`) from your web browser. This will display the `index.html` file in your root directory.


## The Default Document Root Directory

The default document root directory that was initially created for you is minimal.

```
www/
    index.html
    style.css
    apps/
    images/
```

**index.html** is the file that’s displayed when you connect to `http://localhost:8888/`.

**style.css** is a CSS style-sheet that’s included by index.html to give it some pizzazz.

The **apps** directory contains links to some example html/javascript applications
 in ```$
