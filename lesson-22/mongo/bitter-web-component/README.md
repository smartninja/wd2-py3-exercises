### Commands for Heroku deployment (for existing Heroku app)

1. Heroku login: `heroku login`
2. Make sure the Git repo is initialized (`git init`) and the files commited (`git add .` and `git commit -m "message"`)
3. Add Heroku remote URL: `heroku git:remote -a enter-heroku-app-name-here`
4. Push to Heroku: `git push heroku master` (if it doesn work, try to force it: `git push heroku master --force`)

### Build JS using Webpack

First install npm if you haven't got it yet.

Then install webpack:

    npm install webpack
    npm install webpack-cli

And finally run this command to build the final.js file:

    npx webpack src/main.js --output static/js/final.js

