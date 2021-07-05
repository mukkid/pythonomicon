# Programming With Python

## A Bit More Housecleaning

In the past, we have learned to loop a certain number of times. For example in our `fizbuzz` homework problem, we most likely had something like:
```python
count = 0
while count < 100:
    # fizzbuzz stuff
    # ...
    count += 1
```
That works fine and all, but it's a pretty common practice to want to iterate over a series of numbers. Fortunately in the real world, it's a bit easier than that. We have at our disposal, the handy `range()` function. `range()` returns a list (not really, but just go with it) that is filled with numbers that we can iterate through. For example, `range(5)` would give us something that looks like `[0, 1, 2, 3, 4]`.
If we only provide one number, then `range()` will return a list starting from `0` and ending at the number **right before** the number you entered. If you provide two numbers e.g. `range(3, 8)`, then `range()` will return a list that starts at the first number and ends **right before** the last number; in our case: `[3, 4, 5, 6, 7]`. It might be a bit confusing to remember which number is included and which isn't when you enter your numbers. I find it easy to remember by thinking about the _spaces_ between numbers, rather than the numbers themselves.
```
| 0 | 1 | 2 | 3 | 4 | 5 | ...
```
Each pipe character (`|`) represents the space between each number. When you enter arguments for the `range()` function, it'll always start or end at the space **right before** the number you entered.
In our earlier example, we used `range(3, 8)`, which means the list would start the space **right before** the 3, and would end at the space **right before** 8. That gives us the expected answer of `[3, 4, 5, 6, 7]`.

This is cool and all, but the real power comes when you realize that since `range()` returns something that looks like a list, you can use a `for` loop to iterate through it like so:
```python
for number in range(1, 101):
    print(number) # prints numbers from 1 to 100
```

Just to drive home the point, let's redo our earlier `fizzbuzz` homework problem, but using a `for` loop this time.
```python
for number in range(1, 101):
    if number % 15 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)
```

And that's it! No longer do we need to keep track of which number we're on or if we've gone too far or if we need to increment the number. Everything is handled for us.

## A String For Your Troubles

I'll be frank with you, I haven't always been entirely honest. Sometimes it's just too easy to lead a life of vice, but no longer. I am a changed man with a new lease on life.
The truth is, you can index over a string just like you could in a list. What do I mean by this? Remember how you could get a certain element from a list by using `[]`? like `my_list[4]`?
You can do that with a string as well like so: `'hello'[1]'` would be `'e'` since it's the character in 1-th indexed spot. "Okay why is he making a huge deal out of this?" you might be asking.
It means that we can directly iterate through a string with a `for` loop to get each of the characters like so:
```python
my_word = 'supercalifragilisticexpialidocious'
for letter in my_word:
    print(letter)
```
```
s
u
p
e
r
...
...
```

"Alright that's cool I guess, but I still don't get what he's so worked up about" might be echoing around in that noggin of yours. The fact is, it's not true that `for` loops can iterate over only lists, as we can see above. Instead we find (or will find in the future) that `for` loops can iterate over a huge number of things. We call things that `for` loops can iterate through, _iterables_. Makes sense. As I mentioned way above
>>> `range()` returns a list (not really, but just go with it)
            --- Sun Tzu, 2021

It turns out that `range()` _doesn't_ return a list, but something else entirely. _What_ that something is, is something that I don't think we're ready for yet. At the very least, we can call that _something_ an _iterable_ since we are able to iterate through it.

## Look Up High

Speaking of lists and things that are not lists, let's talk about one of the problems with lists. Observe the following:
```python
friend_list = ['Mukund-TooManySnakes', 'Kevin-DankMamay', 'Ebby-Youya', 'Jasmine-Nagi', ... ... ... ...] # Pretend this goes on for a while

def get_name(special_string):
    split_string = special_string.split('-')
    return split_string[0] # Return the first part; the name

def get_username(special_string):
    split_string = special_string.split('-')
    return split_string[1] # Return the second part; the username
```

We are trying to make a friends list sort of thing. We are using a list to store our friend's names and their username. We have also written two functions to help get someone's name or username if we wanted to.
If I wanted to know my third friend's username, I could do something like:
```python
un = get_username(friend_list[2])
print(un)
```
```
Youya
```
Seems nifty and it is. However, what if we wanted to know someone's username if we knew their real name? How would we do that here? We could write a function to help with that; maybe call it `search_username` or something. Let's give that a try.
```python
...
...

def search_username(real_name):
    for special_string in friend_list:
        name = get_name(special_string)
        if name == real_name:
            username = get_username(special_string)
            return username
    return None # Remember we stop at the first return statement. If we got here, it means we never found anyone with that name
```

Our function looks through our friends list and sees if a person's name matches the name we're looking for. If so, it gives us the username of that person. If nobody exists with that name, we get `None` back.
That works well enough, but there's something of an issue. It's fine for people like me with only a handful of friends, but what about someone like you who has hundreds, thousands, or even millions of friends?
Are you _really_ going to search through millions of people just to find someone's username? Remember that although your computer is super fast, problems like these can get out of hand pretty quickly and start slowing down our cpu a lot. There _must_ be a better way than this.

### Enter the dictionary
Luckily smarter people than I thought of a solution to this problem. They created a new type called the _dictionary_ or `dict` for short. What is a dictionary? To put it simply, it's another _data structure_ that holds data like a list. Unlike a list through, it has no concept of order. In a list, there was clearly a "first" element, followed by a "second" element, and so on until the end. In a dictionary, that's not the case. Things are simply _in_ or _not in_ the dictionary.

To differentiate it from a list more, consider the following. A list get you data if you know _where_ it is. For example, above we could find `Youya` in our friends list because we knew that it was in index `2`. If we didn't know that, then we'd have to trudge through the whole list to find what we're looking for.

A dictionary is almost the reverse. You don't care about where something is. Instead you have to specify something called a _key_ which is _what_ you're looking for (notice it's not _where_, but _what_). The dictionary will then return a _value_ that corresponds to the _key_ you provided. This might sound like a lot of mumbo jumbo, but I'll show an example in a bit and hopefully everything makes sense.

To create a dictionary, we use `{}`, sometimes referred to as "curly brackets" or "braces". I say the former, but it's a free country. Let's create one below with our friends list data:
```python
friends = {'Mukund': 'TooManySnakes', 'Kevin': 'DankMaymay', 'Ebby': 'Youya', 'Jasmine': 'Nagi'}

ebbys_username = friends['Ebby']

print(ebbys_username)
```
```
Youya
```
There's a lot of stuff in there, but pay close attention to how we are creating our dictionary. We have a bunch of things separated by commas. These are called _key-value pairs_.
For example, the first one is `'Mukund': 'TooManySnakes'`. The thing to the left of the colon is the _key_ and the thing on the right is the _value_. The space between the colon and the value doesn't matter but it looks nice and tidy. We are saying that the _key_ (in this case, `'Mukund'`) should return the _value_ if it's in the dictionary (in this case, `'TooManySnakes'`). We can see in a later line in the example above where we look up Ebby's username. We ask our dictionary: "Give me the _value_ for whatever is assigned to the _key_ `'Ebby'`". In that case, the value that the dictionary has is `'Youya'`. Remember that we have no idea _where_ either `'Ebby'`, `'Youya'`, or anything else is in our dictionary. That's just how it works.

If we want to add stuff to our dictionary later, we can do it like this:
```python
...
...
# We want to add our new friend "Friendo" who has a username of "Besto Friendo"
friends['Friendo'] = 'Besto Friendo'

print(friends['Friendo'])
```
```
Besto Friendo
```
Simple as that. If by chance `'Friendo'` already was in our dictionary, then his value would be replaced with the new value we are specifying, in our case, `'Besto Friendo'`.

If we try to use a key in a dictionary that doesn't exist, we get an error, similar to how we get an error if we try to index into a list with an index that is outside the bounds.
```python
error_time = friends['Super Friendo']
```
```
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
KeyError: 'Super Friendo' 
```
Notice at the end it is basically saying "I have no idea what the key of `'Super Friendo'` is. We can get around this problem in a few ways. One is to see if our dictionary even has our key in the first place like so:
```python
if 'Besto Friendo' in friends:
    print(friends['Besto Friendo'])
```
We can check to see if a key is in our dictionary using `in`. That returns a boolean, either `True` or `False` depending on if the key is in the dictionary or not. To be honest, it's a bit uncommon to do it like this (though not unheard of). Most people will use this second method, using `.get()`.
```python
print(friends.get('Jasmine'))
print(friends.get('Besto Friendo'))
```
```
Nagi
None
```
Notice instead of getting an error, `.get()` returns `None`. Cool.

## Import The Goods
Some of you may have noticed that in one of our homework assignments, I had you type in `from random import randint` followed by something along the lines of "Don't ask me what this does."
Well the time has come to have the truth revealed. Let's start from the basics. 

What is the `import` keyword and importing in general? Well in a regular python program with no imports, the code runs from top to bottom, and everything you use, must be defined in that very same file.
However, say you had dozens of functions that are useful in a bunch of different places. Or say you had a bunch of projects that all could use similar functions. It's a pain in the ass to rewrite all those functions everywhere. Instead it would be cool to have a single place to define those functions, and you could use them somewhere else. That's where imports come in. Let's write a file titled `my_functions.py` and fill it with some dummy functions.

```python
# my_functions.py

def foo():
    pass # pass just means "don't do anything"

def bar():
    pass

def baz(word):
    pass
```
This file doesn't do anything on its own, but is simply a place for us to store these functions. Now let's make another file called `my_program.py` and try to use those functions.

```python
# my_program.py
import my_functions

my_functions.foo()

my_functions.bar()
```

By importing our earlier file (notice no need to add the `.py` part), we can use the functions in `my_functions.py` from `my_program.py`. We call the thing we are importing, a _module_ or a _library_. You may also notice the weird way we are calling those functions. Instead of just `foo()` or `bar()`, we have to do `my_functions.foo()` or `my_functions.bar()`. This is what we call _namespaces_. Basically, multiple files could have functions that have the same name. To keep everything clear, python makes us use the imported name first as a way of saying "The function came from here".

```python
# my_program.py
import my_functions

def foo():
    pass

foo() # runs the function above
my_program.foo() # runs the `foo` from `my_functions.py`
```

If you want only a few things from a module and don't want to use the full namespace name, we can go one step further and use `from`

```python
# my_program.py
from my_functions import foo, bar

foo() # runs my_function's foo()
bar() # runs my_function's bar()
```

We are saying "We only want `foo` and `bar` from `my_functions` so go ahead and drop them in". I recommend only doing this in personal projects and if the stuff you're importing are pretty uniquely named. For example, it's pretty common to have a function named `run`. If you see `run` in your file, you'd want to know where it was from. If you say `my_functions.run`, it's pretty clear what `run` we're talking about.

Going back to that homework assignment, we used `from random import randint`. From what we just learned, it seems reasonable to guess there's a file called `random.py`, with a function `randint()` in it. We imported that function and used it in our program. We could have just as easily said `import random` and then `random.randint()`. Either one works. You may have noticed that although we were able to `import random` just fine, there is no file called `random.py` as far as we can tell. Well yes and no. These modules are included "for free" with every python program. You can import them without needing to find those files. These modules are called the _standard library_ modules or _stdlib_ for short. There are over 100 stdlib modules such as `random`, `math`, `os`, and even `turtle`. 
All the stdlib modules can be found [online](https://docs.python.org/3/library/index.html) and are very powerful. We'll be using more and more of them as the lessons go on. 

One thing to note is that it's certainly not expected that you memorize every single module out there. More than likely you'll remember a handful of useful ones and just google the rest. Don't worry, that's what everyone else does as well.