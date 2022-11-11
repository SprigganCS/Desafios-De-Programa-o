def main():
  while(1):
    try:
      aux = input()
      aux = aux.split()
      size = int(aux[0])
      nums = aux[1][:]
      if size == 0:
        break
    except EOFError as e:
      break


    #print(len(nums)) #quantidade de letras
    #print(nums,"\n") #letras


    #inicio da rotina
    for i in nums:
      
      if i == "0":
        print(" ", "-"*size)
        for i in range(size):
          print("","|"," "*(size-2),"|")

        for i in range(size):
          print("","|"," "*(size-2),"|")
        print(" ", "-"*size,)

      elif i == "1":
        print(" "*(size+2))
        for i in range(size):
          print(" "*(size+1),"|")
        print(" "*(size+2))
        for i in range(size):
          print(" "*(size+1),"|")


      elif i == "2":
        print(" ", "-"*size)
        for i in range(size):
          print(" "*(size+1),"|")
        print(" ", "-"*size)
        for i in range(size):
          print("","|"," "*(size+1))
        print(" ", "-"*size)

      elif i == "3":
        print(" ", "-"*size)
        for i in range(size):
          print(" "*(size+1),"|")
        print(" ", "-"*size)
        for i in range(size):
          print(" "*(size+1),"|")
        print(" ", "-"*size)
      
      elif i == "4":
        print(" "*(size+2))
        for i in range(size):
          print("","|"," "*(size-2),"|")
        print(" ", "-"*size)
        for i in range(size):
          print(" "*(size+1),"|")

      elif i == "5":
        print(" ", "-"*size)
        for i in range(size):
          print("","|"," "*(size+1))
        print(" ", "-"*size)
        for i in range(size):
          print(" "*(size+1),"|")
        print(" ", "-"*size)

      elif i == "6":
        print(" ", "-"*size)
        for i in range(size):
          print("","|"," "*(size+1))
        print(" ", "-"*size)
        for i in range(size):
          print("","|"," "*(size-2),"|")
        print(" ", "-"*size)
      
      elif i == "7":
        print(" ", "-"*size)
        for i in range(size):
          print(" "*(size+1),"|")
        print(" "*(size+2))
        for i in range(size):
          print(" "*(size+1),"|")
      
      elif i == "8":
        print(" ", "-"*size)
        for i in range(size):
          print("","|"," "*(size-2),"|")
        print(" ", "-"*size)
        for i in range(size):
          print("","|"," "*(size-2),"|")
        print(" ", "-"*size)
      
      elif i == "9":
        print(" ", "-"*size)
        for i in range(size):
          print("","|"," "*(size-2),"|")
        print(" ", "-"*size)
        for i in range(size):
          print(" "*(size+1),"|")
        print(" ", "-"*size)

      else:
        print("erro")
    print("\n")

main()