from enum import Enum

from dataclasses import dataclass, asdict
import pandas as pd


class CustomerFields(Enum):
    customer_id = 'customer_id'
    created_at = 'created_at'
    updated_at = 'updated_at'
    email_address = 'email_address'
    phone_number = 'phone_number'
    name = 'name'
    first_name = 'first_name'
    last_name = 'last_name'
    customer_address_first_line = 'customer_address_first_line'
    customer_address_second_line = 'customer_address_second_line'
    customer_address_city = 'customer_address_city'
    customer_address_state = 'customer_address_state'
    customer_address_country = 'customer_address_country'
    customer_address_zip_code = 'customer_address_zip_code'
    shipping_address_first_line = 'shipping_address_first_line'
    shipping_address_second_line = 'shipping_address_second_line'
    shipping_address_city = 'shipping_address_city'
    shipping_address_state = 'shipping_address_state'
    shipping_address_country = 'shipping_address_country'
    shipping_address_zip_code = 'shipping_address_zip_code'
    billing_address_first_line = 'billing_address_first_line'
    billing_address_second_line = 'billing_address_second_line'
    billing_address_city = 'billing_address_city'
    billing_address_state = 'billing_address_state'
    billing_address_country = 'billing_address_country'
    billing_address_zip_code = 'billing_address_zip_code'
    group_ids = 'group_ids'
    segment_ids = 'segment_ids'
    note = 'note'
    metadata = 'metadata'
    customer_tax_exemption_status = 'customer_tax_exemption_status'


@dataclass(frozen = False)
class CustomersDataModel:
    """
    An Apteo model to store customers
    Each class represents a row in the standard orders table for each churn template
    """

    customer_id: object = None
    created_at: object = None
    updated_at: object = None
    email_address: object = None
    phone_number: object = None

    # Name (Square doesn't report full name so we'll concat and create it)
    name: object = None
    first_name: object = None
    last_name: object = None

    # Address
    customer_address_first_line: object = None
    customer_address_second_line: object = None
    customer_address_city: object = None
    customer_address_state: object = None
    customer_address_country: object = None
    customer_address_zip_code: object = None

    # Shipping Address
    shipping_address_first_line: object = None
    shipping_address_second_line: object = None
    shipping_address_city: object = None
    shipping_address_state: object = None
    shipping_address_country: object = None
    shipping_address_zip_code: object = None

    # Billing Address
    billing_address_first_line: object = None
    billing_address_second_line: object = None
    billing_address_city: object = None
    billing_address_state: object = None
    billing_address_country: object = None
    billing_address_zip_code: object = None

    # Square provides groups and segment IDs (storing them if we use them later)
    group_ids: object = None
    segment_ids: object = None

    # Other details about a customer
    note: object = None
    metadata: object = None
    # Provided via stripe
    customer_tax_exemption_status: object = None

    def set_key(self, key, value):
        """
        Set a key on the object

        :param key: (str) The key to set
        :param value: (obj) The value of the key to set
        """

        self.__dict__[key] = value

    def to_dict(self):
        """
        Return a dict representing the object - this will also convert nested object to dict
        :return: (dict)
        """

        return asdict(self)

    @classmethod
    def to_dataframe(cls, customer_records):
        """
        Take a list of <CustomersDataModel> objects and return it as a pandas dataframe

        :param customer_records: <list<CustomersDataModel>>
        :return: pd.DataFrame
        """

        if customer_records is None or not isinstance(customer_records, list) or len(customer_records) == 0:
            return None

        customer_records = [record.to_dict() for record in customer_records]
        df = pd.DataFrame.from_records(customer_records)
        df['group_ids'] = df['group_ids'].astype('str')
        df['segment_ids'] = df['segment_ids'].astype('str')
        df['metadata'] = df['metadata'].astype('str')

        return df


