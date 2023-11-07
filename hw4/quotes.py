from flask import render_template
from flask.views import MethodView

import gbmodel

class Quotes(MethodView):
    """
    A class derived from MethodView to represent a presenter for the quotes.html view. 
    """

    def get(self):
        """
        Retrieves all quotes from database and returns them with the 
        render_template function.
        """
        model = gbmodel.get_model()
        tuple_list = model.select_quotes()
        quote_dict_list = [dict(quote=row[0], person=row[1], source=row[2], rating=row[3]) for row in tuple_list]

        return render_template('quotes.html', quotes=quote_dict_list)
