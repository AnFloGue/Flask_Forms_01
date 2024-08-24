from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
# Configure a secret key for the Flask application.
app.config['SECRET_KEY'] = 'mysecretkey'


# Define a WTForm class for collecting the information.

class my_InfoForm(FlaskForm):
    """
    This class represents a form to collect information about with
     use of WTForms fields.
    """
    breed = StringField('What breed are you?')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    '''Initialize the breed variable to False to be used
    in the HTML template to conditionally display content.
'''
    breed = False
    # Create an instance of the InfoForm.
    form = my_InfoForm()
    # Check if the form is valid upon submission.
    if form.validate_on_submit():
        # Retrieve the data from the form.
        breed = form.breed.data
        # Reset the breed data in the form to an empty string.
        form.breed.data = ''
    return render_template('00-home.html', form=form, breed=breed)


if __name__ == '__main__':
    app.run(debug=True)