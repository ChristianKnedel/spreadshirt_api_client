
# Setup
First, you need to setup your API credentials:
sp_client = Spreadshirt("-!- api_key -!-", '-!- shop id -!-')

# Examples
## List Products
```python
list_data = sp_client.get_sellables(1)
print(list_data['sellables'][0]['name'])
print(list_data['sellables'][0]['description'])
...
```

## List Departments
```python
departments = sp_client.get_departments()
print(departments['productTypeDepartments'][0]['name'])
```

## Product
```python
sellable = sp_client.get_sellable( sellable_id, idea_id, appearance_id)
print( sellable['name'] )
print( sellable['price'] )
print( sellable['tags'] )
print( sellable['images'] )
...
```
