# Audio Studio Code


A custom built IDE designed designed to translate natural language to code using speech recognition, context free grammars, and recursive decent parsing all stored on a realtime database.

Uses Firebase Realtime Database and Google Speech Recognition API

**Roles:**
<ul>
Ethan Young & Henry Schneider
  <ul>
  <li>Implemented speech recognition machine learning library</li>
  <li>Pre-formatted strings to put in proper format for the phrase parser</li>
  </ul>
Rahul Medicharla
<ul>
<li>Developed Custom IDE from scratch that was capable of running python</li>
<li>Integrated subcomponents with Google Cloud Firebase to pass data between components</li>
</ul>
Jack Italiano
<ul>
<li>Developed Interpreter from pre-formatted strings to recursive object representations for easy access to the code.</li>
<li>Developed Interpreter from objects to python syntax using recursive decent parsing.</li>
</ul>
</ul>

# Mission
**Goal** 
<ul>
We wanted to create a platform for voice to code that is actually useful and efficient for developers. Voice to text applications already exist, but their usefullness is questionable at best, and a gimmick at worst. We are building something in between the fun gimmicks of saying "create a ball that bounces" that will create the code for a functioning bouncing ball on the screen, and the frustratingly explicit "for int i equals 0, i less than 10, i++" to create a for loop.
</ul>

**Target**
<ul>
Our target customer is a real developer that wants to focus on the high-level design of their code rather than the low-level syntax.
</ul>

**Requirements**
<ul>
<li>talking should feel conversational</li>
<li>you should be able to be very specific and get specific results, or very general and get general results</li>
<li>the IDE should always know what you're talking about (know the scope of everything)</li>
<li>you should be able to acces your code from any laptop/desktop/mobile device</li>
</ul>

**Next steps:**
<ul>
<li>Create dataset for speech to psuedo code AI training</li>
<li>Create a more robust interpreter</li>
<li>Improve speech recognition</li>
<li>Improve IDE functionality and UI/UX</li>
<li>Add support for mobile devices</li>
<li>Add support for user accounts</li>
</ul>

# How It Works

**Overview**
<ul>
The first step is to get speech to text data and clean the data into a standardized format. Then, this cleaned data is passed to an interpreteter that creates python objects based on the data received. These objects are stored and accessible in two ways: by line for easy navigation, and by a recursive tree structure for easy manipulation. Next, these objects are parsed into python syntax and sent to the IDE to be printed.
</ul>

**Data Pipeline**
<ol>
<li>put your more in depth description here</li>
</ol>

# Processes
**Speech Recognition**
<ol>
<li>put your more in depth description here</li>
</ol>

**Database**
<ol>
<li>put your more in depth description here</li>
</ol>

**Text to Code**
<ol>
<li>Tokenize text in the input field of database</li>
<li>Parse tokens into python objects that store all data related to the feature</li>
    <ul>
    <li>store names, values, parent, children, scope, etc.</li>
    </ul>
<li>Interpret python objects into proper python syntax</li>
    <ul>
    <li>Recursive decent parsing to parse objects to line by line code with all proper formatting, indentation, etc.</li>
    </ul>
<li>Send map of key value pairs (line_number: formatted_text) to the output field of the databse</li>
</ol>

**Custom IDE**
<ol>
<li>put your more in depth description here</li>
</ol>













