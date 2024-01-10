# :purple_circle: *GreenUnity* :purple_circle:

Welcome to GreenUnity's homepage – the heart of our community garden. Discover a space where nature and community intertwine, offering hands-on gardening experiences, educational opportunities, and a sense of belonging. The homepage is the gateway to a thriving community committed to sustainable living and shared knowledge. Explore the value of being a part of GreenUnity, where you can cultivate not only plants but also lasting connections and a richer understanding of the environment. 

![mockup landingpage](./assets/img/readme-img/mockup_home.png?raw=true "image of mockup home screen for different devices")

🌱 The deployed page can be found [here](https://zabokaa.github.io/GreenUnity/) 🍃

## Table of Contents

- [UX Design](#ux-design)
- [Key Features](#key-features)
- [User Stories](#user-stories)
- [Testing](#testing)
- [Technologies](#technologies)
- [Project Status](#project-status)
- [Acknowledgements](#acknowledgements)

## UX Design

- to build a responsive 1-page web app for a Community Garden
- low-threshold access for users without social media accounts

## Key Features

- Menu and Responsive Design
  - **Responsive Design:** The webpage follows a mobile-first approach, ensuring optimal user experience across various devices.
  - **Menu Navigation:** The page features an intuitive menu for easy navigation, allowing users to access different sections.

- Event Display
  - **Text-Only Display for Mobile:** Events are presented in a text-only format on mobile devices --> enhance readability and user experience.
  - **Image Display for Tablet and Laptop:** Events are showcased with pictures on tablet devices and arranged in two-per-row format for laptops.

- User Enrollment
  - **Event Enrollment:** Users can enroll in one or more events by providing their names and email addresses.
  - **Additional Information:** Users have the option to include additional details, such as special assistance requirements --> better communication and event coordination.

- Quick Navigation
  - **Arrows for Scroll Navigation:** Arrows below each section enable users to quickly navigate to the top of the page.

- Information Sections
  - **Community Garden Development:** Users can find information about the development of the community garden -->  transparency and engagement.
  - **Vision and Mission:** A dedicated section outlines the vision and mission of the community, providing users with a deeper understanding of its purpose.
  - **Opening Hours:** Clear details about the operating hours are available for user convenience.
  - **Monthly Events:** Users can easily access info about events scheduled for the current month, facilitating event planning and participation.

- Footer
  - **Comprehensive Footer:** The footer contains essential information, including the address, a brief impressum, and links to social media.
  - **New Tab Links:** Social media links open in new tabs, ensuring users remain on my page.

## User Stories

- Responsive Experience
  - As a user, I expect a consistent and responsive design for easy use on various devices, prioritizing mobile devices first.

- Event Enrollment
  - As a user, I want a simple event enrollment process.
  - As a user, I need to enroll in multiple events efficiently, providing additional details like special assistance requirements.

- Quick Navigation
  - As a user, I need quick navigation between sections using arrow buttons for efficient browsing.

- Information Access
  - As a user, I want easy access to technical details about the community garden, including history of the community, vision, mission, opening hours, and current month's events.
  - As a user with a visual impairment, I want to use an application that is compatible with a screen reader so that I can get all info.

- Footer Information
  - As a user, I find value in the footer for critical information, including the address, a concise impressum, and social media links set to open in new tabs for a seamless experience.

## Testing

- Manual

  - Page is responsive (menu, images, style of each section) for tablet, laptop, and wide screens
  - Menu working, going up arrow after each section working as well
  - All links working and opening in a new tab
  - All images have alt text or fallback background color and aria-labels are there
  - Contrast ratio (WCAG AAA) passed

- Official validators

  - [W3C HTML Validator](./assets/img/readme-img/html_validation.png): No errors 
  - [W3C CSS Validator](./assets/img/readme-img/CSS_validation.png):  First I had an error because my img tags in the events section had a size attribute without a srcset atrribute --> fixed: no errors 
  - [Lighthouse Chrome DevTools](./assets/img/readme-img/lighthouse_afterResizingImg.png): Values for accessibility / best practise / SEO all 100, increased performance value from 74 to 99 by transforming and resizing all my images 
  - [WAVE](./assets/img/readme-img/wave_validation.png): No errors for accessibility and color contrast
 
- Unfixed Bugs
  
  - On mobile phones, the dropdown menu in the navigation covers the page content, preventing the user from immediately seeing the top of that specific section. To address this issue, they must close the menu. Imo, this cannot be fixed using vanilla HTML alone.

## Technologies

HTML | CSS

## Project Status

Project is: finished

## Acknowledgements

This project was based on full-stack course @ Code Institute.

- Image of raised-bed from  wikimedia.com, all other images from pexels.com
- Images edited with squoosh.app
  
