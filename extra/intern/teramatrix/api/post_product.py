import requests
import json
import os
access_token = '5OtjwgBqfHJZh045rCfEd:aMEXuHw1HJdRTT9efQ'
url = "https://newteramatrix.vendhq.com/api/products?access_token="+access_token

product =  {
"source_id":        "",
"variant_source_id": "",
"handle":           "T-shirts-1",
"type":           "Fashion",
"has_variants":   "true",
"variant_parent_id":  "",
"variant_option_one_name": "",
"variant_option_one_value": "",
"variant_option_two_name": "",
"variant_option_two_value": "",
"variant_option_three_name": "",
"variant_option_three_value": "",
"active":           "true",
"name":             "T-shirts-1",
"base_name":        "T-shirts-1",
"description":      "<p>dress to impress<\/p>",
"image":            "https:\/\/newteramatrix.vendhq.com\/images\/placeholder\/product\/no-image-white-thumb.png",
"image_large":      "https:\/\/newteramatrix.vendhq.com\/images\/placeholder\/product\/no-image-white-original.png",
"images":           [],
"sku":              "10020",
"tags":             "T-shirts-1",
"brand_id":         "02dcd191-ae80-11e6-f485-48f742390301",
"brand_name":       "Forever Diamonds-1",
"supplier_name":    "Lewis Apparel-1",
"supplier_code":    "",
"supply_price":     "0.00",
"account_code_purchase":     "",
"account_code_sales":        "",
"track_inventory":           "true",
"button_order":           "",
    "inventory": [{
        "outlet_id"      :       "02dcd191-ae2b-11e6-f485-48f741e887d7",
        "outlet_name"    :       "Main Outlet",
        "count"          :       "0.00000",
        "reorder_point"          :       "",
        "restock_level"          :       ""
}    ],
    "price_book_entries":    [    {
        "id"                :       "ed1ef6d1-cb75-039c-b0c8-6364be91bf19",
        "product_id"        :       "02dcd191-ae80-11e6-f485-4b11c7b4abd3",
        "price_book_id"     :       "02dcd191-ae2b-11e6-f485-48f741e0e249",
        "price_book_name"   :       "General Price Book (All Products)",
        "type"              :       "BASE",
        "outlet_name"       :       "",
        "outlet_id"         :       "",
        "customer_group_name" :       "All Customers",
        "customer_group_id" :       "02dcd191-ae2b-11e6-f485-48f741df7446",
        "price"             :       "400",
        "loyalty_value"     :       "null",
        "tax"               :       0,
        "tax_id"            :       "02dcd191-ae2b-11e6-f485-48f741e18efc",
        "tax_rate"          :       0,
        "tax_name"          :       "No Tax",
        "display_retail_price_tax_inclusive"          :       "400",
        "retail_price" : 0,
        "min_units"         :       "",
        "max_units"         :       "",
        "valid_from"        :       "",
        "valid_to"          :       ""
    }],
"price":            "400",
"tax":              0,
"tax_id":           "02dcd191-ae2b-11e6-f485-48f741e18efc",
"tax_rate" :        0,
"tax_name" :        "No Tax",
"taxes" : [{"outlet_id":"02dcd191-ae2b-11e6-f485-48f741e887d7","tax_id":"02dcd191-ae2b-11e6-f485-48f741e18efc"}],
"display_retail_price_tax_inclusive"          :       "400",
"retail_price" : 0,
"updated_at":       "2016-07-16 04:57:21",
"deleted_at":       ""
}

resp = requests.post(url,data=json.dumps(product))
# print  "Customer id = "+str(resp.json())
# print resp.status_code
# print json.dumps(resp.json(),indent=4,sort_keys=True)
print resp.json()['product']['id']