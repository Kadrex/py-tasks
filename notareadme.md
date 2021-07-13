# Super nice task

Your will have to make a webpage. 
You may choose what kind of webpage it will be but there are requirements.
I will also (... can't remember what I wanted to write :/)

## What you will learn
* Prototype creation
* Angular - ts, html, scss, REST, etc.
* Material Design (styling library)
* Spring Boot + Security (maybe, I guess)
* Docker!!!!
* Prolly a lot more that I can't recall

## Webpage requirements
* Account stuff (register, login, logout)
* Has to be pretty (use material design for styling)
* It has to have a point - not a page where you show ten pictures of bottles and that's it.
It's got to have a flow.


## What to do

* Create a prototype of the webpage you're going to make.
Use Adobe XD (Kadri uses this), Figma or any other prototype/mockup creating software.
* Implement the prototype in Angular.
* Create database for storing data.
* Create backend for providing frontend with data and saving its data.
* Deploy, put 'em in Docker (sort of optional maybe).
* Keep it all in git!

### Prototype creation
Choose a prototype creating tool you'd like to use.
Adobe XD is a software you have to install, Figma is a web application so no installment is necessary.
I have only used Adobe XD, so I don't know to recommend anything.  

**Tip**: When creating the prototype, make the looks based on the styling library you're going to use.
It doesn't have to be exactly like the styling library but don't put sth in there that you can't actually use or make.  
**Tip**: Don't spend too much time on the prototype. It's just a visual reminder of what you're going
to do, and you won't exactly need it later on (unless you want to apply for a designer position, maybe you could show it).  


### Implementing prototype
First you will need to create a frontend project or download a template.  
If you choose to create a frontend project:  
* Follow this guide: https://medium.com/@skywalkerhunter/create-angular-in-intellij-idea-101-985b6359dd75 (it only has two steps, super easy!)
  * Wait
  * Wait
  * Wait
  * Wait
* Start coding!
  * To run your app, simply write `ng serve` in the IntelliJ terminal and open http://localhost:4200/
    That's where your application runs
  * All the logical components should be separate components. But don't worry, ng will generate them for you:
    * In IntelliJ terminal, navigate to src/app (`cd src/app`)
    * Run `ng generate component <component-name>` command
    * A new component has been added! (Don't forget to add it to git later)
    * To use this new component, in your **other** html file, write <app-component-name> and it will offer it to you.
      (Do not forget the closing tags, I'm just writing a guide here, not perfect-syntaxed code)
  * Navigation https://angular.io/tutorial/toh-pt5
  
* When you start using Material Design, you got to add it to the project
  * Run `ng add @angular/material` command in the IntelliJ terminal
  * It asks you stuff in the terminal, answer. Choose a theme, any theme, really
  * Now you can use material components just by writing <mat-...> (for example <mat-icon>) and
  it will give you the option for it and auto import it for you if you choose it
