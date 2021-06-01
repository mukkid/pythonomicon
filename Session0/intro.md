# Programming with Python

## What is programming?
In essence, programming is just writing instructions for a computer in a way that it can understand and run them.

## What do you mean by _understand_
When we program, we usually write down our instructions in something called a _programming language_.
A programming language is sort of like languages we already know (english, japanese, elvish, etc.). We use languages to convey messages to other things.
In human languages, there's a lot of inplied and ambiguous messages that can be conveyed in very few words. For example, telling someone "Nice Going!" is usually
a compliment, but can be sometimes interpreted as a sarcastic insult ("Nice going, dumbass").

When it comes to computers, they aren't very good at understanding ambiguous messages and can't really uncover inplications within language. Programming languages solve
this problem by having the syntax and grammar rules be written in such a way that the meaning of what you write can only be interpreted in one way.

## Is there any particular reason for using Python?
Python (in my opinion) is easy to pick up and learn, but most of the concepts that we learn can readily be applied to any other programming language. When you are more advanced programmers
you may find reason to use specific languages for specific tasks, but at this point it really doesn't matter.

## How do I install Python?
The installation executable can be found at the [Python Website](https://www.python.org/downloads/). Just click through the default options __BUT__ when you are given the 
option of adding stuff to a PATH variable __select the option to do so__.
To see if the installation worked, open the terminal (on windows, press the windows key + r, and type `cmd` and press enter). Then type `python --version` and press enter. If Python is
installed correctly, it should show the version number that you installed. If so, you're all set!

## What do I need to start writing code?
Technically, any text editor will work and is up to preference. However, I suggest using something like [Visual Studio Code](https://code.visualstudio.com/) for beginners. It has fancy highlighting and other tools already built into it.
Just to be clear, the editor you choose to use does not fundamentally matter when programming. You can use notepad if you like. Just remember that you _cannot_ use a word processor such as MS Word or Google Docs.

### (If you did decide to use Visual Studio Code)
If you did decide to use Visual Studio Code as your editor of choice, I would _highly_ recommend installing the python plugin. Your life will be made way easier and in real life, nobody programs without something similar to it.
To do so, open Visual Studio Code, and click on the icon with the 4 blocks on the left bar (Extensions). Then search for the python extension and install it. It's probably the first search result that shows up.

## Writing our first program
Every aspiring programmer's first program is basically the same thing. Write a program to output the phrase "Hello, World!" onto the screen. Pretty simple.
Go ahead and open up a new file in your editor of choice and name it whatever you want. Just remember that you'll want to make the extension (the part of the filename after the dot `.`) as `.py`.
For example, let's call out file, `first_program.py`. Seems reasonable.

Then type/copy the following line
```python
print('Hello, World!')
```
Then save the file and run it. To run the file in Visual Studios Code, click the green "play" button in the top right. You can also run it through the terminal, but that comes later.
If all is working properly, a window should show up and display `Hello, World!`. Congratulations! You've written your first program.