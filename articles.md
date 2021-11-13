

This page lists the very best Python engineering articles of the internet, hand-picked to give hours and hours 
of pure reading joy.
It is especially designed for onboarding new members on your Python team. Great for skilling up.
Though not necessarily read one after the other, the order is nevertheless not random. 
For example, knowledge of CPython internals specially bytecodes are necessary to make sense of B. Cannon's 
unravelling series. 
The articles are focused on core Python and it's as advanced as articles can get.
You can send pull requests [here](https://github.com/Abdur-rahmaanJ/python-engineering-articles)


## Encoding

| To Read | Author | Notes |
|-|-|-|
| [Unicode Book](https://unicodebook.readthedocs.io/) | Victor Stinner | Also discusses Python handling |

## Maths

| To Read | Author | Notes |
|-|-|-|
| [Math Symbols Explained With Python](https://amitness.com/2019/08/math-for-programmers/) | Amit Chaudhary |  |
| [Foundations Of Applied Mathematics](https://foundations-of-applied-mathematics.github.io/) | Profs And Students At Different Universities | A series of four textbooks developed for Brigham Young University’s Applied and Computational Mathematics degree program for beginning graduate and advanced undergraduate students. Uses Python for concepts |

## Compiler Theory

| To Read | Author | Notes |
|-|-|-|
| [Building Finite State Machines With Python Coroutines](https://arpitbhayani.me/blogs/fsm) | Arpit Bhayani |  |
| [Writing A Python To C Compiler In Python](https://notes.eatonphil.com/writing-a-simple-python-compiler.html) | Phil Eaton |  |
| [Writing A Jinja-Inspired Template Library In Python](https://notes.eatonphil.com/writing-a-template-library-in-python.html) | Phil Eaton |  |
| [Writing A Simple Json Parser](https://notes.eatonphil.com/writing-a-simple-json-parser.html) | Phil Eaton |  |

## CPython Internals

| To Read | Author | Notes |
|-|-|-|
| [Your Guide To The Cpython Source Code](https://realpython.com/cpython-source-code-guide/) | Anthony Shaw |  |
| [Internals Of Cpython 3.6](https://intopythoncom.files.wordpress.com/2017/04/internalsofcpython3-6-1.pdf) | Prashanth Raghu |  |
| [Advanced Internals Of Cpython 3.6](https://intopythoncom.files.wordpress.com/2017/04/merged.pdf) | Prashanth Raghu |  |
| [Python Development Documentation](https://pythondev.readthedocs.io/) | Victor Stinner |  |
| [Lifecycle Of A Python Code - Cpython’S Execution Model](https://dev.to/btaskaya/lifecycle-of-a-python-code---cpythons-execution-model-85i) | Batuhan Osman Taşkaya |  |
| [A Python Interpreter Written In Pythonn](http://aosabook.org/en/500L/a-python-interpreter-written-in-python.html) | Allison Kaptur | Introduction to Python bytecode |
| [Notes About A Web Assembly Backend](https://snarky.ca/what-is-the-core-of-the-python-programming-language/) | Brett Cannon |  |
| [Summary Of Sam Gross' Nogil Proposal](https://lukasz.langa.pl/5d044f91-49c1-4170-aed1-62b6763e6ad0/) | Łukasz Langa |  |
| [Python C Api: Add Functions To Access Pyobject](https://vstinner.github.io/c-api-abstract-pyobject.html) | Victor Stinner |  |
| [C Api Changes Between Python 3.5 To 3.10](https://vstinner.github.io/c-api-python3_10-changes.html) | Victor Stinner |  |
| [Creation Of The Pythoncapi_Compat Project](https://vstinner.github.io/pythoncapi_compat.html) | Victor Stinner |  |
| [Make Structures Opaque In The Python C Api](https://vstinner.github.io/c-api-opaque-structures.html) | Victor Stinner |  |
| [Isolate Python Subinterpreters](https://vstinner.github.io/hide-implementation-details-python-c-api.html) | Victor Stinner |  |
| [Hide Implementation Details From The Python C Api](https://vstinner.github.io/isolate-subinterpreters.html) | Victor Stinner |  |
| [Leaks Discovered By Subinterpreters](https://vstinner.github.io/subinterpreter-leaks.html) | Victor Stinner |  |
| [Gil Bugfixes For Daemon Threads In Python 3.9](https://vstinner.github.io/gil-bugfixes-daemon-threads-python39.html) | Victor Stinner |  |
| [Threading Shutdown Race Condition](https://vstinner.github.io/threading-shutdown-race-condition.html) | Victor Stinner |  |
| [Threading Shutdown Race Condition](https://vstinner.github.io/threading-shutdown-race-condition.html) | Victor Stinner |  |
| [Pass The Python Thread State Explicitly](https://vstinner.github.io/index2.html) | Victor Stinner |  |
| [Asyncio Wsasend() Memory Leak](https://vstinner.github.io/asyncio-proactor-wsasend-memory-leak.html) | Victor Stinner |  |
| [Asyncio: Wsarecv() Cancellation Causing Data Loss](https://vstinner.github.io/asyncio-proactor-wsarecv-cancellation-data-loss.html) | Victor Stinner |  |
| [Asyncio: Proactor Connectpipe() Race Condition](https://vstinner.github.io/asyncio-proactor-connect-pipe-race-condition.html) | Victor Stinner |  |
| [Asyncio: Proactor Cancellation From Hell](https://vstinner.github.io/asyncio-proactor-cancellation-from-hell.html) | Victor Stinner |  |
| [How I Fixed A Very Old Gil Race Condition In Python 3.7](https://vstinner.github.io/python37-gil-change.html) | Victor Stinner |  |
| [History Of The Python Private C Api _Pytime](https://vstinner.github.io/pytime.html) | Victor Stinner |  |

## Insider Bits

| To Read | Author | Notes |
|-|-|-|
| [Constant Folding In Python](https://arpitbhayani.me/blogs/constant-folding-python) | Arpit Bhayani |  |
| [Integer Caching In Python](https://arpitbhayani.me/blogs/python-caches-integers) | Arpit Bhayani |  |
| [Super Long Integers In Python](https://arpitbhayani.me/blogs/super-long-integers) | Arpit Bhayani |  |
| [Unravelling Decorators](https://snarky.ca/unravelling-decorators/) | Brett Cannon |  |
| [Unravelling Data Structure Displays](https://snarky.ca/unravelling-data-structure-displays/) | Brett Cannon |  |
| [(Not) Unravelling Generator Expressions](https://snarky.ca/not-unravelling-generator-expressions/) | Brett Cannon |  |
| [Unravelling The `Async With` Statement](https://snarky.ca/unravelling-the-async-with-statement/) | Brett Cannon |  |
| [Unravelling `Async For` Loops](https://snarky.ca/unravelling-async-for-loops/) | Brett Cannon |  |
| [Unravelling `Async` And `Await`](https://snarky.ca/unravelling-async-and-await/) | Brett Cannon |  |
| [Unravelling The `With` Statement](https://snarky.ca/unravelling-the-with-statement/) | Brett Cannon |  |
| [Unravelling The `Pass` Statement](https://snarky.ca/unravelling-the-pass-statement/) | Brett Cannon |  |
| [Unravelling `For` Statements](https://snarky.ca/unravelling-for-statements/) | Brett Cannon |  |
| [Unravelling Assertions](https://snarky.ca/unravelling-assertions/) | Brett Cannon |  |
| [Unravelling The Import Statement](https://snarky.ca/unravelling-the-import-statement/) | Brett Cannon |  |
| [Unravelling Boolean Operations](https://snarky.ca/unravelling-boolean-operations/) | Brett Cannon |  |
| [Unravelling Membership Testing](https://snarky.ca/unravelling-membership-testing/) | Brett Cannon |  |
| [Unravelling `Not` In Python](https://snarky.ca/unravelling-not-in-python/) | Brett Cannon |  |
| [Unravelling `Is` And `Is Not`](https://snarky.ca/unravelling-is-and-is-not/) | Brett Cannon |  |
| [Unravelling Rich Comparison Operators](https://snarky.ca/unravelling-rich-comparison-operators/) | Brett Cannon |  |
| [Unravelling Unary Arithmetic Operators](https://snarky.ca/unravelling-unary-arithmetic-operators/) | Brett Cannon |  |
| [Unravelling Augmented Arithmetic Assignment](https://snarky.ca/unravelling-augmented-arithmetic-assignment/) | Brett Cannon |  |
| [Unravelling Binary Arithmetic Operations In Python](https://snarky.ca/unravelling-binary-arithmetic-operations-in-python/) | Brett Cannon |  |
| [Unravelling Attribute Access In Python](https://snarky.ca/unravelling-attribute-access-in-python/) | Brett Cannon |  |
| [How The Heck Does Async/Await Work In Python 3.5?](https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/) | Brett Cannon |  |

## Sane Bits

| To Read | Author | Notes |
|-|-|-|
| [An Approach To Lazy Importing In Python 3.7](https://snarky.ca/lazy-importing-in-python-3-7/) | Brett Cannon |  |
| [Customizing Class Creation In Python](https://snarky.ca/customizing-class-creation-in-python/) | Brett Cannon |  |
| [Why Pathlib.Path Doesn'T Inherit From Str In Python](https://snarky.ca/why-pathlib-path-doesn-t-inherit-from-str/) | Brett Cannon |  |
| [Why Python3?](https://snarky.ca/how-to-pitch-python-3-to-management/) | Brett Cannon |  |
| [Why `Print` Became A Function In Python 3](https://snarky.ca/why-print-became-a-function-in-python-3/) | Brett Cannon |  |
| [If I Were Designing Python'S Import From Scratch](https://snarky.ca/if-i-were-designing-imort-from-scratch/) | Brett Cannon |  |
| [Try To Not Use The Python C Api Directly](https://snarky.ca/try-to-not-use-the-c-api-directly/) | Brett Cannon |  |
| [Lambdas As A Solution For Puzzles](https://blog.astrosnail.pt.eu.org/2021-02-11-snake.html) |  |  |

## Performance

| To Read | Author | Notes |
|-|-|-|
| [Python Performance: It’S Not Just The Interpreter](https://blog.kevmod.com/2020/05/python-performance-its-not-just-the-interpreter/) | Kevin Modzelewski | Worked on the Pyston project |
| [Accelerate Numpy Using Tensorflow](https://blog.kevmod.com/2017/06/update-on-numpy-acceleration/) | Kevin Modzelewski |  |
| [Clinging To Memory: How Python Function Calls Can Increase Memory Use](https://pythonspeed.com/articles/function-calls-prevent-garbage-collection/) | Itamar Turner-Trauring |  |
| [Where’S Your Bottleneck? Cpu Time Vs Wallclock Time](https://pythonspeed.com/articles/blocking-cpu-or-io/) | Itamar Turner-Trauring |  |
| [Beyond Cprofile: Choosing The Right Tool For Performance Optimization](https://pythonspeed.com/articles/beyond-cprofile/) | Itamar Turner-Trauring |  |
| [Not Just Cpu: Writing Custom Profilers For Python](https://pythonspeed.com/articles/custom-python-profiler/) | Itamar Turner-Trauring |  |
| [Ci For Performance: Reliable Benchmarking In Noisy Environments](https://pythonspeed.com/articles/consistent-benchmarking-in-ci/) | Itamar Turner-Trauring |  |
| [Why Your Multiprocessing Pool Is Stuck (It’S Full Of Sharks!)](https://pythonspeed.com/articles/python-multiprocessing/) | Itamar Turner-Trauring |  |
| [The Parallelism Blues: When Faster Code Is Slower](https://pythonspeed.com/articles/parallelism-slower/) | Itamar Turner-Trauring |  |
| [The Hidden Performance Overhead Of Python C Extensions](https://pythonspeed.com/articles/python-extension-performance/) | Itamar Turner-Trauring |  |
| [Analysis Of A Python Performance Issue](https://vstinner.github.io/analysis-python-performance-issue.html) | Victor Stinner | Using the CPython benchmark suite |

## Tests

| To Read | Author | Notes |
|-|-|-|
| [Fast Tests For Slow Services: Why You Should Use Verified Fakes](https://pythonspeed.com/articles/verified-fakes/) | Itamar Turner-Trauring |  |
| [How To Use Your Project & Travis To Help Test Python Itself](https://snarky.ca/how-to-use-your-project-travis-to-help-test-python-itself/) | Brett Cannon | Also how to test your project against future Python releases |
| [Why You Should Document Your Tests](https://snarky.ca/how-to-use-your-project-travis-to-help-test-python-itself/) | Hynek Schlawack |  |

## Debugging

| To Read | Author | Notes |
|-|-|-|
| [When C Extensions Crash: Easier Debugging For Your Python Application](https://pythonspeed.com/articles/python-c-extension-crashes/) | Itamar Turner-Trauring |  |

## Zen of Python

| To Read | Author | Notes |
|-|-|-|
| [Zen Of Python, Again](https://lukasz.langa.pl/b6888f38-2e14-4595-a4fe-187fd0557a55/) | Łukasz Langa |  |

## Patterns

| To Read | Author | Notes |
|-|-|-|
| [Typeclasses In Python](https://sobolevn.me/2021/06/typeclasses-in-python) | Nikita Sobolev |  |
| [Typed Functional Dependency Injection In Python](https://sobolevn.me/2020/02/typed-functional-dependency-injection) | Nikita Sobolev |  |
| [When Python Exceptions Are Considered As Anti-Pattern](https://sobolevn.me/2019/02/python-exceptions-considered-an-antipattern) | Nikita Sobolev |  |
| [What’S A Pragmatic Approach To Subclassing In Python?](https://sobolevn.me/2019/02/python-exceptions-considered-an-antipattern) | Hynek Schlawack |  |

## Typing

| To Read | Author | Notes |
|-|-|-|
| [Simple Dependent Types In Python](https://sobolevn.me/2019/01/simple-dependent-types-in-python) | Nikita Sobolev |  |

## Packaging

| To Read | Author | Notes |
|-|-|-|
| [What The Heck Is Pyproject.Toml?](https://snarky.ca/what-the-heck-is-pyproject-toml/) | Brett Cannon |  |
| [Deconstructing Xkcd.Com/1987/](https://snarky.ca/deconstructing-xkcd-com-1987/) | Brett Cannon |  |
| [The Challenges In Designing A Library For Pep 425 (Aka Wheel Tags)/](https://snarky.ca/the-challenges-in-designing-a-library-for-pep-425/) | Brett Cannon |  |

## Concurrency And Parallelism

| To Read | Author | Notes |
|-|-|-|
| [Ways Of Waiting In Asyncio](https://hynek.me/articles/waiting-in-asyncio/) | Hynek Schlawack |  |
| [Designing An Async Api, From Sans-I/O On Up](https://snarky.ca/designing-an-async-api-from-sans-i-o-on-up/) | Brett Cannon |  |
| [The Returns Package For Async](https://sobolevn.me/2020/06/how-async-should-have-been) | Nikita Sobolev |  |
| [Dead Simple Connection Pooling With Twisted](https://hynek.me/articles/dead-simple-connection-pooling-with-twisted/) | Hynek Schlawack |  |

## Task Queues

| To Read | Author | Notes |
|-|-|-|
| [Stepping Stone Article For Redis And Celery](https://ljvmiranda921.github.io/notebook/2019/11/08/flask-redis-celery-mcdo/) | Lj Miranda |  |

## Supply Chain

| To Read | Author | Notes |
|-|-|-|
| [How Do You Verify That Pypi Can Be Trusted?](https://snarky.ca/how-do-you-verify-pypi-can-be-trusted/) | Brett Cannon |  |

## DevOps

| To Read | Author | Notes |
|-|-|-|
| [The History Behind The Decision To Move Python To Github](https://snarky.ca/the-history-behind-the-decision-to-move-python-to-github/) | Brett Cannon |  |
| [Python Deployment Anti-Patterns](https://hynek.me/articles/python-deployment-anti-patterns/) | Hynek Schlawack |  |

## The Road To Being A Core Dev

| To Read | Author | Notes |
|-|-|-|
| [My Road To The Python Commit Bit](https://hynek.me/articles/my-road-to-the-python-commit-bit/) | Hynek Schlawack |  |

## How Mega Corps Use Python

| To Read | Author | Notes |
|-|-|-|
| [Python At Netflix](https://netflixtechblog.com/python-at-netflix-bba45dae649e) | Pythonistas At Netflix |  |
| [Static Analysis At Scale: An Instagram Story](https://instagram-engineering.com/static-analysis-at-scale-an-instagram-story-8f498ab71a0ce) | Benjamin Woodruff |  |

## History And Decisions

| To Read | Author | Notes |
|-|-|-|
| [The Origins Of Pgen](https://python-history.blogspot.com/2018/05/the-origins-of-pgen.html) | Guido Van Rossum |  |
| [The History Of Bool, True And False](https://python-history.blogspot.com/2013/11/the-history-of-bool-true-and-false.html) | Guido Van Rossum |  |
| []() | Guido Van Rossum |  |
| [The Story Of None, True And False (And An Explanation Of Literals, Keywords And Builtins Thrown In)](https://python-history.blogspot.com/2013/11/story-of-none-true-false.html) | Guido Van Rossum |  |
| [Origin Of Metaclasses In Python](https://python-history.blogspot.com/2013/10/origin-of-metaclasses-in-python.html) | Guido Van Rossum |  |
| [Why Python Uses 0-Based Indexing](https://python-history.blogspot.com/2013/10/why-python-uses-0-based-indexing.html) | Guido Van Rossum |  |
| [Karin Dewar, Indentation And The Colon](https://python-history.blogspot.com/2011/07/karin-dewar-indentation-and-colon.html) | Guido Van Rossum |  |
| [Why Python'S Integer Division Floors](https://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html) | Guido Van Rossum |  |
| [From List Comprehensions To Generator Expressions](https://python-history.blogspot.com/2010/06/from-list-comprehensions-to-generator.html) | Guido Van Rossum |  |
| [Method Resolution Order](https://python-history.blogspot.com/2010/06/method-resolution-order.html) | Guido Van Rossum |  |
| [Import Antigravity](https://python-history.blogspot.com/2010/06/import-antigravity.html) | Guido Van Rossum |  |
| [The Inside Story On New-Style Classes](https://python-history.blogspot.com/2010/06/inside-story-on-new-style-classes.html) | Guido Van Rossum |  |
| [New-Style Classes](https://python-history.blogspot.com/2010/06/new-style-classes.html) | Guido Van Rossum |  |
| [Metaclasses And Extension Classes (A.K.A. “The Killer Joke”)](https://python-history.blogspot.com/2009/04/metaclasses-and-extension-classes-aka.html) | Guido Van Rossum |  |
| [And The Snake Attacks](https://python-history.blogspot.com/2009/04/and-snake-attacks.html) | Greg Ewing |  |
| [Origins Of Python'S "Functional" Features](https://python-history.blogspot.com/2009/04/origins-of-pythons-functional-features.html) | Guido Van Rossum |  |
| [The Great (Or Grand) Renaming](https://python-history.blogspot.com/2009/03/great-or-grand-renaming.html) | Guido Van Rossum |  |
| [Dynamically Loaded Modules](https://python-history.blogspot.com/2009/03/dynamically-loaded-modules.html) | Guido Van Rossum |  |
| [The Problem With Integer Division](https://python-history.blogspot.com/2009/03/problem-with-integer-division.html) | Guido Van Rossum |  |
| [How Exceptions Came To Be Classes](https://python-history.blogspot.com/2009/03/how-exceptions-came-to-be-classes.html) | Guido Van Rossum |  |
| [How Everything Became An Executable Statement](https://python-history.blogspot.com/2009/03/how-everything-became-executable.html) | Guido Van Rossum |  |
| [First-Class Everything](https://python-history.blogspot.com/2009/02/first-class-everything.html) | Guido Van Rossum |  |
| [Adding Support For User-Defined Classes](https://python-history.blogspot.com/2009/02/adding-support-for-user-defined-classes.html) | Guido Van Rossum |  |
| [Python'S Use Of Dynamic Typing](https://python-history.blogspot.com/2009/02/pythons-use-of-dynamic-typing.html) | Guido Van Rossum |  |
| [Early Language Design And Development](https://python-history.blogspot.com/2009/02/early-language-design-and-development.html) | Guido Van Rossum |  |
| [Microsoft Ships Python Code... In 1996](https://python-history.blogspot.com/2009/01/microsoft-ships-python-code-in-1996.html) | Greg Ewing |  |
| [Personal History - Part 2, Cnri And Beyond](https://python-history.blogspot.com/2009/01/personal-history-part-2-cnri-and-beyond.html) | Guido Van Rossum |  |
| [Personal History - Part 1, Cwi](https://python-history.blogspot.com/2009/01/personal-history-part-1-cwi.html) | Guido Van Rossum |  |
| [A Brief Timeline Of Python](https://python-history.blogspot.com/2009/01/brief-timeline-of-python.html) | Guido Van Rossum |  |
| [Python'S Design Philosophy](https://python-history.blogspot.com/2009/01/pythons-design-philosophy.html) | Guido Van Rossum |  |
