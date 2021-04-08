<h1>Multi-line strings in programming typically are called `Heredocs`</h1>

NOTE: On the multi-line comments, we use the three quotes at the begining and on the end of the total comment.

When we need to add a few paragraphs on the content of a variable, function or comment, we must use the three quotes at the beggining and on the end of the total text content.<br>
If we use a single quote, the Python´s interpreter is going to throws an error.<br>
Let´s see an example!<br>

    paragraph = "Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

    Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

    Integer posuere erat a ante venenatis dapibus posuere velit aliquet"

    print(paragraph) The syntax is going to be an error! 


What ocurred is, the parser come to this first paragraph line and it expected to find the end of the string at the end of this first line.<br>
So it expected to find a end of quote!<br>
But insted, it just found a new line, so that´s the reason why the parse thow an error.<br>
To correct that, we need to built a different syntax using three quotes at the beggining and on the end of the total text content.<br>

Let´s see the paragraph construction!

        content_02 = """
        TITLE 02
        Content 02 start here. Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

        Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

        Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
        """

        print(content_02)
  
Print

        TITLE 02
        Content 02 start here. Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

        Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

        Integer posuere erat a ante venenatis dapibus posuere velit aliquet.



