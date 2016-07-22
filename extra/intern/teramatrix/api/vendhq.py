import urllib2
import json
import subprocess
# to genrate authorization code  and get access token which can connect to vendhq API

# code = 'SAj5jdILyUFVUQ7hIFd5KlFJXTN5hDjI4FqldcrL'
# domain_prefix  = 'newteramatrix'
# signature='ed5b1b4efcbe86284890e39b81b083ea7c6c5dc33320376f7f131c9e594650c7'

# customer id
# id = '02dcd191-ae2b-11e6-f485-48f741e887d7'
# genrated access_token
access_token = '5OtjwgBqfHJZh045rCfEd:aMEXuHw1HJdRTT9efQ'


file = open('apidata.txt',"w")

# url to connect to application for customer api
#post the data to customers
# customer_id  = subprocess.check_output("python ~/extra/intern/teramatrix/api/post_customer.py",shell=True)
# print str(customer_id)
customer_id = raw_input("Customer id = ")
url_customer = "https://newteramatrix.vendhq.com/api/customers?access_token="+access_token
json_obj  = urllib2.urlopen(url_customer)
data = json.load(json_obj)
file.write("Customer's :-\n")
#get the data from customers
for customer in data['customers']:
	if str(customer_id) == str(customer['id']):
		file.write("Post \n")
		file.write("Id = "+str(customer['id'])+"\n")
		file.write("Name = "+str(customer['name'])+"\n")
		file.write("Email = "+str(customer['email'])+"\n")
		file.write("Loyalty Balance = "+str(customer['loyalty_balance'])+"\n")
		file.write("Company Name = "+str(customer['contact']['company_name'])+"\n")
		file.write("\n")
	else:
		file.write("Get \n")
		file.write("Id = "+str(customer['id'])+"\n")
		file.write('Name = '+str(customer['name'])+"\n")
		file.write('Phone = '+str(customer['contact'])+"\n")
		file.write('Account Balance = '+str(customer['balance'])+"\n")
		file.write('Loyalty Points = '+str(customer['loyalty_balance'])+"\n")
		file.write("\n")


# url to connect to application for outlets api
url_outlets = "https://newteramatrix.vendhq.com/api/outlets?access_token="+access_token
json_obj  = urllib2.urlopen(url_outlets)
data = json.load(json_obj)
file.write("\n")
file.write("Outlet's :- \n")
for outlet in data['outlets']:
	# if id == outlet['id']:
	file.write("Id = "+str(outlet['id'])+"\n")
	file.write("Name = "+str(outlet['name'])+"\n") 
	file.write("Location = "+str(outlet['time_zone'])+"\n")
	file.write("Contact Person = "+str(outlet['contact']['company_name'])+"\n")
	file.write("\n")

# url to connect to application for payment type api
url_ptypes = "https://newteramatrix.vendhq.com/api/payment_types?access_token="+access_token
json_obj  = urllib2.urlopen(url_ptypes)
data = json.load(json_obj)
file.write("\n")
file.write("Payment types:- \n")
file.write(json.dumps(data,indent=4,sort_keys=True))
file.write("\n")

file.write("\n")
file.write("Loyalty program :- \n")
for product in data['payment_types']:
	if product['name']=="Loyalty":
		file.write("Id = "+str(product['id'])+"\n")
		file.write("Payment Type = "+str(product['payment_type'])+"\n")
		file.write("Payment Type Id = "+str(product['payment_type_id'])+"\n")
		file.write("Config Url= "+str(product['config'])+"\n")
	file.write("\n")


# url to connect to application for products api
# post the product to api
# product_id  = subprocess.check_output("python ~/extra/intern/teramatrix/api/post_product.py",shell=True)
# print str(product_id)
product_id = raw_input("Product is = ")
url_products = "https://newteramatrix.vendhq.com/api/products?access_token="+access_token
json_obj  = urllib2.urlopen(url_products)
data = json.load(json_obj)
file.write("\n")
# get the products from api
file.write("\n")
file.write("Products :- \n")
arr=[]
for item in data['products']:
	if str(product_id)==str(product['id']):
		file.write("Post \n")
		file.write("Id = "+str(product['id'])+"\n")
		file.write("Type = "+str(product['type'])+"\n")
		file.write("Name = "+str(product['base_name'])+"\n")
		file.write("Brand Name = "+str(product['brand_name'])+"\n")
		file.write("Sku = "+str(product['sku'])+"\n")
		file.write("Price = "+str(product['price'])+"\n")
		file.write("Tax = "+str(product['tax'])+"\n")
	else:
		file.write("Get \n")
		file.write("Item = "+str(item['name'])+"\n")
		file.write("Imange = "+str(item['image'])+"\n")
		file.write("Price = "+str(item['price'])+"\n")
		file.write("Tax Amount = "+str(item['tax_rate'])+"\n")
		file.write("Menu Description = "+str(item['description'])+"\n")
		if item['tags']:
			arr.append([item['tags']])

for item in data['products']:
	for x in range(0,len(arr)):
		if item['tags']==arr[x][0]:
			arr[x].append(item['name'])
for x in range(0,len(arr)):
	file.write("tags = "+str(arr[x][0])+"\n")
	for y  in range(1,len(arr[x])):
		file.write("Category = "+str(arr[x][y])+"\n")
	file.write("\n")

# # url to connect to application for register sale api
# post the sale to api
# sale_id = subprocess.check_output("python ~/extra/intern/teramatrix/api/post_sale.py",shell=True)
# print str(sale_id)
sale_id = raw_input("Sale id = ")
url_registersale = "https://newteramatrix.vendhq.com/api/register_sales?access_token="+access_token
json_obj  = urllib2.urlopen(url_registersale)
data = json.load(json_obj)
file.write("\n")
file.write("Register Sale :- \n")
for sale in data['register_sales']:
	if str(sale_id) == str(sale['id']): 
		file.write("Post \n")
		file.write("Discount = "+str(sale['register_sale_products'][0]['discount'])+"\n")
		file.write("Price = "+str(sale['register_sale_products'][0]['price'])+"\n")
		file.write("Product List = "+str(sale['register_sale_products'][0]['name'])+"\n")
		file.write("Payment Types = "+str(sale['register_sale_payments'][0]['label'])+"\n")
		file.write("Tax Price = "+str(sale['register_sale_products'][0]['tax'])+"\n")
		file.write("Loyalty = "+str(sale['register_sale_products'][0]['loyalty_value'])+"\n")
		file.write("\n")
		break