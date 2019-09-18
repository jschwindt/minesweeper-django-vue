# minesweeper-django-vue

Demo: https://ancient-tundra-27161.herokuapp.com/

# Design

- Django + django-rest-framework (DRF) + VueJS application.
- Player (user) CRUD using built in Django features.
- Game logic built on the frontend using VueJS.
- DRF for games persistence.
- API auth based on session cookie.

# TODO

- Missing features due to time restriction: 
    1. <s>Ability to reload old paused game</s> Done!
    2. Old games pagination and deletion
    3. API documentation
    4. Tests
- Create two independent applications:
    1. Frontend as a single-page application using VueJS
    2. Backend as an API only application based on DRF.
- Move player CRUD and Auth to the frontend.
- Use JWT as authorization
