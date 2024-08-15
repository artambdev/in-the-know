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
The website is designed for two possible users and 8 user stories:

### User: Site User

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

### User: Site Admin

## Design
A few wireframes were made in advance of starting development to plan out the most important features and the structure of code that would be required to accompany them.

The wireframes are presented below:

### Colour
TODO

### Font
TODO

## Features
The website has X pages and X features across them.

### Pages
The X pages are:

- The homepage, where the user is presented with a list of all the website's posts stacked two-by-two and paginated every 8 posts.
- The detailed post view, where users can see a post in detail, the post it's replying to, all of its replies, and can create a reply
- The post creation page where users can write a new post to start a new discussion
- The post editing page where users can rewrite one of their existing posts to make changes
- The Contact page where users can privately submit feedback to the admins

## Validation

### HTML
All pages on the site are validated with the W3C's Markup Validation Service and show no errors or warnings. See each page below:

### CSS
The CSS style used by the site was validated with the W3C's CSS Validation Service, and showed no errors. There is one warning for the external stylesheet of Google Fonts which cannot be checked. See below:

### JavaScript
The JavaScript code used for the post deletion modal was validated with the JSHint Code Quality Tool, showing no errors or warnings.

### Python
<a href="https://pep8ci.herokuapp.com/">PEP8 Python Linter</a> was used to validate all three Python files and no errors are returned.

### Accessibility
All pages on the site are checked with the WAVE Website Accessibility Evaluation Tool, and none show any errors. See each page below:

### Performance
Google Chrome's Lighthouse feature was used to check every page for performance issues, and each returned a high score in all categories. See each page's result below:

### Browser Compatibility
Each page has been tested to work on:

### Device Compatibility
Each page was tested on Mozilla Firefox and Google Chrome's developer tools for responsive design. Testing was done on a desktop PC running Windows 11 and a Galaxy A50 phone.

### User Stories
Below is a list of user stories and the process by which they are fulfilled:

### Automated Testing

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