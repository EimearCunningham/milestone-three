# On My Bookshelf
![Site shown on different devices](assets/images/readme-images/INSERT IMAGE HERE)

Live website: INSERT LIVE SITE LINK HERE

A website for users to upload book reviews, and browse other peoples book reviews.
 
# UX
 
### Who this website is for:
* This website is for people interested in reading.

### What they want to achieve:
* They want to browse through book reviews, add their own book reviews.

### This project is the best way to help them achieve these things because:
* From the homepage, the user can easily browse through book reviews without having to register / login.
* Once logged in the user has the opportunity to easily upoad their own book reviews.

## User Stories:
1. As a user, I want to browse through book reviews and find more information on each book.
2. As a user, I want to be able to upload my own book reviews to the site.
3. As a user, I want to be able to register and create an account on the site.
4. As a user, I want to be able to login to the site and view my profile.
5. As a user, I want to be able to edit / delete the reviews I have uploaded. 

## Design 
- Color Scheme 

- Typography 
    

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

### Register Page
- The register page will also display the navigation bar at the top of the page.
- Users will be able to login to their account by submitting a form with their username and password, and selecting a "Login" button.

### Add Review Page
- Again, the navigation bar will be visible at the top of this page.
- Only logged in users will be able to access the "Add Review" section.
- Users will be able to complete a form and submit a book review.

### User Profile Page
- Logged in users will be able to navigate to their own unique profile.
- Their profile will display all of they book reviews they uploaded.
- From here, users will be able to Edit and Delete reviews that they uploaded.

### Features Left to Implement


# Technologies Used
## Languages, frameworks and libraries used
- Flask app created.

## Other technologies used
- MongoDB was used to create a database and store data in JSON-like documents. A database called "bookshelf" was created with three
collections - users, reviews, categories.
- Deployed to Heroku.
- Werkzeug

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