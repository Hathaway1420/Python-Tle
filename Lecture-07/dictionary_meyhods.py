student = {"name": "alice", "age":26, "major":"computer Science"}

print(student.keys())
print(student.values())
print(student.items())

print(student.get("name"))
print(student.get("grade","not found"))

major = student.pop("major")
print(major)
print(student)

last_item = student.popitem()
print(last_item)
print(student)

student.clear()
print(student)