import requests
import json

access_token = '5OtjwgBqfHJZh045rCfEd:aMEXuHw1HJdRTT9efQ'
url = "https://newteramatrix.vendhq.com/api/register_sales?access_token="+access_token

sale = {
        "source": "USER",
        "source_id": "",
        "register_id":          "02dcd191-ae2b-11e6-f485-48f741e955dd",
        "market_id":            "3",
        "customer_id":          "02dcd191-ae2b-11e6-f485-48f741dfac83",
        "customer_name":        " ",
        "customer":             {
        "id":               "02dcd191-ae2b-11e6-f485-48f741dfac83",
        "name":             " ",
        "customer_code":    "WALKIN",
        "customer_group_id":         "02dcd191-ae2b-11e6-f485-48f741df7446",
        "customer_group_name":       "All Customers",
        "first_name":             "",
        "last_name":              "",
        "company_name":           "",
        "phone":                  "",
        "mobile":                 "",
        "fax":                    "",
        "email":                  "",
        "twitter":                "",
        "website" :               "",
        "physical_address1":      "",
        "physical_address2":      "",
        "physical_suburb":        "",
        "physical_city":          "",
        "physical_postcode":      "",
        "physical_state":         "",
        "physical_country_id":    "",
        "postal_address1":        "",
        "postal_address2":        "",
        "postal_suburb":          "",
        "postal_city":            "",
        "postal_postcode":        "",
        "postal_state":           "",
        "postal_country_id" :     "",        "enable_loyalty":           0,
        "loyalty_balance":          "0",
        "updated_at":               "2016-07-16 03:38:28",
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
            "company_name":     "",
            "phone":            "",
            "email":            ""
            }
        }
,
        "user_id":              "02dcd191-ae2b-11e6-f485-48f741e9eb75",
        "user_name":            "cjnngr01995@gmail.com",
        "sale_date":            "2016-07-18 08:04:05",
        "created_at":            "2016-07-18 08:04:22",
        "updated_at":            "2016-07-18 08:04:22",
        "total_price":          900,
        "total_cost":           200,
        "total_tax":            0,
        "tax_name":             "No Tax",
        "note":                 "",
        "status":               "CLOSED",
        "short_code":           "cjmb8c",
        "invoice_number":       "2",
        "return_for":           "",
        "register_sale_products": [        {
             "id"                                 : "ce8b4621-5c19-8acb-11e6-4cbe29c3d77b",
             "product_id"                         : "02dcd191-ae80-11e6-f485-48f742d2c3ee",
             "register_id"                        : "02dcd191-ae2b-11e6-f485-48f741e955dd",
             "sequence"                           : "0",
             "handle"                             : "DressShirt",
             "sku"                                : "10020",
             "name"                               : "Dress Shirt \/ Cotton \/ Medium",
             "quantity"                           : 1,
             "price"                              : 90,
             "cost"                               : 20,
             "price_set"                          : 0,
             "discount"                           : 0,
             "loyalty_value"                      : 2.8,
             "tax"                                : 0,
             "tax_id"                             : "02dcd191-ae2b-11e6-f485-48f741e18efc",
             "tax_name"                           : "No Tax",
             "tax_rate"                           : 0,
             "tax_total"                          : 0,
             "price_total"                        : 900,
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
                              "total_price"      : 900,
                              "total_payment"        : 900,
                              "total_to_pay"          : 0                            },
        "register_sale_payments" :        [      {
            "id"                       : "ce8b4621-5c19-8acb-11e6-4cbe3236031c",
            "payment_type_id"          : "1",
            "register_id"              : "02dcd191-ae2b-11e6-f485-48f741e955dd",
            "retailer_payment_type_id" : "02dcd191-ae2b-11e6-f485-48f741e99055",
            "name"                     : "Cash",
                        "label"                    : "Cash",
            "payment_date"             : "2016-07-18 08:04:05",
            "amount"                   : 90                }    ]
                        ,"taxes": [
                                            {
                    "id": "41e1f263-48f7-11e6-b485-02dcd191ae2b",
                    "tax": 0,
                    "name": "No Tax",
                    "rate": 0                }
                                    ]
             }
resp = requests.post(url,data=json.dumps(sale))
print  resp.json()['register_sale']['id']