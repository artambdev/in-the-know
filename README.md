# Facts From the Past
- developed by Arthur Ambalov

![Image of website on different sized screens](docs/am-i-responsive.png)

[Link to live webpage](https://github.com/artambdev/facts-from-the-past/)

## Table of Contents

1. [Overview](#overview)
2. [User Stories](#user-stories)
3. [Design](#design)
    1. [Colour](#colour)
    2. [Font](#font)
4. [Features](#features)
    1. [Pages](#pages)
5. [Validation](#validation)
    1. [HTML](#html)
    2. [CSS](#css)
    3. [Javascript](#javascript)
    4. [Accessibility](#accessibility)
    5. [Performance](#performance)
    6. [Browser Compatibility](#browser-compatibility)
    7. [Device Compatibility](#device-compatibility)
    8. [Testing User Stories](#testing-user-stories)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)

## Overview

In The Know is a social discussion board where users can start conversations and reply to each other in branching chains of posts.

## User Stories
The website is designed for 8 detailed user stories, which are detailed alongside their acceptance criteria:

1. As a user I can view a paginated list of posts so that I can select a post to view or comment on.
Acceptance criteria:
- A list of posts is displayed on the site's main page
- With their title and content displayed
- In the case of many posts, they are moved onto new pages with a previous/next page option

2. As a user I can create a post so that I can start discussions with others.
Acceptance criteria:
- Given a user is registered
- On the main page, a "new post" button is presented
- Clicking the button brings them to a new page to make a post

3. As a user I can register an account so that I can join in on discussions.
Acceptance criteria:
- Given an email address, a user can register an account
- Then they can use their details to log in
- When logged in, they can create posts and reply to posts

4. As a user I can edit and delete posts so that I can engage in the conversation.
Acceptance criteria:
- Given a user has posted
- An "edit" button appears on their posts, allowing them to change them
- A "delete" button appears on their posts, deleting it and its replies

5. As a site admin I can hide or delete users' posts so that I can prevent hostile discussions.
Acceptance criteria:
- Given an admin is logged in
- A "hide" option is presented on users' posts to make them unreadable
- The delete option appears on other users' posts

6. As a user I can view a post in more detail so that I can see its full text and replies.
Acceptance criteria:
- When a post is clicked on
- A new page is entered with a detailed view
- The post it replies to and its own replies are visible

7. As a user I can reply to other users' posts so that I can be involved in a conversation.
Acceptance criteria:
- Given a user is logged in
- A "reply" option is available on a post's detailed view
- Which allows them to create a reply to the post

8. As a site user I can submit a feedback form so that I can convey feedback to the site admins.
Acceptance criteria:
- A user can navigate to the "contact us" page
- They can fill out a form with their details and a message
- Which is then submitted to the database for the admins to review

## Design
A few wireframes were made in advance of starting development to plan out the most important features and the structure of code that would be required to accompany them.

The wireframes are presented below:

<details><summary>Main page's desktop wireframe</summary>
<img src="docs/wireframes/wireframe-home.png">
</details>

<details><summary>Main page's mobile wireframe</summary>
<img src="docs/wireframes/wireframe-home-mobile.png">
</details>

<details><summary>Create Post page's wireframe</summary>
<img src="docs/wireframes/wireframe-create.png">
</details>

<details><summary>Detailed post view's wireframe</summary>
<img src="docs/wireframes/wireframe-detailed.png">
</details>

<details><summary>Contact page's wireframe</summary>
<img src="docs/wireframes/wireframe-contact.png">
</details>

### Colour
Using <a href="https://mycolor.space">ColorSpace</a> a colour scheme ranging from off-white to peach to brown was used to give the website a friendly and cozy scheme suitable for a social site.

### Font
The Lato was chosen as a simple and easy-on-the-eyes sans-serif font. If it cannot be loaded, the browser's default sans-serif font is loaded in its place.

### Database
- The website's backend database is powered by the Django framework, with the PostgresSQL relational database system provided by Code Institute.

The following models are used:

#### Post

The Post model is used to store individual posts. Posts can start a new chain or be a reply to another post.

The post model contains:
- The post author, a built-in Django User model
- A slug ID generated randomly for each post
- Optionally, a post that is being replied to
- The text content of the psot (capped to 200 characters)
- The time the post was created on
- The time it was last updated on
- Whether an admin has hidden the post or not

#### Feedback

The feedback model is used to store feedback anonymously provided to the admins. It provides the following data:
- A name
- An email address
- A message
- Whether an admin has approved it as "resolved" or not
- The time the feedback was sent on

## Features
The website has 5 main pages and X features across them.

### Pages
The 5 pages are:

- The homepage, where the user is presented with a list of all the website's posts stacked side-by-side and paginated every 8 posts. On mobile posts are shown in a one-post-wide list.
- The detailed post view, where users can see a post in detail, the post it's replying to, all of its replies, and can create a reply
- The post creation page where users can write a new post to start a new discussion
- The post editing page where users can rewrite one of their existing posts to make changes
- The Contact page where users can privately submit feedback to the admins

### Navbar
- A navigation bar at the top of the screen
- Allows the user to access all the main pages of the website
- Shows the user's logged-in status
- Sign-in/sign-up/sign-out appear according to logged-in status

<details><summary>Image</summary>
<img src="docs/features/feature-nav.png">
</details>

### Create Post Button
- A large prompt on the main page
- Clicking brings the user to the "create a post" page

<details><summary>Image</summary>
<img src="docs/features/feature-create-post.png">
</details>

### Post List
- A list of all posts on the front page
- Posts are shown side-by-side on larger screens, one-by-one on mobile
- Posts can be clicked on to go to their detailed view page
- Admin users have admin functions visible on posts
- The post's creation date and replied-to post are also shown

<details><summary>Image</summary>
<img src="docs/features/feature-post-list.png">
</details>

### Pagination
- Posts are shown 8 at a time
- Pagination options show at the bottom of the list to go to the next or previous batch

<details><summary>Image</summary>
<img src="docs/features/feature-pagination.png">
</details>

### Detailed View
- Clicking on a post shows it in greater detail
- Users have options to edit or delete their own post from here

<details><summary>Image</summary>
<img src="docs/features/feature-detailed-view.png">
</details>

### Admin Functions
- Admins (superusers) have the option to delete or hide users' posts
- This allows them to moderate unsavory content

<details><summary>Image</summary>
<img src="docs/features/feature-admin.png">
</details>

### Replied-To Post
- In detailed view, the replied-to post is also shown
- It can be clicked to go to its detailed view

<details><summary>Image</summary>
<img src="docs/features/feature-replied-to.png">
</details>

### Reply Form
- While logged in, a form is presented to make a reply
- This creates a new post replying to the currently viewed one

<details><summary>Image</summary>
<img src="docs/features/feature-reply.png">
</details>

### Reply List
- A list of all the post's replies is shown underneath it
- Clicking on any post in the list will bring the user to its detailed view

<details><summary>Image</summary>
<img src="docs/features/feature-reply-list.png">
</details>

### Post Creation Form
- A form on the post creation page
- Allows the user to type text for a new post and submit it

<details><summary>Image</summary>
<img src="docs/features/feature-post-creation-form.png">
</details>

### Feedback Form
- A form on the contact page
- Requires the entry of a name, email address and message
- Posts the feedback model to the database for admin review

<details><summary>Image</summary>
<img src="docs/features/feature-feedback-form.png">
</details>

## Validation & Testing

### HTML
All pages on the site are validated with the W3C's Markup Validation Service and show no errors or warnings. See each page below:
<details><summary>Homepage</summary>
<img src="docs/validation/html/validation-html-home.png">
</details>
<details><summary>Detailed View</summary>
<img src="docs/validation/html/validation-html-detailed.png">
</details>
<details><summary>Contact Page</summary>
<img src="docs/validation/html/validation-html-contact.png">
</details>
<details><summary>Create Page</summary>
<img src="docs/validation/html/validation-html-create.png">
</details>
<details><summary>Edit Page</summary>
<img src="docs/validation/html/validation-html-edit.png">
</details>

### CSS
The CSS style used by the site was validated with the W3C's CSS Validation Service, and showed no errors. There is one warning for the external stylesheet of Google Fonts which cannot be checked. See below:
<details><summary>Images</summary>
<img src="docs/validation/css/validation-css-noerrors.png">
<img src="docs/validation/css/validation-css-warning.png">
</details>

### JavaScript
The JavaScript code used for the post deletion modal was validated with the JSHint Code Quality Tool, showing no errors or warnings.
<details><summary>Image</summary>
<img src="docs/validation/validation-js.png">
</details>

### Python
<a href="https://pep8ci.herokuapp.com/">PEP8 Python Linter</a> was used to validate all edited python files in the contact and list apps.

#### Contact App ####
<details><summary>admin.py</summary>
<img src="docs/validation/python/validation-python-contact-admin.png">
</details>
<details><summary>forms.py</summary>
<img src="docs/validation/python/validation-python-contact-forms.png">
</details>
<details><summary>models.py</summary>
<img src="docs/validation/python/validation-python-contact-models.png">
</details>
<details><summary>test_forms.py</summary>
<img src="docs/validation/python/validation-python-contact-testforms.png">
</details>
<details><summary>test_views.py</summary>
<img src="docs/validation/python/validation-python-contact-testviews.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/python/validation-python-contact-urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/python/validation-python-contact-views.png">
</details>

#### List App ####
<details><summary>admin.py</summary>
<img src="docs/validation/python/validation-python-list-admin.png">
</details>
<details><summary>forms.py</summary>
<img src="docs/validation/python/validation-python-list-forms.png">
</details>
<details><summary>models.py</summary>
<img src="docs/validation/python/validation-python-list-models.png">
</details>
<details><summary>test_forms.py</summary>
<img src="docs/validation/python/validation-python-list-testforms.png">
</details>
<details><summary>test_views.py</summary>
<img src="docs/validation/python/validation-python-list-testviews.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/python/validation-python-list-urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/python/validation-python-list-views.png">
</details>

### Accessibility
All pages on the site are checked with the WAVE Website Accessibility Evaluation Tool, and none show any errors. See each page below:
<details><summary>Homepage</summary>
<img src="docs/validation/wave/validation-wave-home.png">
</details>
<details><summary>Detailed View</summary>
<img src="docs/validation/wave/validation-wave-detailed.png">
</details>
<details><summary>Contact Page</summary>
<img src="docs/validation/wave/validation-wave-contact.png">
</details>
<details><summary>Create Page</summary>
<img src="docs/validation/wave/validation-wave-create.png">
</details>
<details><summary>Edit Page</summary>
<img src="docs/validation/wave/validation-wave-edit.png">
</details>

### Performance
Google Chrome's Lighthouse feature was used to check every page for performance issues, and each returned a high score in all categories. See each page's result below:
<details><summary>Homepage</summary>
<img src="docs/validation/lighthouse/validation-lighthouse-home.png">
</details>
<details><summary>Detailed View</summary>
<img src="docs/validation/lighthouse/validation-lighthouse-detailed.png">
</details>
<details><summary>Contact Page</summary>
<img src="docs/validation/lighthouse/validation-lighthouse-contact.png">
</details>
<details><summary>Create Page</summary>
<img src="docs/validation/lighthouse/validation-lighthouse-create.png">
</details>
<details><summary>Edit Page</summary>
<img src="docs/validation/lighthouse/validation-lighthouse-edit.png">
</details>

### Browser Compatibility
Each page has been tested to work on:
- Mozilla Firefox
- Google Chrome
- Microsoft Edge

### Device Compatibility
Each page was tested on Mozilla Firefox and Google Chrome's developer tools for responsive design. Testing was done on a desktop PC running Windows 11 and a Galaxy A50 phone.

### User Stories
Below is a list of user stories and the process by which they are fulfilled:

1. As a user I can view a paginated list of posts so that I can select a post to view or comment on.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Navbar | Navigate to the homepage via the navbar | Find a paginated list of posts | Works as expected |
| Pagination | On the homepage, scroll to the bottom of the page | Find an option to change pages | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/manual/testing-manual-story-1a.png">
<img src="docs/testing/manual/testing-manual-story-1b.png">
<img src="docs/testing/manual/testing-manual-story-1c.png">
</details>

2. As a user I can create a post so that I can start discussions with others.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Create Post button | Navigate to the homepage, click the Share Your Thoughts button | Go to the Create Post page | Works as expected |
| Create Post form | On the create post page, fill in a message and click post | Go back to the homepage with a new post visible | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/manual/testing-manual-story-2a.png">
<img src="docs/testing/manual/testing-manual-story-2b.png">
</details>

3. As a user I can register an account so that I can join in on discussions.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Navbar | Click the sign-up or sign-in option | Find a form to create an account or log into one | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/manual/testing-manual-story-3a.png">
<img src="docs/testing/manual/testing-manual-story-3b.png">
<img src="docs/testing/manual/testing-manual-story-3c.png">
</details>

4. As a user I can edit and delete posts so that I can engage in the conversation.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Edit button | On one of your posts, click "edit" | Be brought to a page to edit the post | Works as expected |
| Delete button | On one of your posts, click "delete" and confirm | Be brought to the main page with the post deleted | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/manual/testing-manual-story-4a.png">
<img src="docs/testing/manual/testing-manual-story-4b.png">
<img src="docs/testing/manual/testing-manual-story-4c.png">
<img src="docs/testing/manual/testing-manual-story-4d.png">
</details>

5. As a site admin I can hide or delete users' posts so that I can prevent hostile discussions.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Hide button | As a superuser, press "hide" on a user's post | Normal users can no longer see the post | Works as expected |
| Delete button | As a superuser, press "delete" on a user's post | The post is deleted | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/manual/testing-manual-story-5a.png">
<img src="docs/testing/manual/testing-manual-story-5b.png">
<img src="docs/testing/manual/testing-manual-story-5c.png">
<img src="docs/testing/manual/testing-manual-story-5d.png">
</details>

6. As a user I can view a post in more detail so that I can see its full text and replies.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Detailed post view | Click on a post anywhere on the site | Be brought to the post's detailed view with its replies | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/manual/testing-manual-story-6a.png">
<img src="docs/testing/manual/testing-manual-story-6b.png">
</details>

7. As a user I can reply to other users' posts so that I can be involved in a conversation.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Reply form | View any post as a logged in user | See a form to create a reply to the post | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/manual/testing-manual-story-7a.png">
<img src="docs/testing/manual/testing-manual-story-7b.png">
</details>

8. As a site user I can submit a feedback form so that I can convey feedback to the site admins.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Navbar | Click on the "contact us" button | Be brought to a page to submit feedback | Works as expected |
| Feedback form | Fill out the form and click submit | The feedback is entered into the database for admins to view | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/manual/testing-manual-story-8a.png">
<img src="docs/testing/manual/testing-manual-story-8b.png">
<img src="docs/testing/manual/testing-manual-story-8c.png">
</details>

### Automated Testing
Automated tests were created to test the forms and views of both of the apps (urls are tested in the process of testing views). See images of the successful tests in the terminal below:

#### Contact App ####
<details><summary>test_forms.py</summary>
<img src="docs/testing/automated/testing-auto-contact-forms.png">
</details>
<details><summary>test_views.py</summary>
<img src="docs/testing/automated/testing-auto-contact-views.png">
</details>

#### List App ####
<details><summary>test_forms.py</summary>
<img src="docs/testing/automated/testing-auto-list-forms.png">
</details>
<details><summary>test_views.py</summary>
<img src="docs/testing/automated/testing-auto-list-views.png">
</details>

## Bugs
Notable bugs found during development:



## Deployment
The project was deployed using the online platform Heroku. The following steps were taken:
1. Log in or sign up to the Heroku website:

2. Click the "new" button and then "Create a new app"

3. Choose an app name and region to use, Europe in my case

4. Navigate to the "Settings" tab of the new app and set the config vars:

5. Navigate to the "Buildpacks" section of this page and add Python as a buildpack, and then the nodejs buildpack, so that Python is above nodejs

6. Go to the "Deploy" page and select GitHub as a deploy method, log in via GitHub and then select the desired repository

7. Go to "Manual deploy", make sure the main branch is selected, and click "Deploy"

### Forking
On this project's repository, at the upper-right-hand side, there is a "fork" button to create a fork of it.

### Cloning
On this project's repository, at the upper-right-hand side, there is a "Code" button. To clone the project, click the button and:
- Choose between HTTPS, SSH or GitHub CLI as preferred and click the "Copy url to clipboard" button
- Open Git Bash
- Set the working directory to where the cloned project should be
- Type "git clone " followed by the copied URL
- Hit enter to create the cloned project

## Credits
- Icons: <a href="https://fontawesome.com/icons">FontAwesome</a>

Technology used:
- Languages: HTML 5, CSS, JavaScript, Python
- Database management framework: Django
- IDE: GitPod
- Version control: GitHub
- Deployment: Heroku
- Wireframing: Balsamiq
- Validation: W3C HTML Validator, W3C CSS Validator, JSHints Code Quality Tool, WAVE Website Accessibility Evaluation Tool, PEP8, Google Chrome
- Color palette design: <a href="https://mycolor.space">ColorSpace</a>

### Third Party Libraries

- Django AllAuth is used for its login/signup/logout functions alongside the base Django user features.
- Django Crispyforms is installed to create the forms that users can use to create posts or submit feedback to the admins.
- WhiteNoise is used to allow Django to serve static files such as CSS to deployment apps such as Heroku, necessary so that the site can be styled without having a CDN.

Other:
- Mo Shami for mentoring, guidance and feedback throughout the project.