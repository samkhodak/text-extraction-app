from google.cloud import datastore
from .Model import Model

"""
Cloud datastore model for a quote library webapp.

NoSQL default Schema for the cloud datastore database:

+-------------------------+---------------------+--------+--------+
| Quote                   | Person              | Source | Rating |
+=========================+=====================+========+========+
| "To be or not to be..." | William Shakespeare | Hamlet | 9      |
+-------------------------+---------------------+--------+--------+

"""

def entity_to_list(entity):
    """
    Converts a datastore Entity to a list of its properties (each column in a row). 
    :return: List of quote properties (columns)
    """
    if (not entity):
        return None
    # If entity is a list (instead of single entity), pop the last entity off the list
    # and set it to be the entity we use.
    if isinstance(entity, list):
        entity = entity.pop()
    print(entity)
    return [ entity['person'], entity['source'], entity['rating'], entity['quote'] ]


class model(Model): 
    def __init__(self):
        """
        Initializes model class by designating what project to create/add datastore Kind to. 
        """
        self.client = datastore.Client('cloud-khodakovskiy-khod2')

    def select_quotes(self):
        """
        Selects all rows from datastore kind and returns an iterable list of lists.
        Each row contains data in the format of the schema above.
        :return: List of lists, with each list being a row from the datastore database.
        """
        query = self.client.query(kind = "Quote-entry")
        list_of_entities = list(map(entity_to_list, query.fetch()))
        # List of entities is a list of lists (arr of arrays).
        return list_of_entities

    def insert_quote(self, person, source, rating, quote):
        """
        Inserts quote into database, using Model's parameters. 
        :param person: String
        :param source: String 
        :param rating: int
        :param quote: String
        :return: True
        """
        # Creates datastore key for one entity
        key = self.client.key('Quote-entry')
        # creates an Entity (object) to insert into db
        quote_entity = datastore.Entity(key)
        quote_entity.update( {
            'person': person,
            'source': source,
            'rating': rating,
            'quote': quote,
        })
        self.client.put(quote_entity)
        return True
