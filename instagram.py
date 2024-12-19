import re

# Initialize an empty set to store the usernames
my_followers = set()
people_i_follow = set()

# Define the regex pattern to find usernames
pattern = r'href="/([^/]+)/"'
# used to find parts of the text that have usernames ex:
# href="/taylorswift/"
# href="/simonebiles/"

# Open the file with your followers and read its contents
with open("follower-html.txt", "r") as file:
    followers_content = file.read()

# Find all matches and add them to the set of followers 
matches = re.findall(pattern, followers_content)
my_followers.update(matches)


# Open the file with your following and read its contents
with open("following-html.txt", "r") as file:
    following_content = file.read()

# Find all matches and add them to the set of people you follow 
matches = re.findall(pattern, following_content)
people_i_follow.update(matches)


# Print the result
print("Followers:", my_followers)
print("Following:", people_i_follow)

# Now we want to know who isn't following us back!
# If we take the usernames of people we're following, and
# subtract the usernames of people who follow us back,
# we'll be left with only the people who don't follow us back
not_following_back = people_i_follow - my_followers

# Print the results
print("These people are not following me back:")
print(not_following_back)