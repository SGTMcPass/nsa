### WS-API: VariableServer > Example Variable Server Client

('td');
              td2.textContent = `${value}`;
              td2.className = "values";
              tr.appendChild(td1);
              tr.appendChild(td2);
              varTable.appendChild(tr);
          }
          function addVariable(name, value) {
              sendMessage(`{"cmd":"var_add","var_name": "${name}"}`);
              addVarTableRow(name, value);
          }
          var varTable = document.querySelector('table.variables');


          var ws = new WebSocket('ws://localhost:8888/api/ws/VariableServer');
          ws.onopen = function(e) {
              setPeriod(100);
              addVarTableRow("Time", 0.0);
              addVariable("dyn.cannon.pos[0]", 0.0);
              addVariable("dyn.cannon.pos[1]", 0.0);
              addVariable("dyn.cannon.vel[0]", 0.0);
              addVariable("dyn.cannon.vel[1]", 0.0);
              addVariable("dyn.cannon.time", 0.0);
              addVariable("dyn.cannon.timeRate", 0.0);
              addVariable("dyn.cannon.impact", 0.0);
              addVariable("I.dont.exist", 0.0);
              sendMessage("{\"cmd\":\"var_unpause\"}");
          };
          ws.onmessage = function(e) {
             let msg = JSON.parse(e.data);
             if (msg.msg_type == "values") {
                 let valueNodes = varTable.getElementsByClassName("values");
                 valueNodes[0].textContent = msg.time;
                 for (let i = 0; i < msg.values.length; i++ ) {
                     valueNodes[i+1].textContent = msg.values[i];
                 }
