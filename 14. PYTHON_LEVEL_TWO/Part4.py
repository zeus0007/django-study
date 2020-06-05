# f = open('Part4.txt', 'r')
# f.write("Test write to simple text!")
# print('hello world!')


try:
    f = open('Part4.txt', 'r')
    f.write("Test write to simple text!")
# except IOError:
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")
