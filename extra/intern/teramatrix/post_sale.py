import requests
import json

access_token = '5OtjwgBqfHJZh045rCfEd:C81pXwMPHgkvmZlGUm'
url = "https://newteramatrix.vendhq.com/api/register_sales?access_token="+access_token

task = {
        "source": "USER",
        "source_id": "",
        "register_id":          "02dcd191-ae2b-11e6-f485-48f741e955dd",
        "market_id":            "3",
        "customer_id":          "02dcd191-ae2b-11e6-f485-48f741dfac83",
        "customer_name":        "",
        "customer":             {
        "id":               "02dcd191-ae2b-11e6-f485-48f741dfac83",
        "name":             "",
        "customer_code":    "WALKIN",
        "customer_group_id":         "02dcd191-ae2b-11e6-f485-48f741df7446",
        "customer_group_name":       "All Customers",
        "enable_loyalty":           0,
        "loyalty_balance":          "0",
        "updated_at":               "2016-07-13 12:42:28",
        "deleted_at":               "",
        "balance":                  "0",
        "year_to_date":             "0",
        "date_of_birth":            "",
        "sex":                      "",
        "custom_field_1":           "",
        "custom_field_2":           "",
        "custom_field_3":           "",
        "custom_field_4":           "",
        "note":                     "",
        "contact":  {
            }
        }
,
        "user_id":              "02dcd191-ae2b-11e6-f485-48f741e9eb75",
        "user_name":            "cjnngr01995@gmail.com",
        "sale_date":            "2016-07-14 09:36:53",
        "created_at":            "2016-07-14 09:37:13",
        "updated_at":            "2016-07-14 09:37:13",
        "total_price":          100,
        "total_cost":           110,
        "total_tax":            0,
        "tax_name":             "No Tax",
        "note":                 "",
        "status":               "CLOSED",
        "short_code":           "3twqtv",
        "invoice_number":       "1",
        "return_for":           "",
        "register_sale_products": [        {
             "id"                                 : "ce8b4621-5c19-9e72-11e6-49a67d6ec069",
             "product_id"                         : "02dcd191-ae80-11e6-f485-48f7421226be",
             "register_id"                        : "02dcd191-ae2b-11e6-f485-48f741e955dd",
             "sequence"                           : "0",
             "handle"                             : "Sunglasses",
             "sku"                                : "10012",
             "name"                               : "Sunglasses",
             "quantity"                           : 1,
             "price"                              : 100,
             "cost"                               : 10,
             "price_set"                          : 0,
             "discount"                           : 10,
             "loyalty_value"                      : 2,
             "tax"                                : 0,
             "tax_id"                             : "02dcd191-ae2b-11e6-f485-48f741e18efc",
             "tax_name"                           : "No Tax",
             "tax_rate"                           : 0,
             "tax_total"                          : 0,
             "price_total"                        : 200,
             "display_retail_price_tax_inclusive" : "0",
             "status"                             : "CONFIRMED",
             "attributes" : [
                                                {
                    "name" : "line_note",
                    "value": ""
                }
                            ]
        }             ],
        "totals":           { "total_tax"        : 0,
                              "total_price"      : 200,
                              "total_payment"        : 200,
                              "total_to_pay"          : 0                            },
        "register_sale_payments" :        [      {
            "id"                       : "ce8b4621-5c19-9e72-11e6-49a67f998faa",
            "payment_type_id"          : "2",
            "register_id"              : "02dcd191-ae2b-11e6-f485-48f741e955dd",
            "retailer_payment_type_id" : "02dcd191-ae80-11e6-f485-498615814f39",
            "name"                     : "Cheque",
                        "label"                    : "Cheque",
            "payment_date"             : "2016-07-14 09:36:53",
            "amount"                   : 200                }    ]
                        ,"taxes": [
                                            {
                    "id": "41e1f263-48f7-11e6-b485-02dcd191ae2b",
                    "tax": 0,
                    "name": "No Tax",
                    "rate": 0                }
                                    ]
             }

resp = requests.post(url_customer,data=json.dumps(task))
print  "sale id = "+str(resp.json()['register_sale']['id'])