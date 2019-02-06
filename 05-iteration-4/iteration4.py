def iterator(input_vals):
    
    for x in input_vals:
        if type(x) != list:
            print(x)
        else:
            for el in x:
                if type(el) == list:
                    for y in el:
                        print(y)
                else:
                    print(el)
                   

iterator([1, 2, ['jeff', 'tom'], [42, ['billy', 'jason']]])

