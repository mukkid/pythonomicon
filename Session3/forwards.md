# Programming With Python

## The Truth About The Tables
Last time, we covered comparison operators that would output a boolean value. Now we're going to cover three more operators which are usually called _boolean operators_.
Those operators being: `and`, `or`, and `not`.

Boolean operators can be explained mathematically with something called a _truth table_, which outlines all the possible outcomes of using these operators. Starting with `and`, let's take the following example:

```python
sitting_on_the_toilet = True
pants_off = True

poop_time = sitting_on_the_toilet and pants_off
print(poop_time)
```
```
True
```

If you'll go past the variable names, what we have here is a boolean to the left of `and` and another one to the right of it. The `and` operator will turn out to be `True` **only** if **both** sides of the `and` operator are `True`. In truth table form, it would look something like this:

`A`  |`B`  |output of `A and B`
-----|-----|-----
False|False|False
True |False|False
False|True |False
True |True |True

We just substituted `sitting_on_the_toilet` for `A`, and `pants_off` for `B`. The table shows all possible combinations of `A and B`. It might look a bit wild, but trust your intuition: The output is only `True` when `A` _and_ `B` are both `True`. Going back to our earlier example, `poop_time` is only `True` when _both_ `sitting_on_the_toilet` _and_ `pants_off` are `True`. Simple enough.

Now let's move on to `or`. The truth table looks something like this:

`A`  |`B`  |output of `A or B`
-----|-----|-----
False|False|False
True |False|True
False|True |True
True |True |True

Essentially, `A or B` will be `True` when either `A` _or_ `B` are `True`. It doesn't really matter which one is `True`, in fact both could be `True` and it would still work. You just need at least one. Let's look at a more concrete example:

```python
day = 'sunday'

weekend = day == 'saturday' or day == 'sunday'
print(weekend)
```
```
True
```

In this example, we have a variable `weekend` that is set to `True` if either `day == 'saturday'` is `True` _or_ `day == 'sunday'` is `True`. Again, your intuition should help you out here. The only technicality you'll need to remember is that `weekend` will be `True` even if _both_ `saturday` and `sunday` are `True`. I know this isn't possible in real life, but that's just how the operator works. At least one of the two things has to be `True`.

Finally we come to `not`, perhaps the simplest one of the bunch. `not` is what we call a _unary operator_, meaning that it only needs one thing to work, unlike `and` and `or`, (and `+`, `-`, etc.). Let's see the truth table for `not`.

`A`  |output of `not A`
-----|-----
False|True
True |False

It's basically what it says on the tin. Whatever `A` is, `not A` is the opposite. In code, it would look something like:
```python
is_everyone_elses_character_bullshit = True
is_my_character_bullshit = not is_everyone_elses_character_bullshit

print(is_my_character_bullshit)
```
```
False
```

Pretty straight forward. It's somewhat uncommon for `not` to be used all alone like that (though not impossible). More often than not, you'll encounter it in a compound statement with a bunch of parts. For example:
```python
am_i_tired = True
are_the_dishes_dirty = True
are_my_parents_coming_over = False

clean_the_dishes = are_the_dishes_dirty and (not am_i_tired or are_my_parents_coming_over)
print(clean_the_dishes)
```
```
False
```

Here we are trying to determine if I should clean the dishes or not. In plain english, I am saying that I'll clean the dishes if there are any dirty dishes to clean and if I'm not tired or if my parents are coming over. If we break down the code, and substituting the variables, we get `True and (not True or False)`. Going from left to right, we see `True and ...`, and as we know, `and` only is `True` if both sides are `True`. That means we need to check the right side and see if it's `True`. On that side we have `(not True or False)`. Well `not True` is simple enough, that's just `False`. That leaves us with `(False or False`). Since it's an `or` operator, at least one of the two operands needs to be `True`. Since that's not the case, `(False or False)` becomes `(False)`, or more simply: `False`. Now looking at the whole thing we have `True and False` which we know is `False` since the right side didn't turn out to be `True`. This means that I will not be cleaning my dishes today. Lucky!


## A Bit Of Structure
Until now, we've talked about data and data types sort of in a vacuum. By that, I mean that we've sort of just had `int`s, `float`s, `str`s, and `bool`s just hanging out in our code. That's cool and all, but having a bit of structure would be very powerful. This will sound a bit abstract at the start, but just bear with me for a bit. We are going to want to structure our data in the same way that we would want to structure a shopping list. Perhaps obviously enough, a thing that structures our data is what we call a _data structure_. It's nice to have a bunch of words for things you need to buy, but a shopping list becomes useful because things are in an order and structured in a way that makes it easy to use. Speaking of shopping lists, that'll be our first structure (sort of). Introducing the list!

Lists in code are a collection of things that are in a certain order. It doesn't really matter what those things are, but you can group them all together in a list. Let's see an example:

```python
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

print(days)
```
```
['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
```

We can make a list by using the `[` and `]` characters (people tend to call them "square brackets"), and put the stuff we want to be in the list inside separated by commas. Here we've made a list containing strings for each day of the week. Printing out the list shows all the contents. 

We're just getting started though. Lists are what we call _ordered_. That doesn't mean that they are _sorted_ (That's a whole different can of worms), but rather it means that there's clearly a first thing, followed by the second thing, and so on until the last thing. You wouldn't write all your shopping list items and throw them into a bag and call that a list. Ordering is important here. Because lists are ordered, we can ask the list to give us a specific item or _element_ in the list. For example:

```python
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

x = days[2]
print(x)
```
```
wednesday
```

We are asking our list `days` to tell us the element that is at position `2`, which in this case is `wednesday`. This is called _indexing_ the list, and the number we provide is called an _index_. Now if you were paying attention, you might have spotted something strange. "Wait a second, we asked for the item at position `2`, which should be `tuesday`! How come we got `wednesday` instead?!" Clever clever. In Python (and in the majority of other programming languages), indexing doesn't start with the number `1` as we might expect, but the number `0`. This is what we call _zero indexing_. It might seem a bit confusing at first, but you'll pick up on it real fast. To prove it, let's test it out:

```python
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

a = days[0]
b = days[1]
c = days[2]

print(a, b, c)
```
```
monday tuesday wednesday
```
It behaves as we expect (or at least how _I_ expect). 

We can also find out how big our list is by using the `len()` function.
```python
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
number_of_days = len(days)

print(number_of_days)
```
```
7
```
Whew! Still 7 days.

Just be careful to not use an index that it bigger than the size of the list (or try it and see what happens).

We can put whatever we want in our lists, including variables as well as mixing and matching data types. Experiment and try it out!

## Let Me List The Ways
We've seen that lists are a handy way of keeping a bunch of data organized, but there seems to be something we've missed. Sure we can make a list with whatever we want, but it would be nice to modify the list after we've made it. What if we want to add or remove something later? Well there are two useful methods (more on that later) that we can use to do that.

First let's consider the case where we'd want to add something to a list. What if we had a list of my favorite ice cream flavors that looked like:
```python
ice_cream_flavors = ['vanilla', 'strawberry', 'mint chocolate chip']
```
That's cool and all, but yesterday, I had some boba flavored ice cream at a friend's place and really liked it. I'd like to add it to the list without making a completely new list. Well we can do that with the `.append()` method. To _append_ means to stick on the end of something (like the appendix is at the end of a book or your intestine). Let's see how it works:

```python
ice_cream_flavors = ['vanilla', 'strawberry', 'mint chocolate chip']

ice_cream_flavors.append('boba')

print(ice_cream_flavors)
```
```
['vanilla', 'strawberry', 'mint chocolate chip', 'boba']
```
Looks like using `.append('boba')` stuck `'boba'` to the end of our list. We can keep appending to the list if we want. The same friend tells me that they like poop flavored ice cream, so let's add that as well:

```python
ice_cream_flavors = ['vanilla', 'strawberry', 'mint chocolate chip']

ice_cream_flavors.append('boba')
ice_cream_flavors.append('poop')

print(ice_cream_flavors)
```
```
['vanilla', 'strawberry', 'mint chocolate chip', 'boba', 'poop']
```
Unfortunately I'd been bamboozled! When I tried it, it tasted like shit. I'm taking it off the list and having a stern talking to with that friend. How do we remove `'poop'` flavored ice cream from our list? As you might have guessed, there's a different method for that called `.pop()`.

```python
ice_cream_flavors = ['vanilla', 'strawberry', 'mint chocolate chip']

ice_cream_flavors.append('boba')
ice_cream_flavors.append('poop')

ice_cream_flavors.pop()

print(ice_cream_flavors)
```
```
['vanilla', 'strawberry', 'mint chocolate chip', 'boba']
```

As we can see, `.pop()` "pops" off the last thing on our list and gets rid of it. Pretty simple. By the way, don't forget the `.` when using these things. We'll go into this topic at great length in the future, but for now, just think of it as though the dot is saying to the thing on the left of it to do the action on the right. In this case, the dot says "hey `ice_cream_flavors`, go ahead `pop` off the last thing on the list". Lists are some of the most useful and widely used data structures in programming, so make sure to really get a feel for them.

## For Whom Weeps The Storm
Let's go back to that list with the days of the week. What if we wanted to do something simple like print out "Today is monday", but swap out "monday" for every day of the week? Well to do a bunch of similar stuff over and over, we'd need a loop. Let's try it out with the `while` loop we learned before.

```python
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

index = 0

while index < len(days):
    day = days[index]
    print('Today is', day)
    index += 1
```
```
Today is monday
Today is tuesday
Today is wednesday
Today is thursday
Today is friday
Today is saturday
Today is sunday
```

Well it works, I guess. It's nice that I'm able to loop through the list and print stuff out, but it feels like there's so much extra bookwork that we're doing. For example, we need an index to keep track of which element we're trying to access from the list. Since we're using an index, we also need to add 1 to it each time as well or we'd be trapped in an infinite loop. On top of all that, we need to make sure that we remain in the bounds of the list or terrible things will happen, which is why our condition is `index < len(days)`. If we forgot or messed up even one of these things, the loop wouldn't work properly. It just seems annoying for what feels like a very simple problem. Luckily everyone else thought the same thing, and so invented another kind of loop: the `for` loop!

```python
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

for day in days:
    print('Today is', day)
```
```
Today is monday
Today is tuesday
Today is wednesday
Today is thursday
Today is friday
Today is saturday
Today is sunday
```

Isn't that waaaay nicer? No more conditions or index variables! Let's break this down in detail since the `for` loop is **extremely** important to learn properly.
The format looks like:
```python
for VARIABLE in ITERABLE:
    # do whatever you want with VARIABLE
```
We write the word `for`, followed by a variable name that I'm denoting as `VARIABLE`, but it can be called anything. Then you say `in` followed by your list. Technically the correct term is _iterable_ here, but you can just think of it as your list for now. What this does is that it goes through each element in your list, and for each element, it temporarily assigns it to the variable that you named, in this case `VARIABLE`, or in the above case, `day`. Then in the body of the `for` loop, you are free to use that variable however you want. Then in the next cycle, it'll assign the next element to that name and the process repeats until there are no more things in your list. Just to drive the point home, in our days-of-the-week example, we are iterating through the list called `days`. In the first pass, our label which is `day` will be `monday` since that is the first element in our list. We print `day` which outputs the line with `monday`. Then the loop goes to the next element in `days`, which is `tuesday`. Now _`tuesday`_ is assigned to `day` instead of `monday`, and we print `day` again. Only this time, `day` is `tuesday` so we print `Today is tuesday`. The cycle then continues with the rest of the days until the list is empty.

This might take a bit of getting used to, but it's incredibly important to learn. This is the hard part folks! Once you master this, it's all smooth sailing from here on out.

Best of luck!