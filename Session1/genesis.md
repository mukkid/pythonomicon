# Programming with Python

## In The Beginning
In our previous example, we wrote a quick program that outputted `Hello, World!` onto the screen. Let's go over what just happened in not enough detail.
Python is what we call, an _interpreted_ language. It's not important that you remember this specific term, but I'll mention it anyways. Essentially what it means
is that when you write some code into a file and run it, each line gets run from top to bottom. In our case, we only had one line, but if we made something like:
```python
print('Hello, World!')
print('Hello, Universe!')
```
and then ran it, our output would look something like:
```
Hello, World!
Hello, Universe!
```

Seems reasonable.

However, there is also another way to run code. We can use something called the **REPL**.

## The **REPL**?
Yeah, the REPL. It's an abbreviation for **Read, Evaluate, and Print Loop**. Again, not something you need to know, but what it does is that it lets us type in a line
of code, and it'll run instantly. We can then write another line, and it'll run that too. It's a handy tool that lets us mess around with programming without getting to formal with it.
Think of it as scratch space for experimenting. To use our basic python REPL, we can open it by opening the terminal (You do remember how to do that, right? Windows key + R, type `cmd` and press enter),
and just typing `python` and pressing enter.
If you did it right, it should look something like this:
```
Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
The text above the triple arrows don't really matter and may look a bit different from what I have here, but this is the basic python REPL. The triple arrows (`>>>`) means that python is ready for us to enter something.
Let's give it a spin!

```
>>> print('This is the REPL!')
This is the REPL!
```

and we can type more stuff:
```
>>> 5 + 2
7
```
See how we don't have to make write this stuff down in a file to run it? Pretty handy for testing stuff. Of course if you want to keep what you wrote, putting it in a file is the way to go.

By the way, you can quit the REPL by typing in `exit()` and pressing enter, or closing the terminal.

## Time To Start
Now that we've gotten that out of the way, we can start doing some fun stuff. We've already messed around with `print`ing text to the screen using the `print` function (but more on functions later).
You may have also noticed that in an earlier example, we were able to do some rudimentary math. We can do more than just add baby.
```python
>>> 2 + 5
7
>>> 9 - 4
5
>>> 3 * 8
24
>>> 5 / 2
2.5
>>> 2 ** 4
16
>>> 9 % 4
1
```

Those last one or two might be unfamiliar. using two stars (`**`) is the power operator. That example is saying _"Two to the power of four"_. The one after that is probably more unknown. The `%` operator
is called the _Modulus_ operator. If you remember back to your youth, airport security was like division: simpler. When we did _9 / 4_, we used to say, _"How many times does 4 go into 9?"_. Well, 2 times, of course.
But then what of the remainder? Before we learned fractions, we might have just said "9 / 4 is 2 with a remainder of 1". Now you might be catching on. That remainder is what the _modulus_ operator calculates. Go ahead
and test it out with some other numbers in the REPL to see for yourself.

## What about `=`? Well It Varies
True, all the other basic math symbols seem to be present. Surely the equals sign does what we expect?

Well, not quite. In python (and indeed in nearly every programming language ever), the `=` symbol is the _Assignment_ operator. In regular math, the equals symbol might be seen in something like "4 + 9 = 13". What is that saying?
It is basically saying that whatever is to the left of the "=" is the same as whatever is on the right when all the math is done. While this may be true in math, it's not quite the same in programming.
Let's use it in an example and explain as we go along.
```python
x = 3 + 5
```
Now it might seem like we're just doing the same thing, but notice the `x` on the left of the `=` operator. What we are **NOT** saying is that "`x` is the same value as `3 + 5` (8)". Instead what we are saying is "**MAKE** `x` be the value of `3 + 5`.
We are _assigning_ the value of `3 + 5` to `x`. We can then use `x` in the future to do other stuff in place of writing `3 + 5` everywhere. For example:
```python
x = 3 + 5
print(x)
```
```
8
```
And even...
```python
x = 3 + 5
print(x - 6)
```
```
2
```
One more thing to notice is that our assignment always goes in one direction. Whatever is on the right gets assigned to whatever is on the left and _never_ the other way around. To really hit the point home, we can see that in fact, the assignment operator has nothing to do with math at all.

```python
x = 'I am being assigned!'
print(x)
```
```
I am being assigned!
```
See how we told the computer "Make `x` be the value of `'I am being assigned!'`". When used like this, we call `x`, a _Variable_. It's called that because the value of `x` is whatever we tell it to be.
To go even further, there's nothing special about the name `x` in particular. We can call our variable `I_poop_this_many_times` (note the underscores) and use it like this:
```python
I_poop_this_many_times = 4
print(I_poop_this_many_times)
```
```
4
```
There are rules on variable names such as:
* Has to be one continuous "word" (so no spaces)
* Can't start with a number
* Don't use special words which will become apparent in future lessons

But other than that, you're free to use whatever variable names you want.

## One For The Road
I'll end this wall of text with something that I won't fully explain until later.
When you write your programs, you can use input from the user (the person running the program). It looks something like this:
```python
user_input = input('Type your input here')
print(user_input)
```
And when we run it, we see it prompt us:
```
Type your input here
```
It is waiting for you to type your input and press enter. The message that comes up is whatever you typed between the parentheses after `input`. After that, it'll save whatever you typed into a variable, in this case `user_input`. Remember you could use any variable name you want. It'll then just print what you typed back to the screen.
Feel free to mess around with programs of your own with user input like this.

One more thing to note is that if you want to do math stuff with whatever the user types in, you'll need to modify the line `input('Type your input here')` to `int(input('Type your input here'))`. I'll explain why later, but it's pretty fun to just play around with it.

Enjoy!