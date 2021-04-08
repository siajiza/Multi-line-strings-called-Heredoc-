# # Heredoc
# paragraph = "Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

# Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

# Integer posuere erat a ante venenatis dapibus posuere velit aliquet"

# print(paragraph) The syntax is going to be an error! 


# Heredoc 01

content_01 = """
TITLE 01
Content 01 start here. Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet
""".strip()

# Heredoc 02

content_02 = """
TITLE 02
Content 02 start here. Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
"""

print(content_01) #strip() function pulling out any excess newline characters inside of a multi-line string. 

print(content_02) #without strip() function we can see one line empty space and then the item of terminal´s python

