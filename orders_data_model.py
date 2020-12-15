from enum import Enum

import pandas as pd
from dataclasses import dataclass, asdict


@dataclass(frozen = False)
class OrderLineItemDataModel:
    """
    A data model to store the individual line items of an order
    """

    product_id: object = None
    product_name: object = None
    quantity: object = None
    product_cost: object = None


class OrderFields(Enum):
    order_id = 'order_id'
    created_at = 'created_at'
    updated_at = 'updated_at'
    customer_id = 'customer_id'
    order_status = 'order_status'
    order_source = 'order_source'
    location_id = 'location_id'
    location_name = 'location_name'
    location_address_first_line = 'location_address_first_line'
    location_address_second_line = 'location_address_second_line'
    location_address_city = 'location_address_city'
    location_address_state = 'location_address_state'
    location_address_country = 'location_address_country'
    location_address_zip_code = 'location_address_zip_code'

    line_items = 'line_items'

    total_amount = 'total_amount'
    tax_amount = 'tax_amount'
    tip_amount = 'tip_amount'
    service_fee_amount = 'service_fee_amount'
    discount_amount = 'discount_amount'

    # Order Currencies
    total_amount_currency = 'total_amount_currency'
    tax_amount_currency = 'tax_amount_currency'
    tip_amount_currency = 'tip_amount_currency'
    service_fee_amount_currency = 'service_fee_amount_currency'
    discount_amount_currency = 'discount_amount_currency'
    selected_shipping_method = 'selected_shipping_method'
    shipping_address_first_line = 'shipping_address_first_line'
    shipping_address_second_line = 'shipping_address_second_line'
    shipping_address_city = 'shipping_address_city'
    shipping_address_state = 'shipping_address_state'
    shipping_address_country = 'shipping_address_country'
    shipping_address_zip_code = 'shipping_address_zip_code'
    payment_source_type = 'payment_source_type'
    card_brand = 'card_brand'
    card_last_four_digits = 'card_last_four_digits'
    card_expiry_month = 'card_expiry_month'
    card_expiry_year = 'card_expiry_year'
    receipt_number = 'receipt_number'
    receipt_url = 'receipt_url'
    coupon_code = 'coupon_code'


@dataclass(frozen = False)
class OrdersDataModel:
    """
    An Apteo data model to store orders.
    Each class represents a row in the standard orders table for each churn template
    """

    order_id: object = None
    created_at: object = None
    updated_at: object = None
    customer_id: object = None
    order_status: object = None
    order_source: object = None

    # Details about the location where the order took place - mostly for Square
    location_id: object = None
    location_name: object = None
    location_address_first_line: object = None
    location_address_second_line: object = None
    location_address_city: object = None
    location_address_state: object = None
    location_address_country: object = None
    location_address_zip_code: object = None

    # Line Items
    line_items: object = None

    # Order Amounts
    total_amount: object = None
    tax_amount: object = None
    tip_amount: object = None
    service_fee_amount: object = None
    discount_amount: object = None

    # Order Currencies
    total_amount_currency: object = None
    tax_amount_currency: object = None
    tip_amount_currency: object = None
    service_fee_amount_currency: object = None
    discount_amount_currency: object = None

    # Shipping Address (mostly for stripe)
    selected_shipping_method: object = None
    shipping_carrier: object = None
    shipping_address_first_line: object = None
    shipping_address_second_line: object = None
    shipping_address_city: object = None
    shipping_address_state: object = None
    shipping_address_country: object = None
    shipping_address_zip_code: object = None

    # Payment Details
    payment_source_type: object = None
    # Card Brand will be added if its present
    card_brand: object = None
    card_last_four_digits: object = None
    card_expiry_month: object = None
    card_expiry_year: object = None
    receipt_number: object = None
    receipt_url: object = None

    coupon_code: object = None

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
    def to_dataframe(cls, orders_records):
        """
        Take a list of <OrdersDataModel> objects and return it as a pandas dataframe

        :param orders_records: <list<OrdersDataModel>>
        :return: pd.DataFrame
        """

        if orders_records is None or not isinstance(orders_records, list) or len(orders_records) == 0:
            return None

        orders_records = [record.to_dict() for record in orders_records]
        df = pd.DataFrame.from_records(orders_records)
        df['line_items'] = df['line_items'].astype('str')

        return df

