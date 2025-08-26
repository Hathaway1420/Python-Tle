import struct
num_records = int(input("How many records do you want to create?"))

with open("record.bin","wb") as file:
    id_num = int(input("Enter ID: "))
    name = input("Enter Age:")
    age = int(input("Enter Age: "))
    gpa = float(input("Enter GPA: "))

    data = struct.pack('i120sif', id_num, name.encode(), age, gpa)
    file.write(data)
print(f"{num_records}records have been written to records.bin")