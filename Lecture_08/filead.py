def main():
    infile = open('philosopher.txt','w')
    
    file_contents =infile.read()

    infile.close()
    print(file_contents)
main()