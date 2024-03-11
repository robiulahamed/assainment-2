try:
    with open('input.txt ','r') as input_file:
        data=input_file.read()


        process_data = data.lower()
         
        with open('output.txt','w') as output_file:
            output_file.write(process_data)

    print("Data priceesed and weitten to output.txt successful ")


except FileNotFoundError:
    print("error: the input file 'input.txt' does   not exist.")

except PermissionError:
    print("Error: permission denied to open the input file.")

except IOError as ie:
    print(f"ioerror occured: {str(ie)}")
except Exception as ex:
    print("An error occured: ",str(ex))
        