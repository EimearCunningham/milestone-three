# On My Bookshelf
![Site shown on different devices](assets/images/readme-images/INSERT IMAGE HERE)

Live website: INSERT LIVE SITE LINK HERE

A website for users to upload book reviews, and browse other peoples book reviews.
 
# UX
 
### Who this website is for:
* This website is for people interested in reading who want to share book reviews with others & upload their own book reviews.

### What they want to achieve:
* They want to browse through book reviews & add their own book reviews.

### This project is the best way to help them achieve these things because:
* From the homepage, the user can easily browse through book reviews without having to register / login.
* Once logged in the user has the opportunity to easily upoad their own book reviews by filling out a short form.

## User Stories:
1. As a user, I want to browse through book reviews and find more information on each book.
2. As a user, I want to search for a book/author in the reviews.
3. As a user, I want to be able to register and create an account on the site.
4. As a user, I want to be able to upload my own book reviews to the site.
5. As a user, I want to be able to login to the site and view my profile.
6. As a user, I want to be able to edit / delete the reviews I have uploaded. 

## Design 
### Color Scheme 
I decided to keep the color scheme of the site neutral and clean
- A light grey/lilac (#d1d1e0) was used as the background color for the site 
- A soft peach (#e8e4e3) was used as the background color for the review cards, to compliment the page background
### Typography 
- Google Font [Kiwi Maru](https://fonts.google.com/specimen/Kiwi+Maru)"Kiwi Maru" was used as the font type across the site. I thought this everyday text complimented the casual and clean style of the site.

## Wireframes:
[desktop]
[tablet]
[mobile]

# Features
### Navigation bar
- The navigation bar at the top of each page allows the user to easily get to each section of the site.
- Depending on whether the user is logged in/not, the navigation bar will display different options:
    * If user is not logged in the navigation bar will display the options: Home, Register, Login.
    * If the user is logged in the navigation bar will display the options: Home, Add Review, Profile, Logout.
- The logo in the top left corner will bring the user to the homepage, as expected.

### Homepage
- The homepage will display the navigation bar at the top of the page.
- A large hero image will be displayed underneath the navigation bar.
- All uploaded book reviews will be displayed on the homepage.
- If a user is logged in, the book reviews they have uploaded themselves will have the options "Edit" and "Delete".

### Login Page
- The login page will display the naviagation bar at the top of the page.
- The page will contain a form with two inputs - "Username" and "Password", and a "Register" button.
- When ths user selects the "Register" button and succesfully createas a profile, they will be redirected to their own Profile.

### Registration Page
- The register page will also display the navigation bar at the top of the page.
- Users will be able to login to their account by submitting a form with their username and password, and selecting a "Login" button.

### Add Review Page
- Again, the navigation bar will be visible at the top of this page.
- Only logged in users will be able to access the "Add Review" section.
- Users will be able to complete a form and submit a book review.

### Edit Review Page
- Users will be able to edit any reviews they created themselves.
- The option will be available on the review displayed on the homepage and on the users profile page.
- When the 'Edit Review' button is selected, the user will be brought to a form that is prepopulated with the reviews information.
- The user will have the option to edit each field of the information and then submit the form to edit the review.

### Delete Review functionality
- Users will be able to delete any review that they uploaded, should they not want it shown on the site anymore.
- They will have the option to 'Delete Review' from their profile page or the site homepage.
- When selected, the review will be deleted.

### User Profile Page
- Logged in users will be able to navigate to their own unique profile.
- Their profile will display all of they book reviews they uploaded.
- From here, users will be able to Edit and Delete reviews that they uploaded.

### Logout functionality
- When logged in, users will have the option to 'Logout' displayed on the navbar.
- When selected the user will be logged out from their account.

### Features Left to Implement

# Technologies Used
## Languages, frameworks and libraries used
* HTML5, CSS3, Javascript and Python were the programming languages used for this project.
* [Github](https://github.com/)
* [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) - Bootstrap version 4 was used for layout and responsiveness purposes..
* [jQuery](https://jquery.com/)- jQuery was used to create the 'Scroll to top' button.
* [Font Awesome](https://fontawesome.com/) - 
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Flask framework used to create app. 
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Templating language used with Flask
* [Mongo DB Atlas](https://www.mongodb.com/) - Used to create non relational database

## Other technologies used
* [Unsplash.com](https://unsplash.com/Unsplash.com) - Provided hero image for homepage
* [Am I Responsive](http://ami.responsivedesign.is/) - Used to create responsive.JPG for README.
* [Balsamiq](https://balsamiq.com/wireframes/) - Desktop app used to create wireframes.
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - Used to hash users passwords.

# Testing
This can be found in [testing.md](testing.md)


# Deployment
## Project was deployed to Heroku 

4 things we need to push to Heroku
1.	Create Heroku app
2.	Link git repository to Heroku
3.	Create requirements.txt file
4.	Create a Procfile

1.	Create app on Heroku 
Sign in and select ‘Create new app’

2. Select GitHub icon and insert repository name
Search for repository and 'Connect' once found
Go to 'Settings' tab of Heroku app
Go to 'Reveal config vars'
Add the following keys and values: INSERT SCREENGRAB OF CONFIG VARS

3 & 4. Push requirements.txt and Procfile to GitHub
Go to Heroku and 'Enable automatic deployment' & 'Deploy branch'
'Your app was succesfully deployed' - https://on-my-bookshelf-ms3.herokuapp.com/


# Credits
Favicon https://iconarchive.com/tag/favicon-book
REGEX https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url 
Scroll to top https://www.w3schools.com/howto/howto_js_scroll_to_top.asp 
## Code

## Content

## Media

## Acknowledgements


**This site is for educational purposes only** 

BUGS:
Validation on select category dropdown - Add value="" to <option selected disabled value="">Select Category</option>