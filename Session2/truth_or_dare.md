# Programming with Python

## Not My Type
In our last lesson, we saw a thing called a _string_. Things like `"hello"`, `"23"` (note the quotes), and `"yo mama's so fat, I needed to buy more RAM just to look at her picture."`. We also got a hint at another type of thing in the line:
```python
a = int(input('type a: '))
```
You may not know exactly what's going on there, but pay attention to the `int` part. When all is said and done, `a` winds up being a number, but not just any number. It is an _Integer_, or `int` as we write in code. An `int` is a **whole** number that can be either positive, negative, or zero.

We have actually seen one more kind of thing, though it might not be as clear as the last two. In the previous sheet, we ran the example:
```python
>>> 5 / 2
2.5
```
Well `5` and `2` are clearly `int`s, but what about the `2.5`? That's certainly not a whole number, so it can't be an `int`. Instead, we call it a `float`. Why is it called a `float`? It's not too important, but essentially numbers like this can have the decimal point anywhere.
For example, `264.32`. Since the decimal point can occur anywhere, we say that it's a _floating point number_ (because the decimal point can float to wherever I guess), and hence, `float`. A history lesson, but not too important

We have been describing different...things so far, but what exactly are we talking about? These are what we call _types_. For example, `"Hello!"` is a _String_ (`str`) type, `42` is an _Integer_ (`int`) type, and `3.1415` is a _Float_ (`float`) type. The _type_ of a thing determines how it can be used. For example, you can add two `int` types such as `3 + 4`, but does it make sense to add an `int` and string like `4 + 'hello'`? Probably not. If you try to do it, Python will get mad and display an error on the screen when it tries to run it.S
```python
>>> 4 + 'hello'
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

As it turns out, almost everything is a _type_ of some sort. If you want to find out what _type_ something is, you can ask python by using the `type()` function (more on functions some other time):
```python
>>> type(42)
<class 'int'>
```
The snippet above is asking "What kind of _type_ is `42`?" and of course the answer is an `int` type.

## You Can Handle The Truth
So far, all our programs do raw calculations. For example, "If you tell me `a` and `b` for the Pythagorean Theorem, I'll tell you `c`." However, we may want to ask and answer questions in our code. Let's pose the following problem:
> Ask the user to enter a number, and see if the number is less than `42`

We know how to do the first part to get the number from the user, but how about the second part? We need to ask the question "Is this number less than `42`?". To do that, we have another operator that you might have seen before: `<`. Let's see it in action.

```python
number = int(input('Enter your number: '))
check = number < 42
print(check)
```
```
Enter your number: 20
True
```
```
Enter your number: 100
False
```
Notice that when we print `check`, it outputs either `True` or `False`. We'll touch upon that in a moment. In addition to the `<` (less than) operator, we have other operators that you'd expect: `>` (greater than), `<=` (less than or equal to), `>=` (greater than or equal to). We can also use `==` (equals to) to see if two things have the same value, and `!=` (not equal to) to see if two things have different values. Pay close attention to the difference between `=` and `==`. `=` is the assignment operator that is used to assign values to variables. `==` is a question operator that asks if the value on the left is the same as the value on the right.

All of the "question" operators that we have covered have something in common: They all ask and answer **only** True or False questions. "Is 20 less than 42? True", "Is 100 less than 42? False". Like `str`, `int`, and `float` from before, `True` and `False` are also their own type. That type is called a _Boolean_ (`bool`) named after the English mathematician George Boole. Boolean values are _always_ either `True` or `False`. There isn't really another way to ask questions in code, so make sure to write your program in such a way that everything is a "yes or no" question.

## Fire Emblem IF
Now that we got a taste of booleans, let's try to use them for something a tad more complicated. It would be nice if we could ask a question, and then have the code change depending on the answer. Well lucky you, we can with our first flow control statement: the `if` statement.

It might be best to show an example and explain what's going on.
```python
number = int(input('Enter your number: '))

if number == 42:
    print('Your number was 42')

print('Game over')
```
```
Enter your number: 42
Your number was 42
Game over
```
```
Enter your number: 10
Game over
```
Here we have an `if` statement in action. From a high level, we can see that _if_ your number was `42`, then it prints `Your number was 42` and then `Game over`. If it was not true (dare I say, `False`), then it _skips_ the indented part and continues on to print `Game over`. To use an `if` statement, we simply just type `if` followed by anything that turns into a boolean type. Notice that neither `number` nor `42` was a boolean, but using the `==` operator, we ask the question "Does `number` have the same value as `42`?" which spits out a `True` or `False` answer. Then end with a `:` followed by a new line.

Now comes the _if block_. That's the stuff that's indented in a bit. Everything that's indented in under the `if` statement will **only** run if the thing next to the `if` statement is `True`.  We can put as many lines of code as we want in this block. For example:
```python
...
...
if number == 42:
    print('Your number was 42')
    favorite = 69
    print('But my favorite number is', favorite)
    print('Nice')
print('Game over')
```
```
Enter your number: 42
Your number was 42
But my favorite number is 69
Nice
Game over
```

You might be asking "Should I indent with spaces or tabs? How many should I use?" The answer is that it really doesn't matter so long as you are consistent. If you decide to use a tab, stick with tabs. Same deal with spaces. If you want an authoritative source like me (what is wrong with you), then you can use 4 spaces. That's a common layout, so common in fact that visual studio code will input 4 spaces if you press the tab key. Handy!

This is handy and all, but let's say we wanted to run some code if our condition was `True`, but do something _else_ otherwise. Well for all your contrarian needs, we have the `else` word.

```python
...
...
if number == 42:
    print('Your number was 42')
else:
    print('Your number was NOT 42')
print('Game over')
```
```
Enter your number: 42
Your number was 42
Game over
```
```
Enter your number: 123123
Your number was NOT 42
Game over
```
Notice that the `else` block only runs if the `if` statement above it didn't run and vice versa.

There is one more situation that we haven't covered. What if you wanted to check to see if the number they typed was 420, but if it wasn't you want to check to see if it was 69. If it was neither of those things, the you can do something else. Let's check out our new key word, `elif` (_Else If_ but shortened).

```python
...
...
if number == 420:
    print('Your number was 42')
elif number == 69:
    print('Your number was 69. Nice!')
else:
    print('Normie number detected')
print('Game Over')
```
```
Enter your number: 69
Your number was 69. Nice!
Game over
```
Again notice that it _only_ runs the block when the statement above it is `True`. We can also toss in as many `elif` blocks as we want if we want to check for more conditions. As always, we can add as many lines as we want to any of these blocks.

## Dormamu I've Come To Bargain
Now that we've shown a pretty powerful use for a boolean, it's time for one more. In the previous homework assignment, you were asked to take input from the user, and print some stuff 3 times in a row. While doing it 3 times isn't a big deal, what if the assignment was to do it 100 times, or 10000 times, or 1000000000 times? I wouldn't want to stick around typing that many lines. Not to worry, we can use something called a _loop_. A loop is sort of what it sounds like; it lets you loop stuff over and over again. There are a few different kinds of loops, but for today we'll focus on the `while` loop. What the `while` loop lets you do is run a block of code over and over again until a certain condition is satisfied. Let's take a look.

```python
number = 1

while number < 5:
    print(number)
    number = number + 1 # Add 1 to our number

print("And we're done!")
```
```
1
2
3
4
And we're done!
```

Here we can see that our `while` loop looks a lot like an `if` statement, and in fact it is syntactically identical. The only difference here is that so long as the condition next to the word `while` is `True`, everything indented under it will run. Once it finishes the block, it jumps back to the `while` condition to see if it's still `True`. If it is, then it runs the block again. And again. And again. Each time we loop, we are adding `1` to our number until eventually `number` is `5`. At that point, it checks the `while` condition as usual, but this time it's `False` (5 is not less than 5). Since it's `False`, the loop stops and the code continues on below. 

Keep in mind that we are changing `number` in the loop. If we forgot to change `number`, we would keep looping, but `number` would _always_ be less than `5`. Essentially, we would be looping _forever_. We call this an _infinite loop_ and it will make your program get stuck, since it's "trapped" in that block forever until you stop the program yourself.

There are times when using an infinite loop is useful, but that'll be covered later. For now, just try to remember `if`, `elif`, `else`, and `while`. These are absolute fundamentals for any programming language and should be mastered. Having said that, mastering them isn't exactly the hardest thing in the world and you could do it in a pretty short time (if not already).

Until next time!

