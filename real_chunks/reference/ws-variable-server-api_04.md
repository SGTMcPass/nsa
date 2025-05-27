### WS-API: VariableServer > Example Variable Server Client

 = varTable.getElementsByClassName("values");
                 valueNodes[0].textContent = msg.time;
                 for (let i = 0; i < msg.values.length; i++ ) {
                     valueNodes[i+1].textContent = msg.values[i];
                 }
             }
          };
          ws.onerror = function(e) {
             console.log("WebSocket Error: " , e);
             handleErrors(e);
          };
          ws.onclose = function(e) {
             console.log("Connection closed", e);
          };

      </script>
  </body>
</html>
```

Continue to [Extending the HTTP API](Extend-http-api)
