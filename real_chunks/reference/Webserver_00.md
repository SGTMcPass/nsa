### Adding a Web Server to Your Sim > The Default Document Root Directory

| [Home](/trick) → [Documentation Home](../Documentation-Home) → Web Server |
|------------------------------------------------------------------|

# Adding a Web Server to Your Sim

If Trick is [configured with Civetweb](Configure-Civetweb.md),
adding a web server to your simulation simply requires including the CivetServer sim module into your **S_define** file:

```
#include "sim_objects/CivetServer.sm"
```

## Configuration of the Web Server

The following (`input.py`) parameters are available to configure your web server:

|Parameter Name             | Default Value             | Description                                                       |
|---------------------------|---------------------------|-------------------------------------------------------------------|
|web.server.enable          | `False`                   |Must be explicitly enabled                                         |
|web.server.port            | `8888`                    |Web servers “listen” port                                          |
|web.server.document_root   | `"www"`                   |Web servers document root                                          |
|web.server.debug           | `False`                   |Print Client/Server Communication.                                 |
|web.server.ssl_enable      | `False`                   |Encrypt traffic. Uses https instead of http.                       |
|web.server.path_to_ssl_cert|`"~/.ssl/server.pem"`      |Path to your certificate.  This is only used if `ssl_enable = True`|
|web.server.error_log_file  |`"civet_server_error.log"` |CivetWeb error log file.                                           |

For your web server to be active, you must at least specify the following :

```python
web.server.enable = True

```

To have your web server listen on port `8890`, rather than `8888`, you would specify:

```python
web.server.port =
