# Grain_Haven

## Milestone Project 3

This repository contains the code for an online homebrewing recipe application. It is primarily built using Python and the Flask framework.

## UX

This application was built with a mobile first, responsive design in mind.

### User Stories

- As a new User I should:

  - See a simple cover image with a tag line.
  - See an easy to use navigation bar to allow instant access to the recipes.
  - Have the ability to start creating a recipe from the home page.

- As a user creating a recipe I should:

  - Have the ability to choose my name, brew size, fermentables, hops, mash schedule and yeast.
  - Be able to choose the style of beer from a menu.
  - Be able to easily save the recipe in the forum with a button click.
  - Be able to cancel the recipe and return to the recipes page.

- As a user viewing the recipes:

  - I should be able to see a thumbnail picture which gives me an idea of the beer.
  - I should be able to see some comments to gain an idea of the background of the recipe.
  - I should be able to sort the recipes by beer style for fast naviagtion to a specific style of my choosing.

- As a user editing my recipes:

  - I should be able to easily access and edit the recipes I created.
  - I should have full control when it comes to editing the recipes I created and change any aspect of said recipe.
  - I should be able to delete any user created recipes as I see fit.

## Testing and validation.

### Testing

- The site was tested on all modern desktop and mobile browsers to ensure cross compatibility and functionality.
- The site was tested to be responsive and to ensure it would be correctly displayed across mobile devices.
- I ensured that each one of the user stories were thoroughly tested to be functional without errors.
- Testing for this project was implemented manually. The majority of testing covered the various Flask routes. Some examples of issues/tests on routes:

  - I manually tested the add/edit routes a number of times to get the correct functionality, origionally the routes were not adding my data to the mongo database and this required a number of test variants to get the functionality.
  - The pagination functionality required a lot of testing to get it implemented. Originally I managed to get the pagination to show but no matter what page I was on it showed every recipe. This took a number of tests to work out the sytax needed to get it functioning correctly.

- I tested my app speed using [this](https://developers.google.com/speed/pagespeed/insights/?url=https%3A%2F%2Fgrain-haven.herokuapp.com%2F) Google speed testing utility.

### Validation

All Python code was linted and formatted to the [Pep8](https://www.python.org/dev/peps/pep-0008/) standard.

All Html and CSS was run through validators to ensure correct syntax, styling and appropiate use of tags.

## Features overview

- Add a recipe.
- Edit recipes.
- Filter recipes by style.
- Delete User created recipes

### Features I'd like to implement in future versions

- Log in system and unique users
- Sharable recipes.
- Export to printable version.
- Implement search caching/indexing.
- Rating system

## Challenges

- Learning how to integrate Flask and MongoDB was a challange, with only a week and a half to create the project I had to spend a considerable amount of time learning how to create certain routes. I learned much from how to manage and interact with a NoSQL data store.

- I learned a considerable amount about the jinja templating language through reading documentation as I struggled initially with some of the syntax.

## Technologies Used

- [HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript)
- [jQuery](https://jquery.com/)
- [Bootstrap](https://getbpptstrap.com)
- [Flask](http://flask.pocoo.org/)
- [MongoDB](https://www.mongodb.com/)
- [Heroku](https://www.heroku.com/)

## Deployment

- A live version of this app is available [here](https://grain-haven.herokuapp.com/).
- - The Flask application is deployed to a Heroku instance.

The process I took to deploy this project entails: - Creating a new heroku environment - Creating a requirements.txt file so heroku can install the necessary add ons such as Flask to run the app - Creating a Procfile to show Heroku this is a web application. - Pushing my project to Github - Setting my IP, PORT and MONGODB URI variables within my heroku gui - Linking my Github to Heroku and deploying through heroku - Setting up automatic deployments in Heroku to always grab the newest release from my github.

## MongoDb Schema

- The main MongoDB collection `recipes` takes the following schema.

```json
{
  "_id": {
    "$oid": "5d3ed8901c9d4400000cf3f6"
  },
  "recipe_name": "Guiness Clone",
  "recipe_style": "Stout",
  "batch_size": "23L",
  "fermentables": "Pale ale 5.4kg, Vienna Malt 0.49kg, Munich I 0.27kg, Caramunich II 0.2,",
  "hops": "target 30g 60 minutes",
  "mash_steps": "Saccharification 67C 60 Minutes, Mash Out 75C 10 Minutes",
  "yeast": "Irish Ale Yeast",
  "comments": "Guinness is a dark Irish dry stout that originated in the brewery of A...",
  "image": "image link",
  "can_delete": "False"
}
```

## Credits

### Third-party

- I found the code required for the landing page video [here](https://codepen.io/JacobLett/pen/LmWvLZ)
- I found the code to help me set up the Flask Pagination [here](https://flask-paginate.readthedocs.io/en/latest/)
- I sourced the landing video from [here](https://coverr.co/)
