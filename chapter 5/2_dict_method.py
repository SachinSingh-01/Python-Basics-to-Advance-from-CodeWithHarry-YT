marks={
    "Harry": 100,
    "Shubham": 69,
    "Rohan": 98,
    0: "Harry"
}

print(marks.items()) # Ishka matlab naam ke sath number v dikhaiga 

print(marks.keys()) # Ishka matlab sirf naam dikhaiga

print(marks.values()) # Ishka matlab sirf number dikhaiga

marks.update({"Harry":  99, "Renuka": 100})
print(marks)

print(marks.get("Harry"))
print(marks["Harry"])

print(marks.get("Harry2")) #prints none
print(marks["Harry2"]) # returns an erro


