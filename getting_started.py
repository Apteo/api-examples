import uuid
import pandas as pd
import random as r
import datetime
import numpy as np
import json
import requests
import string

# First get your customers and orders, we assume you have methods named `get_customers` and `get_orders` that queries your
# database and maps them to the data classes "customers_data_model" and "orders_data_model" to map your data. Please note
# the structure of those classes to identify the format of how your attributes should be named.

customers = get_customers()
orders = get_orders()

# Now push the data to Apteo

UrlPath = "https://developers.apteo.co/api/v2/data-sources/create"
ApiKey = "Please contact us to request an API key"

# First, create the customers and orders tables on Apteo. Tables must be contained within a data source. All fields are required.

headers = {"Authorization": "Basic %s" % ApiKey}
body = {
    "dataSourceName": "E-commerce Data",
    "tables": [{

        ###### CUSTOMERS ######
        "tableName": "customers",
        "autoAssignRowId": True,
        "schema": [
            {
                "fieldName": "customer_id",
                "fieldType": "STRING",
                "isNullable": False
            },
            {
                "fieldName": "created_at",
                "fieldType": "DATETIME",
                "isNullable": True
            },
            {
                "fieldName": "updated_at",
                "fieldType": "DATETIME",
                "isNullable": True
            },
            {
                "fieldName": "name",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "first_name",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "last_name",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "customer_address_first_line",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "customer_address_second_line",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "customer_address_city",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "customer_address_state",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "customer_address_country",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "customer_address_zip_code",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "email_address",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "phone_number",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "shipping_address_first_line",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "shipping_address_second_line",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "shipping_address_city",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "shipping_address_state",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "shipping_address_country",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "shipping_address_zip_code",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "billing_address_first_line",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "billing_address_second_line",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "billing_address_city",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "billing_address_state",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "billing_address_country",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "billing_address_zip_code",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "group_ids",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "segment_ids",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "note",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "metadata",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "customer_tax_exemption_status",
                "fieldType": "STRING",
                "isNullable": True
            }
        ]

        ###### Orders ######
    }, {
        "tableName": "orders",
        "autoAssignRowId": False,
        "schema": [
            {
                "fieldName": "order_id",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "line_items",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "total_amount",
                "fieldType": "FLOAT",
                "isNullable": True
            },
            {
                "fieldName": "tax_amount",
                "fieldType": "FLOAT",
                "isNullable": True
            },
            {
                "fieldName": "tip_amount",
                "fieldType": "FLOAT",
                "isNullable": True
            },
            {
                "fieldName": "service_fee",
                "fieldType": "FLOAT",
                "isNullable": True
            },
            {
                "fieldName": "discount_amount",
                "fieldType": "FLOAT",
                "isNullable": True
            },
            {
                "fieldName": "total_amount_currency",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "tax_amount_currency",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "tip_amount_currency",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "service_fee_amount_currency",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "discount_amount_currency",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "coupon_code",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "updated_at",
                "fieldType": "DATETIME",
                "isNullable": True
            },
            {
                "fieldName": "created_at",
                "fieldType": "DATETIME",
                "isNullable": True
            },
            {
                "fieldName": "customer_id",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "order_status",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "order_source",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "location_id",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "location_name",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "location_address_first_line",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "location_address_second_line",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "location_address_city",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "location_address_state",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "location_address_country",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "location_address_zip_code",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "selected_shipping_method",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "shipping_carrier",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "shipping_address_first_line",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "shipping_address_second_line",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "shipping_address_city",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "shipping_address_state",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "shipping_address_country",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "shipping_address_zip_code",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "payment_source_type",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "card_brand",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "card_last_four_digits",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "card_expiry_month",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "card_expiry_year",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "receipt_number",
                "fieldType": "STRING",
                "isNullable": True
            },
            {
                "fieldName": "receipt_url",
                "fieldType": "STRING",
                "isNullable": True
            }
        ]
    }]
}

response = requests.post(url = UrlPath, headers = headers, data = json.dumps(body))

# The response will contain the API specific paths that you need to use to send in customers and orders
print(json.dumps(json.loads(response.content), sort_keys=True, indent=4))

# First, we can push the customers table to Apteo. We have a limit of 75 MB for a request's payload so we will make
# sure we send over customers and orders in chunks

headers = {"Authorization": "Basic %s" % ApiKey}
CustomersInsertionPath = "https://developers.apteo.co/api/v2/data-connectors/<get ID from response above>/insert"

Step = 10000
for i in range(0, len(customers), Step):
    customer_subset = customers[i : i + Step]
    body = {
        "dataRows": [customer.to_dict() for customer in customer_subset]
    }

    response = requests.post(url = CustomersInsertionPath, headers = headers, data = json.dumps(body, default = str))
    print(response.__dict__)

    # You may run into issues sending data and if you do you should retry
    if response.status_code >= 300:
        print("Error")
        print("Current iteration: %s" % i)
        break

headers = {"Authorization": "Basic %s" % ApiKey}
OrdersInsertionApiPath = "https://developers.apteo.co/api/v2/data-connectors/<get ID from response above>/insert"

# Now we send in order data. Note that line items must be represented as a string for now.

for i in range(0, len(orders), Step):
    orders = orders[i : i + Step]
    for order in orders:
        # Convert line items to a string - this is a limitation of our current API
        order.line_items = str(order.line_items.to_dict())
    body = {
        "dataRows": orders.to_dict()
    }

    response = requests.post(url = OrdersInsertionApiPath, headers = headers, data = json.dumps(body, default = str))
    print(response.__dict__)

    if response.status_code >= 300:
        print("Error")
        print("Current iteration: %s" % i)
        break