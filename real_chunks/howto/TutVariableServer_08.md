### Trick Variable Server > Appendix > The Variable Server API

\") \n" )
client_socket.send( b"trick.var_unpause()\n" )

# ----------------------------------------------------------------------
# 8.0 Repeatedly read and process the responses from the variable server.
while(True):
    # 8.1 Read the response line from the variable server.
    line = insock.readline()
    if line == '':
        break

    # 8.2 Split the line into an array of value fields.
    field = line.split("\t")

    # 8.3 Get the position of the ball and update it on the canvas.
    x,y = float(field[1]), float(field[2])
    cx,cy = (x*SCALE+MARGIN), (HEIGHT-y*SCALE-MARGIN)
    canvas.coords(cannonBall,cx-ballRadius,cy-ballRadius,cx+ballRadius,cy+ballRadius)

    # 8.4 Get and display current Sim Mode.
    simMode = int(field[3])
    if simMode == MODE_FREEZE:
        canvas.itemconfigure(modeText, fill="blue", text="FREEZE")
    elif simMode == MODE_RUN:
        canvas.itemconfigure(modeText, fill="red", text="RUN")
    else:
        canvas.itemconfigure(modeText, text="--unknown-mode--")

    # 8.5 When impact occurs display the impact info, and command the sim from RUN mode to FREEZE mode.
    impact = int(field[4])
    if simMode == MODE_RUN:
        if impact:
            # 8.5.1 Display the impact info on the canvas.
            canvas.itemconfigure(impactTimeText, text="Impact time = " + field[5])
            canvas.itemconfigure(impactPosText, text="Impact pos  = (" + field[1] + "," + field[2] + ")")
            # 8.5.2 Command the sim to FREEZE mode.
            client_socket.send( b"trick.exec_freeze()\n")

    # 8.6 When the "Fire" button is pressed, command the sim from FREEZE mode to RUN mode.
    if simMode == MODE_FREEZE:
        if fireCommand:
            fireCommand = False
            fireButton.config(state=DISABLED)
            # 8.6.1 Command the sim to assign the slider values to init_speed, and init_angle.
            client_socket.send( b"dyn.cannon.init_speed = " + bytes(str(speedScale.get()), 'UTF-8') + b" \n")
            client_socket.send( b"dyn.cannon.init_angle = " + bytes(str(angleScale.get()*(math.pi/180.0)), 'UTF-8') + b" \n")
            # 8.6.2 Command the sim to re-run the cannon_init job.
            client_socket.send( b"trick.cannon_init( dyn.cannon )\n")
            # 8
