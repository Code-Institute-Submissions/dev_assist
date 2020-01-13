
<h1  align="center">
<a  href="https://dev-assist.herokuapp.com/"  target="_blank"><img  src="/documentation/desktop.gif"  alt="DevAssist Desktop Screen"/></a>
<a  href="https://dev-assist.herokuapp.com/"  target="_blank"><img  src="/documentation/mobile.gif"  alt="DevAssist Mobile Screen"/></a>
</h1>
<h2  align="center">
DevAssist
</h2>
<div  align="center">

  

This is project is part of the 'Full Stack Dev Milestone Project 4' module of the Code Institute Full Stack Software Development course, and is the final project of the course. The website intends to mimic a forum type environment where registered users can raise technical queries and respond to other users queries, with an ecommerce option to donate funds to the site creators. Python, Django, Bootstrap and Stripe technologies will be used to achieve this. The marks from this project contribute to the receipt of a diploma level award. The site can be accessed from https://dev-assist.herokuapp.com/
<br>
This site is purely for educational purposes only and does not provide any services. Do not enter personal information. The Ecommerce backend uses the test version of Stripe and will only work using the test stripe credit card number 4242424242424242, see https://stripe.com/docs/testing for test card details.

<br>
</div>

  

## Table of Contents

1.  [**UX**](#ux)
-  [**Project Goals**](#project-goals)
-  [**User goals**](#user-goals)
-  [**User Stories**](#user-stories)
-  [**Design**](#design)
-  [**Wireframes**](#wireframes)

  
2.  [**Features**](#features)
-  [**Existing Features**](#existing-features)
-  [**Features Left to Implement**](#features-left-to-implement)
3.  [**Database**](#database)
4.  [**Technologies used**](#technologies-used)
5.  [**Testing**](#testing)
6.  [**Coding Notes**](#coding-notes)
7.  [**Deployment**](#deployment)
8.  [**Acknowledgements**](#acknowledgements)
9.  [**Disclaimer**](#disclaimer)

  
## UX

  

### Project Goals

The aim of this project is to create a Full Stack web app to fully demonstrate the learnings throughout the course. A pass in this project is required to pass the course and obtain certification. The site will use Python and the Django Framework with a back-end db (PostgreSQL) for the back-end stack. Bootstrap 4 and HTML will be used on the front-end stack. <br>
The site will mimic an open community support site for development type issues, with the community itself providing the support for other users on the site. Users will be be required to register on the site to add posts or comments. There will also be a donation functionality to demonstrate the use of eCommerce, in this case i will be using Stripe as a payment system. Registered Users will be able to donate small sums which will help keep the site maintained and also allow further future functionalities.
<br>


#### User goals

User goals in brief are as follows:

1. To allow users to register on the site.
2. To allow users to Post a query or comment to the site when logged in.
3. To allow users to edit or delete their Posts
4. To  allow users to submit donations to the site management team to help assist with site maintenance and future additional functionalities

  

#### User Stories
1.  I want to see a brief  summary of the main site sections and  relevant links when i go to the landing page of the site.
2. I want to be able to view my Posts on the site.
3. I want to be able to view Posts by other users to the site.
4.  I want Post per page to be limited to a small amount with the ability to view all reviews through pagination.
5.  Summary of Posts on the community page should have button links to the full Post.
6.  The full Post view should show the original user who created the Post.
7.  The full Post view should show the date of the Post.
8.  The full Post view should allow logged in users to edit or delete their own Posts.
9.  The full Post view should allow any logged in user to add a comment.
10.  The full Post view should show all comments associated with the Post.
11.  There should be an option to register on the site.
12. There should be an option to log onto the site.
13. There should be an option to log out of the site when logged in
14. I want to be able to send a donation to the site via a credit card payment option.
15. I want there to be a cart functionality where i can see what i have added to the cart for the current logged in session.
16. The cart will persist only during the logged in session.
17. There should be a checkout option on the cart page which clicks through to the order form payment screen.
18. The order form checkout page will sumarise the order and show the total payment.
19. The user will be able to add the credit card details and submit the payment with a valid card number(for the purpose of this project this will only be the Stripe test card number).
20. Successful payment will be messaged and the cart cleared on successful submit.
21. I should be able to search through the community posts.



### Design

  
**Fonts**

I decided to use the 'Ubuntu' font from google("[https://fonts.googleapis.com/css?family=Ubuntu](https://fonts.googleapis.com/css?family=Ubuntu)") as i felt that it was an 'easy on the eye' font and aided reading the Posts and comments.


**Colours**


![#757575](https://placehold.it/15/757575/000000?text=+) ***#757575*** ![#a8a9ad](https://placehold.it/15/a8a9ad/000000?text=+) ***#a8a9ad***  ![#fafafa](https://placehold.it/15/fafafa/000000?text=+) ***#fafafa***  
Initially i toyed with the idea of using a 70s style pallet as i found some of the colour schemes of this era interesting. However, once i started doing the project I began to think about using a monochrome style, trying to see if I can make a site looking interesting as possible with a bare minimum of colour.

**Topography**

The site uses bootstrap 4 to be fully responsive across multiple devices. It has been checked on multiple devices using chrome dev tools and physically on Chrome and Firefox on Desktop and a Samsung Galxay S9.The top navigation floats to the right on desktop size windows and collapses down to a drop-down navigation on mobile devices

### Wireframes

WIreFames were created using balsamiq tool with license key provided by the Code Institute. https://balsamiq.com/ and came be found in the  [/documentation ](/documentation) folder at  [/documentation/DevAssist_WireFrames.pdf](/documentation/DevAssist_WireFrames.pdf)  .  The wireframes were created at the very start of the project. Throughout development scope changed,  i adjusted the layouts as appropriate to the projects end goals, there were also new pages added to accommodate journeys not initially thought of that became needed as the project progressed.

  

## Features

### Existing Features

```diff
- TODO
1. Add features here.
```

### Future Features to Implement

Future versions of the project may have the following:
```diff
- TODO
1. Add future features here.
```

 

## Database

```diff
- TODO
1. Add DB detail here.
```

### Database schema

```diff
- TODO
1. Add schema here.
```

  

## Technologies Used

  

This project utilizes Python, Django, Postgres, SQLite, HTML, CSS and JavaScript technologies.

  

-  [Python](https://www.python.org/)
The project uses **Python 3** to create the app, create the routes, create the functions within those routes and handles all back end interactions.

- [JQuery](https://jquery.com)
 The project uses **JQuery** as part of bootstrap 4 and to create a character counter on the text area fields.

-  [Bootstrap 4](https://getbootstrap.com/)
The project uses **Bootstrap** to simplify the structure of the website and make the website responsive easily.

-  **HTML 5 and CSS3**
The project uses **HTML5 and CSS3** for website structure and design.

-  [Google Fonts](https://fonts.google.com/)
```diff
- TODO
Add font detail here.
```
```diff
- TODO
Add Django and postgress details here.
```
-  [GitHub](https://github.com/)
This project uses **GitHub** to remotely store the source code in a repository. The project can be cloned or downloaded from here. See [Deployment](#deployment) section

-  [StackEdit](https://stackedit.io)
This project uses **StackEdit** to build the markdown for this readme file

 
  
  

## Testing

  

I worked in sprints so every task was manually tested thoroughly via flash() messages or expected behaviors. I used my own kanban board with a small whiteboard and Post Its to track tasks. After each task completion, I would fully test it before moving on to the next task.

```diff
- TODO
further test details on unittesting here
```

  

When the project was fully completed i went through the below testing scenarios to further test the project.

  

| Test | Expected |Passed |
| :------------- |:-------------| :-----:|
| User loads the landing page of site | Page displays without error and reviews can be viewed | &#9745; |
```diff
- TODO
Add testcases.
```

## Coding Notes
Some of the features of the code are as follows:
```diff
- TODO
1. Add code explanations here.
```
~~~
im a code block
~~~
## Deployment

I personally used vscode on my local machine to develop the site using Python 3.7.3  and deployed to Heroku via Github.

1. To download or clone the site to your local machine you will need to go to my [repo](https://github.com/alimgee/book-review-milestone-project3) see steps in https://help.github.com/en/articles/cloning-a-repository .
2.  Before you download or clone the site you will need to ensure you have [Python 3.7](https://www.python.org/downloads/) installed. 
3. Once you have Python installed, created a virtual environment as appropriate to you chosen IDE and os.
```diff
- TODO
Additonal steps to deploy here.
```

### Acknowledgements

<strong>Code Institute</strong> tutors for their assistance in getting me this far in the course.

All the folk in the <strong>Code Institute Slack </strong> for their invaluable input to their fellow members development. I also learned a lot for this project from the [Corey Schaffer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) series of you tube videos on python and Django.

```diff
- TODO
more detail here
```


#### Disclaimer

The content of this website is educational purposes only and should not be used on a real world basis.
