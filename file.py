'''


## Encoding


| To Read | Author | Notes |
|-|-|-|
| [Unicode Book](https://unicodebook.readthedocs.io/) | Victor Stinner | Also discusses Python handling |

## CPython Internals


| To Read | Author | Notes |
|-|-|-|
| [Your Guide to the CPython Source Code](https://realpython.com/cpython-source-code-guide/) | Anthony Shaw |  |

## How Mega Corps Use Python


| To Read | Author | Notes |
|-|-|-|
| [NetFlix](https://netflixtechblog.com/python-at-netflix-bba45dae649e) | Pythonistas at Netflix |  |
| [Static Analysis at Scale: An Instagram Story](https://instagram-engineering.com/static-analysis-at-scale-an-instagram-story-8f498ab71a0c) | Benjamin Woodruff |  |


'''


data = {
    'Encoding':
    [
        [
            "Unicode Book",
            'https://unicodebook.readthedocs.io/',
            'Victor Stinner',
            'Also discusses Python handling'
        ]
    ],
    'Maths':
    [
        [
            "Math Symbols Explained with Python",
            'https://amitness.com/2019/08/math-for-programmers/',
            'Amit Chaudhary',
            ''
        ],
        [
            "Foundations of Applied Mathematics",
            'https://foundations-of-applied-mathematics.github.io/',
            'Profs and Students at different universities',
            (
                'A series of four textbooks developed for Brigham Young University’s Applied and Computational Mathematics degree program for beginning graduate and advanced undergraduate students. '
                'Uses Python for concepts'
            )
        ]
    ],
    'Compiler Theory':
    [
        [
            "Building Finite State Machines with Python Coroutines",
            'https://arpitbhayani.me/blogs/fsm',
            'Arpit Bhayani',
            ''
        ],
        [
            "Writing a Python to C compiler in Python",
            'https://notes.eatonphil.com/writing-a-simple-python-compiler.html',
            'Phil Eaton',
            ''
        ],
        [
            "Writing a Jinja-inspired template library in Python",
            'https://notes.eatonphil.com/writing-a-template-library-in-python.html',
            'Phil Eaton',
            ''
        ],
        [
            "Writing a simple JSON parser",
            'https://notes.eatonphil.com/writing-a-simple-json-parser.html',
            'Phil Eaton',
            ''
        ],
    ],
    'CPython Internals':
    [
        
        [
            "Your Guide to the CPython Source Code",
            'https://realpython.com/cpython-source-code-guide/',
            'Anthony Shaw',
            ''
        ],
        [
            "Internals of CPython 3.6",
            'https://intopythoncom.files.wordpress.com/2017/04/internalsofcpython3-6-1.pdf',
            'Prashanth Raghu',
            ''
        ],
        [
            "Advanced Internals of CPython 3.6",
            'https://intopythoncom.files.wordpress.com/2017/04/merged.pdf',
            'Prashanth Raghu',
            ''
        ],
        [
            "Python Development Documentation",
            'https://pythondev.readthedocs.io/',
            'Victor Stinner',
            ''
        ],
        [
            "Lifecycle of a Python Code - CPython’s Execution Model",
            'https://dev.to/btaskaya/lifecycle-of-a-python-code---cpythons-execution-model-85i',
            'Batuhan Osman Taşkaya',
            ''
        ],
        [
            "A Python Interpreter Written in Pythonn",
            'http://aosabook.org/en/500L/a-python-interpreter-written-in-python.html',
            'Allison Kaptur',
            'Introduction to Python bytecode'
        ],
        [
            "Notes About A Web Assembly Backend",
            'https://snarky.ca/what-is-the-core-of-the-python-programming-language/',
            'Brett Cannon',
            ''
        ],
        [
            "Summary of Sam Gross' NoGIL proposal",
            'https://lukasz.langa.pl/5d044f91-49c1-4170-aed1-62b6763e6ad0/',
            'Łukasz Langa',
            ''
        ],
        [
            "Python C API: Add functions to access PyObject",
            'https://vstinner.github.io/c-api-abstract-pyobject.html',
            'Victor Stinner',
            ''
        ],
        [
            "C API changes between Python 3.5 to 3.10",
            'https://vstinner.github.io/c-api-python3_10-changes.html',
            'Victor Stinner',
            ''
        ],
        [
            "Creation of the pythoncapi_compat project",
            'https://vstinner.github.io/pythoncapi_compat.html',
            'Victor Stinner',
            ''
        ],
        [
            "Make structures opaque in the Python C API",
            'https://vstinner.github.io/c-api-opaque-structures.html',
            'Victor Stinner',
            ''
        ],
        [
            "Isolate Python Subinterpreters",
            'https://vstinner.github.io/hide-implementation-details-python-c-api.html',
            'Victor Stinner',
            ''
        ],
        [
            "Hide implementation details from the Python C API",
            'https://vstinner.github.io/isolate-subinterpreters.html',
            'Victor Stinner',
            ''
        ],
        [
            "Leaks discovered by subinterpreters",
            'https://vstinner.github.io/subinterpreter-leaks.html',
            'Victor Stinner',
            ''
        ],
        [
            "GIL bugfixes for daemon threads in Python 3.9",
            'https://vstinner.github.io/gil-bugfixes-daemon-threads-python39.html',
            'Victor Stinner',
            ''
        ],
        [
            "Threading shutdown race condition",
            'https://vstinner.github.io/threading-shutdown-race-condition.html',
            'Victor Stinner',
            ''
        ],
        [
            "Threading shutdown race condition",
            'https://vstinner.github.io/threading-shutdown-race-condition.html',
            'Victor Stinner',
            ''
        ],
        [
            "Pass the Python thread state explicitly",
            'https://vstinner.github.io/index2.html',
            'Victor Stinner',
            ''
        ],
        [
            "asyncio WSASend() memory leak",
            'https://vstinner.github.io/asyncio-proactor-wsasend-memory-leak.html',
            'Victor Stinner',
            ''
        ],
        [
            "asyncio: WSARecv() cancellation causing data loss",
            'https://vstinner.github.io/asyncio-proactor-wsarecv-cancellation-data-loss.html',
            'Victor Stinner',
            ''
        ],
        [
            "Asyncio: Proactor ConnectPipe() Race Condition",
            'https://vstinner.github.io/asyncio-proactor-connect-pipe-race-condition.html',
            'Victor Stinner',
            ''
        ],
        [
            "Asyncio: Proactor Cancellation From Hell",
            'https://vstinner.github.io/asyncio-proactor-cancellation-from-hell.html',
            'Victor Stinner',
            ''
        ],
        [
            "How I fixed a very old GIL race condition in Python 3.7",
            'https://vstinner.github.io/python37-gil-change.html',
            'Victor Stinner',
            ''
        ],
        [
            "History of the Python private C API _PyTime",
            'https://vstinner.github.io/pytime.html',
            'Victor Stinner',
            ''
        ],
    ],
    'Insider Bits':
    [
        [
            "Constant Folding in Python",
            'https://arpitbhayani.me/blogs/constant-folding-python',
            'Arpit Bhayani',
            ''
        ],
        [
            "Integer Caching in Python",
            'https://arpitbhayani.me/blogs/python-caches-integers',
            'Arpit Bhayani',
            ''
        ],
        [
            "Super Long Integers in Python",
            'https://arpitbhayani.me/blogs/super-long-integers',
            'Arpit Bhayani',
            ''
        ],
        [
            "Unravelling decorators",
            'https://snarky.ca/unravelling-decorators/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling data structure displays",
            'https://snarky.ca/unravelling-data-structure-displays/',
            'Brett Cannon',
            ''
        ],
        [
            "(Not) unravelling generator expressions",
            'https://snarky.ca/not-unravelling-generator-expressions/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling the `async with` statement",
            'https://snarky.ca/unravelling-the-async-with-statement/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling `async for` loops",
            'https://snarky.ca/unravelling-async-for-loops/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling `async` and `await`",
            'https://snarky.ca/unravelling-async-and-await/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling the `with` statement",
            'https://snarky.ca/unravelling-the-with-statement/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling the `pass` statement",
            'https://snarky.ca/unravelling-the-pass-statement/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling `for` statements",
            'https://snarky.ca/unravelling-for-statements/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling assertions",
            'https://snarky.ca/unravelling-assertions/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling the import statement",
            'https://snarky.ca/unravelling-the-import-statement/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling boolean operations",
            'https://snarky.ca/unravelling-boolean-operations/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling membership testing",
            'https://snarky.ca/unravelling-membership-testing/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling `not` in Python",
            'https://snarky.ca/unravelling-not-in-python/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling `is` and `is not`",
            'https://snarky.ca/unravelling-is-and-is-not/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling rich comparison operators",
            'https://snarky.ca/unravelling-rich-comparison-operators/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling unary arithmetic operators",
            'https://snarky.ca/unravelling-unary-arithmetic-operators/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling augmented arithmetic assignment",
            'https://snarky.ca/unravelling-augmented-arithmetic-assignment/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling binary arithmetic operations in Python",
            'https://snarky.ca/unravelling-binary-arithmetic-operations-in-python/',
            'Brett Cannon',
            ''
        ],
        [
            "Unravelling attribute access in Python",
            'https://snarky.ca/unravelling-attribute-access-in-python/',
            'Brett Cannon',
            ''
        ],
        [
            "How the heck does async/await work in Python 3.5?",
            'https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/',
            'Brett Cannon',
            ''
        ],
    ],
    'Sane Bits':
    [
        [
            "An approach to lazy importing in Python 3.7",
            'https://snarky.ca/lazy-importing-in-python-3-7/',
            'Brett Cannon',
            ''
        ],
        [
            "Customizing class creation in Python",
            'https://snarky.ca/customizing-class-creation-in-python/',
            'Brett Cannon',
            ''
        ],
        [
            "Why pathlib.Path doesn't inherit from str in Python",
            'https://snarky.ca/why-pathlib-path-doesn-t-inherit-from-str/',
            'Brett Cannon',
            ''
        ],
        [
            "Why Python3?",
            'https://snarky.ca/how-to-pitch-python-3-to-management/',
            'Brett Cannon',
            ''
        ],
        [
            "Why `print` became a function in Python 3",
            'https://snarky.ca/why-print-became-a-function-in-python-3/',
            'Brett Cannon',
            ''
        ],
        [
            "If I were designing Python's import from scratch",
            'https://snarky.ca/if-i-were-designing-imort-from-scratch/',
            'Brett Cannon',
            ''
        ],
        [
            "Try to not use the Python C API directly",
            'https://snarky.ca/try-to-not-use-the-c-api-directly/',
            'Brett Cannon',
            ''
        ],
        [
            "Lambdas as a solution for puzzles",
            'https://blog.astrosnail.pt.eu.org/2021-02-11-snake.html',
            '',
            ''
        ],
    ],
    'Performance':
    [
        [
            "Python performance: it’s not just the interpreter",
            'https://blog.kevmod.com/2020/05/python-performance-its-not-just-the-interpreter/',
            'Kevin Modzelewski',
            'Worked on the Pyston project'
        ],
        [
            "Accelerate Numpy using Tensorflow",
            'https://blog.kevmod.com/2017/06/update-on-numpy-acceleration/',
            'Kevin Modzelewski',
            ''
        ],
        [
            "Clinging to memory: how Python function calls can increase memory use",
            'https://pythonspeed.com/articles/function-calls-prevent-garbage-collection/',
            'Itamar Turner-Trauring',
            ''
        ],
        [
            "Where’s your bottleneck? CPU time vs wallclock time",
            'https://pythonspeed.com/articles/blocking-cpu-or-io/',
            'Itamar Turner-Trauring',
            ''
        ],
        [
            "Beyond cProfile: Choosing the right tool for performance optimization",
            'https://pythonspeed.com/articles/beyond-cprofile/',
            'Itamar Turner-Trauring',
            ''
        ],
        [
            "Not just CPU: writing custom profilers for Python",
            'https://pythonspeed.com/articles/custom-python-profiler/',
            'Itamar Turner-Trauring',
            ''
        ],
        [
            "CI for performance: Reliable benchmarking in noisy environments",
            'https://pythonspeed.com/articles/consistent-benchmarking-in-ci/',
            'Itamar Turner-Trauring',
            ''
        ],
        [
            "Why your multiprocessing Pool is stuck (it’s full of sharks!)",
            'https://pythonspeed.com/articles/python-multiprocessing/',
            'Itamar Turner-Trauring',
            ''
        ],
        [
            "The Parallelism Blues: when faster code is slower",
            'https://pythonspeed.com/articles/parallelism-slower/',
            'Itamar Turner-Trauring',
            ''
        ],
        [
            "The hidden performance overhead of Python C extensions",
            'https://pythonspeed.com/articles/python-extension-performance/',
            'Itamar Turner-Trauring',
            ''
        ],
        [
            "Analysis of a Python performance issue",
            'https://vstinner.github.io/analysis-python-performance-issue.html',
            'Victor Stinner',
            'Using the CPython benchmark suite'
        ],
    ],
    'Tests':
    [
        [
            "Fast tests for slow services: why you should use verified fakes",
            'https://pythonspeed.com/articles/verified-fakes/',
            'Itamar Turner-Trauring',
            ''
        ],
        [
            "How to use your project & Travis to help test Python itself",
            'https://snarky.ca/how-to-use-your-project-travis-to-help-test-python-itself/',
            'Brett Cannon',
            'Also how to test your project against future Python releases'
        ],
        [
            "Why You Should Document Your Tests",
            'https://snarky.ca/how-to-use-your-project-travis-to-help-test-python-itself/',
            'Hynek Schlawack',
            ''
        ],
    ],
    'Debugging':
    [
        [
            "When C extensions crash: easier debugging for your Python application",
            'https://pythonspeed.com/articles/python-c-extension-crashes/',
            'Itamar Turner-Trauring',
            ''
        ],
    ],
    'Zen of Python':
    [
        [
            "Zen of Python, Again",
            'https://lukasz.langa.pl/b6888f38-2e14-4595-a4fe-187fd0557a55/',
            'Łukasz Langa',
            ''
        ],
    ],
    'Patterns':
    [
        [
            "Typeclasses in Python",
            'https://sobolevn.me/2021/06/typeclasses-in-python',
            'Nikita Sobolev',
            ''
        ],
        [
            "Typed functional Dependency Injection in Python",
            'https://sobolevn.me/2020/02/typed-functional-dependency-injection',
            'Nikita Sobolev',
            ''
        ],
        [
            "When Python exceptions are considered as anti-pattern",
            'https://sobolevn.me/2019/02/python-exceptions-considered-an-antipattern',
            'Nikita Sobolev',
            ''
        ],
        [
            "What’s a pragmatic approach to subclassing in Python?",
            'https://sobolevn.me/2019/02/python-exceptions-considered-an-antipattern',
            'Hynek Schlawack',
            ''
        ],
    ],
    'Typing':
    [
        [
            "Simple dependent types in Python",
            'https://sobolevn.me/2019/01/simple-dependent-types-in-python',
            'Nikita Sobolev',
            ''
        ],
    ],
    'Packaging':
    [
        [
            "What the heck is pyproject.toml?",
            'https://snarky.ca/what-the-heck-is-pyproject-toml/',
            'Brett Cannon',
            ''
        ],
        [
            "Deconstructing xkcd.com/1987/",
            'https://snarky.ca/deconstructing-xkcd-com-1987/',
            'Brett Cannon',
            ''
        ],
        [
            "The challenges in designing a library for PEP 425 (aka wheel tags)/",
            'https://snarky.ca/the-challenges-in-designing-a-library-for-pep-425/',
            'Brett Cannon',
            ''
        ],
    ],
    'Concurrency And Parallelism':
    [
        [
            "Ways of waiting in asyncio",
            'https://hynek.me/articles/waiting-in-asyncio/',
            'Hynek Schlawack',
            ''
        ],
        [
            "Designing an async API, from sans-I/O on up",
            'https://snarky.ca/designing-an-async-api-from-sans-i-o-on-up/',
            'Brett Cannon',
            ''
        ],
        [
            "The Returns Package For Async",
            'https://sobolevn.me/2020/06/how-async-should-have-been',
            'Nikita Sobolev',
            ''
        ],
        [
            "Dead Simple Connection Pooling with Twisted",
            'https://hynek.me/articles/dead-simple-connection-pooling-with-twisted/',
            'Hynek Schlawack',
            ''
        ],
    ],
    'Task Queues':
    [
        [
            "Stepping Stone Article For Redis And Celery",
            'https://ljvmiranda921.github.io/notebook/2019/11/08/flask-redis-celery-mcdo/',
            'Lj Miranda',
            ''
        ]
    ],
    'Supply Chain':
    [
        [
            "How do you verify that PyPI can be trusted?",
            'https://snarky.ca/how-do-you-verify-pypi-can-be-trusted/',
            'Brett Cannon',
            ''
        ],
    ],
    'DevOps':
    [
        [
            "The history behind the decision to move Python to GitHub",
            'https://snarky.ca/the-history-behind-the-decision-to-move-python-to-github/',
            'Brett Cannon',
            ''
        ],
        [
            "Python Deployment Anti-Patterns",
            'https://hynek.me/articles/python-deployment-anti-patterns/',
            'Hynek Schlawack',
            ''
        ],
    ],
    'The Road To Being A Core Dev':
    [
        [
            "My Road to the Python Commit Bit",
            'https://hynek.me/articles/my-road-to-the-python-commit-bit/',
            'Hynek Schlawack',
            ''
        ],
    ],
    'How Mega Corps Use Python':
    [
        [
            "Python At Netflix",
            'https://netflixtechblog.com/python-at-netflix-bba45dae649e',
            'Pythonistas at Netflix',
            '',
        ],
        [
            "Static Analysis at Scale: An Instagram Story",
            'https://instagram-engineering.com/static-analysis-at-scale-an-instagram-story-8f498ab71a0ce',
            'Benjamin Woodruff',
            '',
        ]
    ],
    'History And Decisions':
    [  
        [
            "The origins of pgen",
            'https://python-history.blogspot.com/2018/05/the-origins-of-pgen.html',
            'Guido van Rossum',
            '',
        ],
        [
            "The history of bool, True and False",
            'https://python-history.blogspot.com/2013/11/the-history-of-bool-true-and-false.html',
            'Guido van Rossum',
            '',
        ],
        [
            "",
            '',
            'Guido van Rossum',
            '',
        ],
        [
            "The story of None, True and False (and an explanation of literals, keywords and builtins thrown in)",
            'https://python-history.blogspot.com/2013/11/story-of-none-true-false.html',
            'Guido van Rossum',
            '',
        ],
        [
            "Origin of metaclasses in Python",
            'https://python-history.blogspot.com/2013/10/origin-of-metaclasses-in-python.html',
            'Guido van Rossum',
            '',
        ],
        [
            "Why Python uses 0-based indexing",
            'https://python-history.blogspot.com/2013/10/why-python-uses-0-based-indexing.html',
            'Guido van Rossum',
            '',
        ],
        [
            "Karin Dewar, Indentation and the Colon",
            'https://python-history.blogspot.com/2011/07/karin-dewar-indentation-and-colon.html',
            'Guido van Rossum',
            '',
        ],
        [
            "Why Python's Integer Division Floors",
            'https://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html',
            'Guido van Rossum',
            '',
        ],
        [
            "From List Comprehensions to Generator Expressions",
            'https://python-history.blogspot.com/2010/06/from-list-comprehensions-to-generator.html',
            'Guido van Rossum',
            '',
        ],
        [
            "Method Resolution Order",
            'https://python-history.blogspot.com/2010/06/method-resolution-order.html',
            'Guido van Rossum',
            '',
        ],
        [
            "import antigravity",
            'https://python-history.blogspot.com/2010/06/import-antigravity.html',
            'Guido van Rossum',
            '',
        ],
        [
            "The Inside Story on New-Style Classes",
            'https://python-history.blogspot.com/2010/06/inside-story-on-new-style-classes.html',
            'Guido van Rossum',
            '',
        ],
        [
            "New-style Classes",
            'https://python-history.blogspot.com/2010/06/new-style-classes.html',
            'Guido van Rossum',
            '',
        ],
        [
            '''Metaclasses and Extension Classes (a.k.a. “The Killer Joke”)''',
            'https://python-history.blogspot.com/2009/04/metaclasses-and-extension-classes-aka.html',
            'Guido van Rossum',
            '',
        ],
        [
            "And the Snake Attacks",
            'https://python-history.blogspot.com/2009/04/and-snake-attacks.html',
            'Greg Erwin',
            '',
        ],
        [
            '''Origins of Python's "Functional" Features''',
            'https://python-history.blogspot.com/2009/04/origins-of-pythons-functional-features.html',
            'Guido van Rossum',
            '',
        ],
        [
            "The Great (or Grand) Renaming",
            'https://python-history.blogspot.com/2009/03/great-or-grand-renaming.html',
            'Guido van Rossum',
            '',
        ],
        [
            "Dynamically Loaded Modules",
            'https://python-history.blogspot.com/2009/03/dynamically-loaded-modules.html',
            'Guido van Rossum',
            '',
        ],
        [
            "The Problem with Integer Division",
            'https://python-history.blogspot.com/2009/03/problem-with-integer-division.html',
            'Guido van Rossum',
            '',
        ],
        [
            "How Exceptions Came to be Classes",
            'https://python-history.blogspot.com/2009/03/how-exceptions-came-to-be-classes.html',
            'Guido van Rossum',
            '',
        ],
        [
            "How Everything Became an Executable Statement",
            'https://python-history.blogspot.com/2009/03/how-everything-became-executable.html',
            'Guido van Rossum',
            '',
        ],
        [
            "First-class Everything",
            'https://python-history.blogspot.com/2009/02/first-class-everything.html',
            'Guido van Rossum',
            '',
        ],
        [
            "Adding Support for User-defined Classes",
            'https://python-history.blogspot.com/2009/02/adding-support-for-user-defined-classes.html',
            'Guido van Rossum',
            '',
        ], 
        [
            "Python's Use of Dynamic Typing",
            'https://python-history.blogspot.com/2009/02/pythons-use-of-dynamic-typing.html',
            'Guido van Rossum',
            '',
        ],
        [
            "Early Language Design and Development",
            'https://python-history.blogspot.com/2009/02/early-language-design-and-development.html',
            'Guido van Rossum',
            '',
        ],
        [
            "Microsoft Ships Python Code... in 1996",
            'https://python-history.blogspot.com/2009/01/microsoft-ships-python-code-in-1996.html',
            'Greg Erwin',
            '',
        ],
        [
            "Personal History - part 2, CNRI and beyond",
            'https://python-history.blogspot.com/2009/01/personal-history-part-2-cnri-and-beyond.html',
            'Guido van Rossum',
            '',
        ],
        [
            "Personal History - part 1, CWI",
            'https://python-history.blogspot.com/2009/01/personal-history-part-1-cwi.html',
            'Guido van Rossum',
            '',
        ],
        [
            "A Brief Timeline of Python",
            'https://python-history.blogspot.com/2009/01/brief-timeline-of-python.html',
            'Guido van Rossum',
            '',
        ],
        [
            "Python's Design Philosophy",
            'https://python-history.blogspot.com/2009/01/pythons-design-philosophy.html',
            'Guido van Rossum',
            '',
        ],
    ],
}

print('''

This page lists the very best Python engineering articles of the internet, hand-picked to give hours and hours 
of pure reading joy.
It is especially designed for onboarding new members on your Python team. Great for skilling up.
Though not necessarily read one after the other, the order is nevertheless not random. 
For example, knowledge of CPython internals specially bytecodes are necessary to make sense of B. Cannon's 
unravelling series. 
The articles are focused on core Python and it's as advanced as articles can get.
''')
for topic in data:
    print(f'\n## {topic}')
    print('')
    print('| To Read | Author | Notes |\n'
            '|-|-|-|')
    for i, article in enumerate(data[topic]):
        assert len(data[topic][i]) == 4, f'{data[topic]} - {i} not equal to 4'
        title = data[topic][i][0].title()
        link = data[topic][i][1].title()
        author = data[topic][i][2].title()
        notes = data[topic][i][3]
        print(f'| [{title}]({link}) | {author} | {notes} |')
