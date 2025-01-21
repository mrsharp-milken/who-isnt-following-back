# who-isnt-following-back

A simple program to figure out who isn't following you back on instagram

<img width="1244" alt="image" src="https://github.com/user-attachments/assets/c27f6f78-8ee4-42e1-a40d-fafc44ebdd14" />

## Instructions for use

Note: These instructions are designed to help you along, but _they do not try to hold your hand through every step_. You will probably need to try multiple times, reread to check your interpretation, and review the visual aids over and over again.

1. Download and unzip the project files. Click on the green "<> Code" button, then choose "Download ZIP." After the download completes, open Finder, find the downloaded .zip file in your downloads, and open it. This should create a folder called `who-isnt-following-back-main`. Open the folder and make sure you can see all the files, most importantly: `follower-html.txt`, `following-html.txt`, and `instagram.py`.

2. Now we'll get the list of your instagram following. [Go to instagram.com using google chrome on a computer, sign in, and go to your profile](https://github.com/mrsharp-milken/who-isnt-following-back/blob/main/get-to-following-1.png). Click on the part of your profile that shows how many accounts you are following.

3. Now that you have the window of the accounts you are following open, [scroll all the way to the bottom to load the list all of your following](https://github.com/mrsharp-milken/who-isnt-following-back/blob/main/get-to-following-2.png). This may take a little while.

4. Once the whole list is loaded, [right click (or two-finger click) one of the accounts, then choose Inspect](https://github.com/mrsharp-milken/who-isnt-following-back/blob/main/get-to-following-3.png). This will open the source code for the webpage.

5. This source code is called HTML. As your mouse hovers over the HTML, the corresponding part of the webpage gets highlighted. [Scroll up in the HTML until you find the `<div` that highlights the list of accounts, but nothing else. Right click this `<div` then choose "Edit as HTML".](https://github.com/mrsharp-milken/who-isnt-following-back/blob/main/get-to-following-4.gif) Select all of the HTML in the text box, and copy it.

6. The HTML you just copied contains the usernames of all the accounts that you follow! However, there's a bunch of other junk in there, so we'll use code to search through it. [Paste the HTML into the `following-html.txt` file so we can search it with Python](https://github.com/mrsharp-milken/who-isnt-following-back/blob/main/get-to-following-5.gif).

7. Repeat steps 2-6 for the list of accounts that follow you, aka your "followers". Paste the HTML for your followers into the `follower-html.txt` file.

8. It's time to use Python to search through the HTML! Open the `instagram.py` file with Thonny. Read through the file, it's not very long! In short:
    - We look at each of the files with HTML, and search for a special pattern in the HTML that will contain usernames.
    - This gives us the list of people who we follow and the list of people that follow us.
    - Then, we "subtract" all the people who follow us from the list of people we follow, and we're left with a list of people who don't follow us back.

9. Run the program and check your output to see who doesn't follow you back! It's possible that you get an error, but that's OK! Read through the error, to see if you can understand it, try repeating the steps again, and ask ChatGPT for help too.
