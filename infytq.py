def update_stack(input_stack):
     temp_stack1= stack(input_stack.get_max_size())
     temp_stack2= stack(input_stack.get_max_size())
     output_stack = stack(input_stack.get_max_size())
     num = input_stack.pop()
     while (not(input_stack.is_empty())):
         top_element = input_stack.pop()
         element = input_stack.pop()
         if(top_element<element):
             temp_stack1.push(element+num)
             input_stack.push(num)
         else:
            temp_stack2.push(top_element+num)
         num+=1                                                    
     while(not temp_stack1.is_empty()):
        out_stack.push(temp_stack1.pop())
     while(not temp_stack1.is_empty()):
        out_stack.push(temp_stack1.pop())
     return out_stack