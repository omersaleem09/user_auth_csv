ds = [
{
"type": "GET",
"status": 200,
"page": "example.com/one"
},
{
"type": "POST",
"status": 200,
"page": "example.com/two"
},
{
"type": "GET",
"status": 404,
"page": "example.com/three"
},
{
"type": "POST",
"status": 403,
"page": "example.com/four"
},
{
"type": "GET",
"status": 500,
"page": "example.com/five"
},
{
"type": "GET",
"status": 403,
"page": "example.com/six"
},
{
"type": "POST","status": 403,
"page": "example.com/seven"
},
{
"type": "GET",
"status": 403,
"page": "example.com/eight"
}
]

list_of_pages = []

for i in ds:
    if i['type'] == "GET" and i['status'] == 403:
        list_of_pages.append(i['page'])

print("LIST OF PAGES")
print(list_of_pages)