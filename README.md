# :purple_circle: *GreenUnity* :purple_circle:

![mockup landingpage](./img/readme-img/mockup_home.png?raw=true)

## table of contents

- [objective](#objective)
- [key features](#key-features)
- [user stories](#user-stories)
- [testing](#testing)
- [technologies](#technologies)
- [project status](#project-status)
- [acknowledgements](#acknowledgements)

## objective

to build a responsive 1-page web app for a Community Garden

## key features

- menu + responsive design 

  - ability to navigate to all different sections
  - 

## user stories
- Event Enrollment
  - As a user, I want a simple event enrollment process. 
  - As a user, I need to enroll in multiple events efficiently, providing additional details like special assistance requirements.

- Responsive Experience
  - As a user, I expect a consistent and responsive design for easy use on various devices, prioritizing mobile devices first.

- Quick Navigation
  - As a user, I need quick navigation between sections using arrow buttons for efficient browsing.

- Information Access
  - As a user, I want easy access to technical details about the community garden, including history of the community, vision, mission, opening hours, and current month's events.
  - As a user with a visual impairment, I want to use an application that is compatible with a screen reader so that I can get all info. 

- Footer Information
  - As a user, I find value in the footer for critical information, including the address, a concise impressum, and social media links set to open in new tabs for a seamless experience.


## testing

*manual

- page is responsive (menu, images, style of each section) for tablet, laptop, and wide screens
- menu working, going up arrow after each section working as well
- all links working and opening in a new tab
- all images have alt text or fallback background color and aria-labels are there
- contrast ratio (WCAG AAA) passed

*official validators

- CSS validator: no errors
- HTML validator: 1st errors bc img had size attribute without sourceset atrribute --> fixed
- lighthouse: increased from 63% to 99% by transforming and resizing all my images (using squoosh.app)
- WAVE: no errors

## technologies

HTML | CSS

## project status

project is: finished

## acknowledgements

this project was based on full-stack course @ Code Institute

- images from pexels.com and wikimedia, all commons
