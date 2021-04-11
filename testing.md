# Testing

## Validation Services
### Validation Services used
* [W3C Markup Validation Service](https://validator.w3.org/) - To validate html code
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - To validatate CSS code
* [JS Hint](https://jshint.com/) - To validate JavaScript code
* [PEP8 Online](http://pep8online.com/) - To validate python code

### Errors / Warnings found by W3C Markup Validation Service:
All rendered pages were ran through the W3C Markup validation Service
## Errors:
- Register and Login pages: 
    - 'Error: Attribute actions not allowed on element form at this point.'
        - This was resolved by correcting the typo 'actions' to 'action'
- Add Review page: 
    - 'Error: Attribute type not allowed on element select at this point.'
        - Resolved by removing 'type' attribute from the select input.
    - 'Error: The value of the for attribute of the label element must be the ID of a non-hidden form control.'
        - Changed label for="bookCover" to for="book_cover"
    - 'Error: The aria-describedby attribute must point to an element in the same document.'
- Edit Review page:
    - 'Error: Attribute type not allowed on element select at this point.'
        - Removed type="text" from select input.
    - 'Error: The first child option element of a select element with a required attribute, and without a multiple attribute, and without a size attribute whose value is greater than 1, must have either an empty value attribute, or must have no text content. Consider either adding a placeholder option label, or adding a size attribute with a value equal to the number of option elements.'
        - Fixed by adding a first option with value="" to the select rating element
    - 'Error: The value of the for attribute of the label element must be the ID of a non-hidden form control.'
        - Changed for="author" to for="author_name" to match input ID.


### Errors / Warnings found by W3C CSS Validation Service:
- No errors / warnings found

## Errors / Warnings found by JS Hint:
script.js file was ran through JS hint with the following comments:
/*globals $:false */ - As I used jQuery
/*jshint esversion: 6 */ - As I used Javascript ES6
### Warnings
- Two 'missing semicolons'
    - Added semicolons to relevant lines
- One undefined variable 'mybutton'
    -  Declared variable using 'let' 
-One unused variable 'topFunction'
    - Ignored as variable is being called outside the JS file

## Errors / Warnings found by PEP8 online:
- 'continuation line with same indent as next logical line'
    - Changed indentation of login function

## Testing User Stories 
1. As a user, I want to browse through book reviews and find more information on each book.
    - The first page that the user is greeted with when visiting the site is the "review.html" page.
    - From here they can easily see all reviews that they/other users have uploaded to the site.
2. As a user, I want to be able to upload my own book reviews to the site.
    - Once logged in the user has the option to 'Add review' from the navigation bar.
    - On this page the user will fill out a form with different fields about the book they are reviewing.
    - On submitting the form, the users review will be added to the main page "reviews.html", and the user will be redirected to this page.
3. As a user, I want to be able to register and create an account on the site.
    - On a users first visit, the navigation bar will show the option to 'Register'.
    - When selected, the user is brought to a form where they need to input a username and password.
    - Once submitted, provided all criteria is met for the username and password, the users account is created and they are brought to their profile page.
    - When registered, the user will see new options in the navigation bar - Profile, Add Review, Logout.
4. As a user, I want to be able to login to the site and view my profile.
    - When a user visits the site, they will see the option to 'login' from the navigation bar.
    - This will lead them to a login page where they need to input their previously created username and password.
    - Once logged in, they will be brought to their Profile, and the navigation bar will have new options - Profile, Add Review, Logout
    - The users profile will contain all reviews uploaded by them, along with the option to Edit/Delete each one.
5. As a user, I want to be able to edit / delete the reviews I have uploaded. 
    - When a logged in user is on the main Reviews page, any reviews uploaded by them will have Edit/Delete options.
    - They will also have these options from their Profile page.
    - The Edit option will take the users to a form, which will be prepopulated with the review information.
    - The user can change any input and the submit the changes, which will update the original review.
    - The Delete option will delete the review from the database.

## Manual testing of all elements and functionality 

### Register Page
- Accesible by selecting 'Register link' from navbar - Which is visible when user is not logged in.
- Try to register an already existing username
    - User receives flash message 'Username already exists.
- Test username validation by inputting no username/ username less than 5 characters / username more than 15 characters
    - User receives relevant promts / flash message that user name already exists / is too short / is required. User cannot type username longer than 15 characters.
- Test password validation by inputting no password/ password less than 5 characters / password more than 15 characters.
    - User receives relevant promts that password is too short / is required. User cannot type password longer than 15 characters.
- Test submit button
    - Upon submitting valid registration details, user is brought to their profile page and is shown a 'Registration Successfull!' flash message. The user is now logged into their account. 

### Logout functionality
- Test logout button - Only visible to a logged in user
    - On selecting the logout button from the navbar, the user is redirected to the login page and shown a flash message 'You have been logged out!'. Navigation bar changes so that user doesn't have options that only logged in users should have (Add Review, Profile, Log out)
    
### Login Page
- Login page accessible through navbar (to not logged in user)
- Test submitting username that doesn't exist
    - User receives flash message 'Incorrect username / password'
- Test submitting incorrect password
    - User receives flash message 'Incorrect username / password'
-Test submitting valid username and password
    - User is logged in, brought to their profile and shown a flash message - 'Welcome, {{username}}'

### Add Review page
- Accessible from navbar when user is logged in
- Test 'Book Title' field
    - User cannot submit empty input, receives prompt - 'Please fill in this field'
    - User cannot submit value less than 3 characters, receives prompt - 'Please lengthen this text to 3 characters or mroe, you are currently using (2) characters'
    - User can not input more than 100 characters
- Test 'Authors Name' field
    - User cannot submit empty input, receives prompt - 'Please fill in this field'
    - User cannot submit value less than 5 characters, receives prompt - 'Please lengthen this text to 5 characters or mroe, you are currently using (4) characters'
    - User can not input more than 30 characters
    **Updated max length from 20 to 30 to allow for longer author names**
- Test 'Category' dropdown
    - User cannot leave dropdown as default 'Select category' - Prompted to 'Please select an item in the list'
    - Dropdown reveals all available book categories and allows user to select one
- Test 'URL of book cover image
    - Although input doesn't allow empty input, user can input text that is not a URL
    **To fix this issue, I added pattern attribute to the form input with a regex pattern for URL**
- Test 'Rate this book' dropdown
    - User cannot leave dropdown as default 'Rate this book' - Prompted to 'Please select an item in the list'
    - Dropdown reveals all star ratings from 1-5 and allows user to select one
- Upon submitting a valid form, the user is redirected to the main 'Reviews' page, where their review is added. They also receive a flash message - 'Review Added!'

### Edit Review functionality
- Test 'Edit Review' button on homepage, and Profile page
    - Edit review button is only available to user if they submitted the review themselves
    - Edit review button on both homepage and profile page lead the user to the Edit Review form.
- Test that when user is redirected to 'Edit Review' page, that the form is prepopulated with that specfic reviews information
    - All inputs show the correct information for the original review
- Test that when each input on the Edit Review form is updated, the review is updated in the database and on the front end
    - Review updates on both the homepage and the users profile page
- Upon submitting the Edit Review form, user receives a flash message 'Review edited!'. User stays on Edit Review page
### Delete Review functionality
- Test Delete Review button from users profile page
    - Button appears on all review on users profile page sa they were all created by the user
    - When Delete Review button is selected the review is deleted from the profile page, the review page and the database
    - When the button is selected from the Profile page, the user receives a flash message 'Review Deleted', and is redirected to the homepage
- Test Delete Review button from homepage
    - When user is not logged in, no reviews show the option to Delete Review
    - When user is logged in, only reviews that they created show the Delete Review button
    - When Delete Review button is selected the review is deleted from the  homepage, the profile page and the database
    - When Delete Review button is selected from the homepage, the user receives a flash message 'Review Deleted', and the homepage is refreshed 

### Search
- Test searching by book title
    - Search for name of book that review exists for & select 'Search' button - That review is shown to user
    - Search one word of full book title eg 'The' and and books with 'The' in the title is shown to user
- Test searching by author name
    - Search for author name that review exists for - That review is returned to user
    - Search for author name who has more than one book review - All reviews with that author name are returned to user
**User has to scroll down each time to view search results**

## Console and terminal errors
- No console errors
- Terminal shows 'Doctype must be declared first'
    - Ignored as doctype is declared in base.html
- Terminal also shows 'env imported but unused'
    - Ignored as env.py is not being pushed (in gitignore file)


## Accessability Testing
[WAVE Web Accessability Evaluation Tool](https://wave.webaim.org/) was used to test the accessability of my site.
The following recommendations and changes were made:
1. 1x missing form label - Search bar on homepage
    - Added label to search form on homepage
2. 1x long alternative text
    - Igonored as this will depend on the length of the book title the user has input.
3. 1x skipped level hearding
    - Changed h5 in book review cards to h2.
    