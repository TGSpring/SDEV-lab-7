"""Tyler Spring
Lab 7
This is the second part of the website project, lab 6.
Here the user is prompted to entry a user name and password in the correct format.
Once that is validated the user is granted access to 6 other pages of the website.
This includes a page with images, a table, and a registration form the user can
fill with an email and password, again having it validated."""
from datetime import date

import flask

app = flask.Flask(__name__)


@app.route('/')
@app.route('/logger.html')
def logger():
    """
Logger function. First page that prompts the user and does not let them to the other
functions until this is completed.
    :rtype: object
    """
    if 'visited' not in flask.session:
        return flask.render_template('logger.html', the_title='logger')


@app.route('/page1.html')
def page1():
    """
Page 1 function. Is available after the logger is validated.
Provides links to other pages using the render
template function of the flask class.
    :rtype: object
    """
    return flask.render_template('page1.html', the_title='Page 1')


@app.route('/page2.html')
def page2():
    """
Page 2 function. Is available after the logger is validated.
Provides links to other pages using the render
template function of the flask class.
:return:
    """
    return flask.render_template('page2.html', the_title='Page 2')


@app.route('/page3.html')
def page3():
    """
Page 3 function. Is available after the logger is validated.
Provides links to other pages using the render
template function of the flask class.
    :rtype: object
    """
    return flask.render_template('page3.html', the_title='Page 3')


@app.route('/page4.html')
def page4():
    """
Page 4 function. Is available after the logger is validated.
Provides links to other pages using the render
template function of the flask class.
    :rtype: object
    """
    return flask.render_template('page4.html', date=date.today())


@app.route('/page5.html')
def page5():
    """
Page 5 function. Is available after the logger is validated.
Provides links to other pages using the render
template function of the flask class.
    :rtype: object
    """
    return flask.render_template('page5.html', date=date.today())


@app.route('/page6.html')
def page6():
    """
Page 6 function. Is available after the logger is validated.
Provides links to other pages using the render
template function of the flask class.
    :rtype: object
    """
    return flask.render_template('page6.html', date=date.today())


if __name__ == "__main__":
    app.run(debug=True)
