# Final Project - Physical Computing and the Internet of Things

*Name:*  Camila Vargas Restrepo

*Date:* December 14. 2017

*Size:* 53.34 cm × 53.34 cm (21 in × 21 in)

*Medium* Balsa Wood

## Project: Watching

This birch wood clock that runs on a Raspberry Pi is meant to disorient the audience and make them question the concept of time. It's meant to challenge what the clock represents and how it does so. 

### Detailed Project Description

#### WHAT

**The Clock**

The piece is a 53.34 in diameter clock made out of birch wood. The clock movement mechanism was inspired by the [Starchar Clock](http://thewoodenclock.com/downloads/starchar-clock-plans/) designed by Colin Sprinkle. The mechanism was built following the instructions provided by Sprinkle. The clock is equipped with an hour, minute and second hand which all move thanks to the wood mechanism designed by Sprinkle. The clock moves thanks to a [continuous rotation servo motor](https://www.adafruit.com/product/154) wich is hooked to a [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/). 

The clock has a non traditional face that displays roman numerals that increase counterclockwise ![Clock Face][images/Clock Face.jpg]. As is used in many clocks for [multiple reasons](http://mentalfloss.com/article/24578/why-do-some-clocks-use-roman-numeral-iiii), the clock uses IIII instead of IV to represent 4. 

Embedded in the clock face is a a small [Raspberry Pi Camera Module](https://www.raspberrypi.org/products/camera-module-v2/) that is used to recognize faces as a proxy for detecting if there is someone looking at the clock.

*Scenarios*
* If someone is looking at the clock, the hands will move counterclockwise. Since the numerals increase counterclockwise, time is moving forward in this scenario. 
* If no one is looking at the clock, the hands will move clockwise. Since the numerals increase counterclockwise, in this scenario time is moving backwards. 
* If someone looks at the clock after a period where no one was looking at the clock, the hands will move fast counterclockwise to recover the time "lost" and then return to seconds pace. 

**The Exhibition Space**

Ideally, the clock hangs on a wall in front of a mirror. The wall angled in a way that allows for the audience first impression of the space to be walking towards the mirror while they see the reflection of the clock's face (See Initial Impression). To some, this should be disorienting since the clock's hands appear to be moving forward in the mirror (assume no one else is  in the space, so no one is looking at the clock). The person should then move towards the clock in order to inspect the space. When they turn around to look at the clock (See Inspection) the camera should detect them and have the hands start moving clockwise.

![Space Diagram 1](images/SpaceDiagram1.JPG)

When the person turns around again to re-inspect the mirror (this should / could happen if the person is confused, which is the whole point of the piece) the camera will stop detecting their faces and will start moving the hands counterclockwise. To the audience member who is now looking back at the mirror, the hands are still moving clockwise (See Re-Inspection). 

![Space Diagram 2](images/SpaceDiagram2.JPG)

#### WHY

*The Clock*

For a very long time clocks have fascinated me. When I was in elementary school I once pulled my kitchen's clock apart to use the mechanism for an art project. The choice to build an analogue, wooden clock with was motivated partly by nostalgia and an acknowledgement that times are changing and what used to be a clear representation of time may no longer be so as digital clocks replace analogue ones. 

*The Operationalization of Constructs*

One of the prime characteristics of the information age is our increased capacity to measure and quantify phenomena. We are now able to gather data about almost anything imaginable: from the steps we take to the food we eat, from how long you've been driving to how many friends you have.

Reality mining was introduced by Alex Pentland in the paper [*Reality Mining: Sensing Complex Social Systems*](http://realitycommons.media.mit.edu/pdfs/realitymining.pdf) The authors' goal was to demonstrate "the ability to use standard Bluetooth-enabled mobile telephones to measure information access and use in different contexts, recognize social patterns in daily user activity, infer relationships, identify socially significant
locations, and model organizational rhythms." Reality mining is at the core of our times, we want to measure, quantify and decide. 

If you pair reality mining with solutionism, The belief that all difficulties have benign solutions, often of a technocratic nature. 


But in the end, the number of likes we get is only a proxy for how beautiful we are, the number of friends on facebook is only a proxy for how many friends we have, the steps displayed on our fitbits are only a proxy for how active we were (arguable, it's a proxy for steps as well). A central piece of the Reality Mining puzzle, one that people often forget, is the step where we operationalize our constructs, when we simultaneously decide what the essence of our construct is and what the best way to quantify it is. Then, we make the assumption that our definition is accurate and blend the two to the extent where the boundaries between the two tend to disappear, we forget that likes are not friendships and that clock tickings are not time. 


*Time*

	*“People never seemed to notice that, by saving time, they were losing something else. No one cared to admit that life was becoming ever poorer, bleaker and more monotonous. The ones who felt this most keenly were the children, because no one had time for them any more. But time is life itself, and life resides in the human heart. And the more people saved, the less they had.”* ― Michael Ende, Momo

Momo is a fiction novel by Michael Ende. One day, to the city where Momo lives arrive the Grey Men who present themselves as agents of the Timsavings Bank. They claim that time can be deposited to the bank and be later retrieve it. Yet, the more time people save, the less they have; the time put in the bank is lost forever. 

In the project I wanted to challenge the way we operationalize concepts and how naturalized it's representaiton can become. The orientation of the clock's hands have become something so common, so natural (although arguable we are at the end of an era in that sense) that clocks have effaced numbers from their dials. By flipping the face around, my intention was to create a sense of disorientation and make people think hard about the representation of time. 


*Abstract Concepts and the Arbitariness of their Representations* 

	*"Calendars and clocks exist to measure time, but that signifies little because we all know that an hour can seem as eternity or pass in a flash, according to how we spend it."* - Michael Ende, Momo


What problem is it responding to?  What issue is it engaging?   
  

### Hardware 

* [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/). 
* [continuous rotation servo motor](https://www.adafruit.com/product/154)
* [Raspberry Pi Camera Module](https://www.raspberrypi.org/products/camera-module-v2/)
* [Portable Power Stick](https://getonhand.com/collections/portable-power/products/new-stick-black)

*Hardware Wiring Diagram*
![Wiring Diagram](images/WiringDiagram.png)

This short video illustrates how the clock was put together
[![Process Video](https://img.youtube.com/vi/ZWfhtFWAcsg/0.jpg)](https://www.youtube.com/watch?v=ZWfhtFWAcsg)


#### Software

< Explain your code.  You might include code snippets, either `inline` or
```c++
//Multiline
bool photon_fun = TRUE;
```
You should link to your full code, either included in the repository (e.g. [my_code.ino](code/my_code.ino)  or to the Shared Revision in your Particle IDE. >


### Design / Form

< Explain the device's form, the aesthetic choices made and how they relate to the concept/function the device is intended to engage >

< include photos of your device >

### Evaluation / Reflection

This project was an amazing experience for many reasons. Skill-wise, I learned how to use the CNC, how to use the laser cutters, how to saw, drill, clamp, glue etc. I learned how to use the Raspberry Pi, how to use a continuous servo (although some parts of this are still unclear), and how to use OpenCV to detect faces. I started exploring multiprocessign in Python (although some parts of this are still unclear). 

	*“...it's like this. Sometimes, when you've a very long street ahead of you, you think how terribly long it is and feel sure you'll never get it swept. And then you start to hurry. You work faster and faster and every time you look up there seems to be just as much left to sweep as before, and you try even harder, and you panic, and in the end you're out of breath and have to stop--and still the street stretches away in front of you. That's not the way to do it.

	You must never think of the whole street at once, understand? You must only concentrate on the next step, the next breath, the next stroke of the broom, and the next, and the next. Nothing else.

	That way you enjoy your work, which is important, because then you make a good job of it. And that's how it ought to be.

	And all at once, before you know it, you find you've swept the whole street clean, bit by bit. what's more, you aren't out of breath. That's important, too...”* -Michael Ende, Momo

But this project was also about the process, the process of learning, the patience, recovering from mistakes, and ultimately, dedicating the necessary time. 

< What is your own evaluation of your project?   What did you learn through this project?  What would you do differently in the future? >
