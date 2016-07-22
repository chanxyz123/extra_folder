import requests
import json
import os
access_token = '5OtjwgBqfHJZh045rCfEd:aMEXuHw1HJdRTT9efQ'
url = "https://newteramatrix.vendhq.com/api/customers?access_token="+access_token

customer = {
        "name":             "chandrajeet nagar",
        "customer_code":    "xexeaxw",
        "customer_group_id":         "02dcd191-ae2b-11e6-f485-48f741df7446",
        "customer_group_name":       "All Customers",
        "first_name":             "chandrajeet",
        "last_name":              "nagar",
        "company_name":           "TTPL",
        "phone":                  "",
        "mobile":                 "9816936041",
        "fax":                    "",
        "email":                  "cjnngr01995@gmail.com",
        "twitter":                "",
        "website" :               "",
        "physical_address1":      "",
        "physical_address2":      "",
        "physical_suburb":        "",
        "physical_city":          "Jaipur",
        "physical_postcode":      "302029",
        "physical_state":         "Rajasthan",
        "physical_country_id":    "IN",
        "postal_address1":        "",
        "postal_address2":        "",
        "postal_suburb":          "",
        "postal_city":            "Jaipur",
        "postal_postcode":        "302029",
        "postal_state":           "Rajasthan",
        "postal_country_id" :     "IN",        "enable_loyalty":           1,
        "loyalty_balance":          "0.00000",
        "updated_at":               "2016-07-15 05:13:41",
        "deleted_at":               "",
        "balance":                  "0.000",
        "year_to_date":             "0.00000",
        "date_of_birth":            "1994-09-28",
        "sex":                      "M",
        "custom_field_1":           "",
        "custom_field_2":           "",
        "custom_field_3":           "",
        "custom_field_4":           "",
        "note":                     "",
        "contact":  {
            "company_name":     "teramatrix",
            "phone":            "",
            "email":            "cjnngr01995@gmail.com"
            }
        }


resp = requests.post(url,data=json.dumps(customer))
print  resp.json()['customer']['id']
# print resp.status_code
# print json.dumps(resp.json(),indent=4,sort_keys=Tru