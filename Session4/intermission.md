# Programming With Python

## Listing Off A Few More Things
Last time we talked, we had talked about `list`s and a few uses for them. Here we'll be doing what I'll call "cleanup". We'll be covering a few extra tools you can use with lists that we didn't have time to go over earlier. I'll just list them off and give some examples.

### Inserting into a list
Last time we learned how to append items to a list using `.append()`. However, this method always sticks our item to the end of the list (following the definition of "append"). If instead we want to insert our item somewhere in the middle, we'd want to use `.insert()`.
```python
tests = ['test1', 'test2', 'test4', 'test5'] 
tests.insert(2, 'test3')
print(tests)
```
```
['test1', 'test2', 'test3', 'test4', 'test5']
```
`.insert()` is used similarly to how we used `.append()` The only different now is that instead of just providing what you want to append, you need to tell `.insert()` where you want your item to go. Specifically, the first number you enter is where your item will be squeeze in. Everything to the right will be moved over by one to make space.

### Combining lists
If we have two lists, and want to smash them together to make a larger list, we can revisit our old friend, the `+` operator. What?! How come I can use the `+` operator here too? Don't worry about it. All will be made clear some other day. For now, just know that you can "add" together lists to make a longer list like so:
```python
list_1 = ['one nothing wrong with me', 'two nothing wrong with me']
list_2 = ['three nothing wrong with me', 'four nothing wrong with me']
list_3 = list_1 + list_2
print(list_3)
```
```
['one nothing wrong with me', 'two nothing wrong with me', 'three nothing wrong with me', 'four nothing wrong with me']
```

### Sorting lists
We can also sort lists of stuff which is pretty handy. It's pretty common to want to sort stuff, so let's see how it works.
```python
list_of_numbers = [4, 2, 1, 6, 10, 3]
sorted_list_of_numbers = sorted(list_of_numbers)
print(sorted_list_of_numbers)

list_of_strings = ['xray', 'foxtrot', 'sierra', 'alpha', 'charlie', 'echo']
sorted_list_of_strings = sorted(list_of_strings)
print(sorted_list_of_strings)
```
```
[1, 2, 3, 4, 6, 10]
['alpha', 'charlie', 'echo', 'foxtrot', 'sierra', 'xray']
```
Notice that when we sort our first list with numbers, it does it from lowest to highest. The second list, which is just strings, is sorted alphabetically. Cool.

## String On A Few More Things
Just like how we managed to cram random stuff about lists, I'm about to cram random stuff about `str`ings as well, so hold on.

### Combining strings
Again, just like lists, we can add strings together to combine them.
```python
first = 'one step closer to the edge,'
second = " and I'm about to break."
line = first + second
print(line)
```
```
one step closer to the edge, and I'm about to break.
```
Straightforward enough.

### Splitting strings
This is a bit more specialized, but we can split our string into smaller strings called sub-strings. Let's see an example and we'll explain it from there.
```python
long_string = 'To be or not to be'
list_of_strings = long_string.split(' ')
print(list_of_strings)
```
```
['To', 'be', 'or', 'not', 'to', 'be']
```

We use `.split()` to... well... split our string. We give `.split()` a character, and python will use that character like a blade and slice our string along those characters. In the example above, we provided `' '`, or just a space. Notice that a space (`' '`) is _not_ the same an empty string (`''`). Keep that in mind.

### Back together again
We can split our string into a list of strings, so it's only natural that we could take a list of strings and combine it back into a single string.
```python
list_of_strings = ['toobie', 'aurnaught', 'tobee']
long_string = ' '.join(list_of_strings)
print(long_string)
```
```
toobie aurnaught tobee
```
This one makes sense in concept, but might be a bit tricky in practice. We are probably doing the reverse of what you'd expect. Pay attention here, since it's easy to confuse. We are taking a string (in this case, `' '`, the space character), and using `.join()`. We then tell `.join()` the list of strings we want to combine. It then takes the first character we specified, the space (`' '`), and puts them in between each element in the list. In the end it gives us back the combined string. It's somewhat of a wild ride, but just reverses what we did in `.split()`. Feel free to google it and practice.

## Any Type You Want
A bit of whiplash, but remember types? Like `int`, `str`, and what not? Remember how I mentioned that depending on the type, you can only do certain things? That's still true, but say we want to take a string of a number, and convert it into an `int` so we can do some math. We'll in comes type conversion. It's pretty simple to use. In fact, you've used it before, probably without realizing it.
```python
number_but_string = '42'
number_for_real = int(number_but_string)
print(number_for_real * 2)
```
```
84
```
Essentially, you just take the type you want, in this case `int`, and just slap your variable right after it. Easy peasy. We can do the same thing with `float`, `str`, or whatever else you want. If you recall to when we used `input('Type your input')`, it always gave us a string. However, if we wanted to input a number, remember we typed `int(input('Type your number'))`. All we did was take whatever our input was, and convert it into an `int`. Now you know.

## Function Over Form
Alright nerds pay attention. This is one of the most important concepts in programming. You might have noticed that we've been using these things that end with parentheses. Stuff like `input()`, `sorted()`, and even `print()`. These are what we call _functions_. A _function_ is sort of like a box where you put stuff in, and it does something and gives something back to you. For instance, you pass a list of stuff to the `sorted()` function, and it does... something, and gives you back another list with your stuff sorted. Another example is if you remember back to math(s) class where you could write a function for graphs. Stuff like:

<img src="https://render.githubusercontent.com/render/math?math=f(x) = x + 5">

This defines a function that we're calling <img src="https://render.githubusercontent.com/render/math?math=f">, that takes in some <img src="https://render.githubusercontent.com/render/math?math=x">, and returns some other number. The way the function works is defined by <img src="https://render.githubusercontent.com/render/math?math=x + 5">.

Let's see how this works in python:
```python
def double_my_number(number):
    doubled_number = number * 2
    return doubled_number

n = double_my_number(21)
print(n)
```
```
42
```

Let's take a closer look here. We are _defining_ a function using `def`, followed by what you want your function to be called. In our case, we are defining a function and calling it `double_my_number`. Right after that, we write parentheses, followed some variables names. These names are what we call _parameters_. They are what we use as labels for stuff that we pass into our function. The names of these parameters don't really matter, but it's handy to keep them descriptive. Inside the function body, we can do whatever we want, and we're allowed to use our variable `number` however we want. The key to remember is the `return` keyword. In a function, the `return` keyword basically means "once you see this word, stop the function and go back to where we were". If you have anything to the right of the `return` keyword, that is what the _output_ of the function would be.

When we use our function, we _pass_ a number, `21` to our `double_my_number` function. This `21` is called an argument which we tell our function to double. In our function, `number` becomes `21` in this case. We then double our number and assign it to `doubled_number`. Now for the important part. We use `return` and the thing to the right of `return`, in this case, `doubled_number`, is what our function will spit out when it's done. Essentially, `double_my_number(21)` _returns_ the number `42` because of that `return` statement.

You are free to use any programming advanced tech in your function body. Functions let you organize your code and helps you not have to rewrite code all the time.
