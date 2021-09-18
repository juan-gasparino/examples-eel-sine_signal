# Template desktop app with Python and JS

Template that allow you to create Desktop App with Frontend technology and Python in backend.

This project use eel.js library from: https://github.com/samuelhwilliams/Eel

eel.js make easy to compile your project in 1 exe (HTML,JS,CSS) and Python all together

All the project has been created in Win10 enviroment.

## 1 - Run project

To run the project go to: Backend open cmd and type: python sineSignal.py

This will open the project and will run up a local server in port 8080.

## 2 - Update frontend part

In order to update the frontend part you have to stop the application.

Go to frontend folder and run: "npm start" to run up a server in port 8080 using webpack-dev-server.

You have to keep in mind that this will only run up the frontend part the backend will remain off so many backend

parts wont run. Modify the frontend part that you want html,css or js and save.

Now go back to the cmd console and run "npm run build" this will compile all the frontend files and will save it in

dist folder.

Now you have to recompile the backend part in order to update the whole app. Go to the backend folder and run: "python sineSignal.py"
