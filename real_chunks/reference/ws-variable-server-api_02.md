### WS-API: VariableServer > Example Variable Server Client

body>
      <style>
          table { border-collapse: collapse; width: 100%; }
          th, td { text-align: left; padding: 8px; }
          tr:nth-child(even){background-color: #f2f2f2}
          th { background-color: #562399; color: white; }
      </style>
      <header>
      </header>

      <div class="variableDisplay"></div>
      <table class="variables">
          <tr>
              <th>Variable</th>
              <th>Value</th>
          </tr>
      </table>

      <div id="output"></div>
      <script type="text/javascript">
          function log(s) {
              var p = document.createElement("p");
              p.style.wordWrap = "break-word";
              p.textContent = s;
              output.appendChild(p);
          }
          function sendMessage(msg) {
              ws.send(msg);
          }
          // Interface to Trick WebSocket Variable Server
          function setPeriod(period) {
              sendMessage(`{"cmd":"var_cycle","period":${period}}`);
          }
          function addVarTableRow(name, value) {
              // create a row in the table that contains two <td>s, one for the var_name and one for its value.
              let tr = document.createElement('tr');
              let td1 = document.createElement('td');
              td1.textContent = `${name}`;
              let td2 = document.createElement('td');
              td2.textContent = `${value}`;
              td2.className = "values";
              tr.appendChild(td1);
              tr.appendChild(td2);
              varTable.appendChild(tr);
          }
          function addVariable(name, value) {
              sendMessage(`{"
